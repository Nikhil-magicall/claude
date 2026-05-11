#!/usr/bin/env python3
"""Scrape all Instantly.ai warmup pool mailboxes and save to CSV."""

import requests
import json
import csv
import time
import sys

# Config
OAUTH_TOKEN = open('/home/claude/.claude/remote/.oauth_token').read().strip()
MCP_URL = (
    "https://api.anthropic.com/v2/ccr-sessions/cse_01KUXhGxJD3ZX7rgW71iQfE7/mcp"
    "?mcp_url=https%3A%2F%2Fmcp.sendkit.ai%2Fmcp"
    "&mcp_server_id=a73d382a-a2d0-5f99-8187-eea5b0222606"
    "&toolbox_mcp_server_id=c6911ce2-1510-4324-8e9b-90f07a77d8b5"
)
HEADERS = {
    "Authorization": f"Bearer {OAUTH_TOKEN}",
    "Content-Type": "application/json",
    "X-MCP-Server-ID": "c6911ce2-1510-4324-8e9b-90f07a77d8b5",
    "X-Session-UUID": "cse_01KUXhGxJD3ZX7rgW71iQfE7",
    "anthropic-version": "2023-06-01",
}
OUTPUT_CSV = "/home/user/claude/instantly_warmup_pool.csv"
PAGE_SIZE = 100
RETRY_LIMIT = 4

CSV_FIELDS = [
    "mailbox_id", "email", "displayName", "provider", "connectionType",
    "status", "sendingEnabled", "dailySendLimit", "sentToday",
    "warmup_enabled", "warmup_status", "warmup_currentDay", "warmup_currentVolume",
    "warmup_totalEmailsSent", "warmup_inboxRate", "warmup_spamRate",
    "warmup_promotionsRate", "warmup_replyRate", "warmup_blockRate",
    "warmup_bounceRate", "warmup_deferralRate", "warmup_openRate",
    "warmup_totalRepliesReceived", "warmup_lastCalculatedAt",
    "healthScore", "totalSent", "bounceRate", "tags", "createdAt",
]


def call_list_mailboxes(cursor=None, attempt=0):
    args = {"limit": PAGE_SIZE, "warmupEnabled": "true"}
    if cursor:
        args["cursor"] = cursor

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {"name": "list_mailboxes", "arguments": args},
    }
    try:
        r = requests.post(MCP_URL, json=payload, headers=HEADERS, timeout=60, stream=True)
        for line in r.iter_lines():
            if line and line.startswith(b'data: '):
                data = json.loads(line[6:])
                result = data.get('result', {})
                # Try text content (primary format)
                for c in result.get('content', []):
                    if c.get('type') == 'text':
                        parsed = json.loads(c['text'])
                        return parsed.get('data', []), parsed.get('pagination', {})
                # Fall back to structuredContent
                if 'structuredContent' in result:
                    sc = result['structuredContent']
                    return sc.get('data', []), sc.get('pagination', {})
    except Exception as e:
        if attempt < RETRY_LIMIT:
            wait = 2 ** attempt
            print(f"  Retry {attempt+1}/{RETRY_LIMIT} after {wait}s: {e}", file=sys.stderr)
            time.sleep(wait)
            return call_list_mailboxes(cursor, attempt + 1)
        print(f"  FATAL after {RETRY_LIMIT} retries: {e}", file=sys.stderr)
    return [], {}


def flatten(mailbox):
    w = mailbox.get('warmup', {})
    m = w.get('metrics', {})
    return {
        "mailbox_id":                   mailbox.get('_id', ''),
        "email":                        mailbox.get('email', ''),
        "displayName":                  mailbox.get('displayName', ''),
        "provider":                     mailbox.get('provider', ''),
        "connectionType":               mailbox.get('connectionType', ''),
        "status":                       mailbox.get('status', ''),
        "sendingEnabled":               mailbox.get('sendingEnabled', ''),
        "dailySendLimit":               mailbox.get('dailySendLimit', ''),
        "sentToday":                    mailbox.get('sentToday', ''),
        "warmup_enabled":               w.get('enabled', ''),
        "warmup_status":                w.get('status', ''),
        "warmup_currentDay":            w.get('currentDay', ''),
        "warmup_currentVolume":         w.get('currentVolume', ''),
        "warmup_totalEmailsSent":       m.get('totalEmailsSent', ''),
        "warmup_inboxRate":             m.get('inboxRate', ''),
        "warmup_spamRate":              m.get('spamRate', ''),
        "warmup_promotionsRate":        m.get('promotionsRate', ''),
        "warmup_replyRate":             m.get('replyRate', ''),
        "warmup_blockRate":             m.get('blockRate', ''),
        "warmup_bounceRate":            m.get('bounceRate', ''),
        "warmup_deferralRate":          m.get('deferralRate', ''),
        "warmup_openRate":              m.get('openRate', ''),
        "warmup_totalRepliesReceived":  m.get('totalRepliesReceived', ''),
        "warmup_lastCalculatedAt":      m.get('lastCalculatedAt', ''),
        "healthScore":                  mailbox.get('setupStatus', {}).get('healthScore', ''),
        "totalSent":                    mailbox.get('totalSent', ''),
        "bounceRate":                   mailbox.get('bounceRate', ''),
        "tags":                         '|'.join(mailbox.get('tags', [])),
        "createdAt":                    mailbox.get('createdAt', ''),
    }


def main():
    cursor = None
    total_fetched = 0
    page = 0

    with open(OUTPUT_CSV, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()

        while True:
            page += 1
            mailboxes, pagination = call_list_mailboxes(cursor)

            if not mailboxes:
                print(f"No mailboxes returned on page {page}, stopping.")
                break

            for mb in mailboxes:
                writer.writerow(flatten(mb))

            total_fetched += len(mailboxes)
            total = pagination.get('total', '?')
            has_more = pagination.get('hasMore', False)
            cursor = pagination.get('nextCursor')

            print(f"Page {page}: fetched {len(mailboxes)} | total so far: {total_fetched}/{total}")
            f.flush()

            if not has_more or not cursor:
                break

            time.sleep(0.2)  # be gentle with the API

    print(f"\nDone. {total_fetched} warmup-pool mailboxes saved to {OUTPUT_CSV}")


if __name__ == '__main__':
    main()
