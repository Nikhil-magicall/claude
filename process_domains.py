#!/usr/bin/env python3
"""Process all domains from the outbound-agencies tag and enrich with employee size."""

import requests
import json
import csv
import time
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

# Config
OAUTH_TOKEN = open('/home/claude/.claude/remote/.oauth_token').read().strip()
MCP_URL = (
    "https://api.anthropic.com/v2/ccr-sessions/cse_01WBNEHFhVKJgcr9xtEtc7WX/mcp"
    "?mcp_url=https%3A%2F%2Fapi.discolike.com%2Fv1%2Fmcp"
    "&mcp_server_id=57c890e7-36c7-519e-a206-a537616eb8ac"
    "&toolbox_mcp_server_id=9d74a502-cbfb-45b1-ab7d-0c0373a09ce5"
)
HEADERS = {
    "Authorization": f"Bearer {OAUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-Session-UUID": "cse_01WBNEHFhVKJgcr9xtEtc7WX",
    "anthropic-version": "2023-06-01",
}
DOMAINS_FILE = "/tmp/all_domains.txt"
OUTPUT_CSV = "/home/user/claude/outbound_agencies_employee_size.csv"
BATCH_SIZE = 100
MAX_WORKERS = 8
RETRY_LIMIT = 3


def call_append_data(domains, attempt=0):
    """Call DiscoLike append-data for a batch of domains."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "append-data",
            "arguments": {
                "filters": {"domains": domains, "dataset": ["bizdata"]},
                "fields": ["domain", "employees"]
            }
        }
    }
    try:
        r = requests.post(MCP_URL, json=payload, headers=HEADERS, timeout=60, stream=True)
        # Parse SSE stream
        for line in r.iter_lines():
            if line and line.startswith(b'data: '):
                data = json.loads(line[6:])
                result = data.get('result', {})
                if 'structuredContent' in result:
                    return result['structuredContent'].get('results', [])
                # Fallback: parse text content
                content = result.get('content', [])
                for c in content:
                    if c.get('type') == 'text':
                        try:
                            return json.loads(c['text']).get('results', [])
                        except:
                            pass
    except Exception as e:
        if attempt < RETRY_LIMIT:
            time.sleep(2 ** attempt)
            return call_append_data(domains, attempt + 1)
        print(f"  ERROR after {RETRY_LIMIT} retries: {e}", file=sys.stderr)
    return []


def get_last_processed_domain():
    """Find the last domain already in the CSV."""
    try:
        with open(OUTPUT_CSV, 'r') as f:
            lines = f.readlines()
        if len(lines) > 1:
            return lines[-1].split(',')[0].strip()
    except FileNotFoundError:
        pass
    return None


def main():
    # Read all domains
    with open(DOMAINS_FILE) as f:
        all_domains = [line.strip() for line in f if line.strip()]

    total = len(all_domains)
    print(f"Total domains: {total}")

    # Find where to start
    last_domain = get_last_processed_domain()
    start_idx = 0
    if last_domain:
        try:
            start_idx = all_domains.index(last_domain) + 1
        except ValueError:
            pass

    remaining = all_domains[start_idx:]
    print(f"Already processed: {start_idx}, Remaining: {len(remaining)}")

    if not remaining:
        print("All domains already processed!")
        return

    # Create batches
    batches = [remaining[i:i+BATCH_SIZE] for i in range(0, len(remaining), BATCH_SIZE)]
    print(f"Batches to process: {len(batches)}")

    processed = 0
    with open(OUTPUT_CSV, 'a', newline='') as f:
        writer = csv.writer(f)

        # Process in parallel groups
        group_size = MAX_WORKERS
        for group_start in range(0, len(batches), group_size):
            group = batches[group_start:group_start + group_size]

            with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
                futures = {executor.submit(call_append_data, batch): i
                          for i, batch in enumerate(group)}

                results_map = {}
                for future in as_completed(futures):
                    idx = futures[future]
                    results_map[idx] = future.result()

            # Write results in order
            for idx in sorted(results_map.keys()):
                results = results_map[idx]
                for r in results:
                    if r and r.get('domain'):
                        writer.writerow([r['domain'], r.get('employees', '')])
                        processed += 1

            f.flush()
            total_done = start_idx + processed
            pct = total_done / total * 100
            print(f"Progress: {total_done}/{total} ({pct:.1f}%) - Batch group {group_start//group_size + 1}/{(len(batches)+group_size-1)//group_size}")

    print(f"\nDone! Total rows written this session: {processed}")

    # Final count
    with open(OUTPUT_CSV) as f:
        total_rows = sum(1 for _ in f)
    print(f"Total CSV rows (including header): {total_rows}")


if __name__ == '__main__':
    main()
