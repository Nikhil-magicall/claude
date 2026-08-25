#!/usr/bin/env python3
"""Merge Clay contact results (results.jsonl) into a final CSV joined to company data."""
import csv, json, os, sys, re

BASE = os.path.dirname(os.path.abspath(__file__))
WORK = os.path.join(BASE, 'worklist.csv')
RES  = os.path.join(BASE, 'results.jsonl')
OUT  = os.path.join(BASE, 'contacts_found.csv')

# Role bucketing — applied to the LinkedIn title text.
BUCKETS = [
    ('CEO',       r'\b(chief executive|ceo)\b'),
    ('Founder',   r'\b(founder|co-?founder|owner|president)\b'),
    ('CRO/CMO',   r'\b(chief revenue|cro|chief marketing|cmo|chief growth|chief commercial)\b'),
    ('Partner',   r'\b(partner|principal|managing director)\b'),
    ('VP',        r'\b(vp|vice president|svp|evp)\b'),
    ('Director',  r'\b(director|head of)\b'),
]
SALESMKT = re.compile(r'\b(sales|marketing|revenue|growth|business development|bizdev|bd|demand gen|commercial|go.?to.?market|gtm|client|account)\b', re.I)

def bucket(title):
    t = (title or '').lower()
    for name, pat in BUCKETS:
        if re.search(pat, t, re.I):
            return name
    return 'Other'

def main():
    companies = {}
    with open(WORK, newline='') as f:
        for r in csv.DictReader(f):
            companies[r['domain']] = r

    seen = set()
    rows = []
    if os.path.exists(RES):
        with open(RES) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except json.JSONDecodeError:
                    continue
                dom = rec.get('domain', '')
                co = companies.get(dom, {})
                for c in rec.get('contacts', []):
                    key = (dom, c.get('profile_id') or c.get('url') or c.get('name'))
                    if key in seen:
                        continue
                    seen.add(key)
                    title = c.get('title', '')
                    rows.append({
                        'company_domain': dom,
                        'company_name': co.get('company_name', ''),
                        'company_score': co.get('score', ''),
                        'company_employees': co.get('employees', ''),
                        'company_revenue': co.get('revenue', ''),
                        'company_city': co.get('city', ''),
                        'company_state': co.get('state', ''),
                        'company_country': co.get('country', ''),
                        'contact_name': c.get('name', ''),
                        'contact_title': title,
                        'role_bucket': bucket(title),
                        'sales_or_marketing': 'Y' if SALESMKT.search(title or '') else '',
                        'linkedin_url': c.get('url', ''),
                        'contact_location': c.get('location', ''),
                        'title_start_date': c.get('start_date', ''),
                        'contact_at_this_company': 'Y' if (c.get('contact_domain') or dom) == dom else 'N',
                    })

    rows.sort(key=lambda r: (-int(r['company_score'] or 0), r['company_domain'], r['contact_name']))
    if rows:
        with open(OUT, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    done = set()
    if os.path.exists(RES):
        with open(RES) as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        done.add(json.loads(line).get('domain'))
                    except json.JSONDecodeError:
                        pass
    print(f'companies searched : {len(done)} / {len(companies)}')
    print(f'contacts written   : {len(rows)}  -> {OUT}')
    from collections import Counter
    print('by role bucket     :', dict(Counter(r['role_bucket'] for r in rows).most_common()))
    print('sales/marketing tag:', sum(1 for r in rows if r['sales_or_marketing'] == 'Y'))

if __name__ == '__main__':
    main()
