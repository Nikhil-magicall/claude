#!/usr/bin/env python3
import json
import csv
import sys
import os

def extract_linkedin(social_urls):
    if not social_urls:
        return ""
    if isinstance(social_urls, dict):
        return social_urls.get("linkedin") or ""
    if isinstance(social_urls, list):
        for url in social_urls:
            if isinstance(url, str) and "linkedin.com" in url:
                return url
    return ""

def process_batch_file(filepath, writer):
    with open(filepath) as f:
        data = json.load(f)
    results = data.get("results", [])
    for r in results:
        writer.writerow({
            "domain": r.get("domain") or "",
            "description": (r.get("description") or "").replace("\n", " ").strip(),
            "linkedin": extract_linkedin(r.get("social_urls")),
            "employees": r.get("employees") or "",
        })
    return len(results)

def main():
    output_file = "/home/user/claude/outbound_agencies_merged.csv"
    file_exists = os.path.exists(output_file)

    with open(output_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["domain", "description", "linkedin", "employees"],
                                quoting=csv.QUOTE_ALL)
        if not file_exists or os.path.getsize(output_file) == 0:
            writer.writeheader()

        for batch_file in sys.argv[1:]:
            count = process_batch_file(batch_file, writer)
            print(f"Processed {count} rows from {os.path.basename(batch_file)}")

if __name__ == "__main__":
    main()
