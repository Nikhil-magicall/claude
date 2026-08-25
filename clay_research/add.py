#!/usr/bin/env python3
"""Append one company's Clay results to results.jsonl. Usage: add.py <domain> <<< '<json contacts array>'"""
import json, sys, os
BASE = os.path.dirname(os.path.abspath(__file__))
domain = sys.argv[1]
raw = sys.stdin.read().strip()
contacts = json.loads(raw) if raw else []
with open(os.path.join(BASE, 'results.jsonl'), 'a') as f:
    f.write(json.dumps({'domain': domain, 'contacts': contacts}) + '\n')
print(f'{domain}: {len(contacts)} contacts')
