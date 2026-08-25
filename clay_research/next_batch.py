#!/usr/bin/env python3
"""Print the next N unsearched domains from the worklist (resume point)."""
import csv, json, os, sys
BASE = os.path.dirname(os.path.abspath(__file__))
n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
done = set()
res = os.path.join(BASE, 'results.jsonl')
if os.path.exists(res):
    with open(res) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    done.add(json.loads(line).get('domain'))
                except json.JSONDecodeError:
                    pass
with open(os.path.join(BASE, 'worklist.csv'), newline='') as f:
    todo = [r['domain'] for r in csv.DictReader(f) if r['domain'] not in done]
print(f'# done={len(done)} remaining={len(todo)}')
for d in todo[:n]:
    print(d)
