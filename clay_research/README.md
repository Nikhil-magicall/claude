# Clay contact research — DiscoLike HR/staffing list

Finds CEO / Founder / Partner / VP / Director (sales & marketing) contacts for the
7,007 companies in the DiscoLike export, via the Clay MCP connector.

## Files
| File | Purpose |
|---|---|
| `worklist.csv` | 7,007 deduped domains sorted by DiscoLike score (highest first) |
| `results.jsonl` | Append-only raw results, one JSON object per company searched |
| `contacts_found.csv` | Final joined output (regenerate with `merge.py`) |
| `next_batch.py` | Prints the next N unsearched domains — the resume point |
| `merge.py` | Rebuilds `contacts_found.csv` from `results.jsonl` |
| `add.py` | Appends one company's contacts to `results.jsonl` |

## Resuming
```bash
python3 next_batch.py 50   # next 50 domains to search
python3 merge.py           # rebuild output + print progress
```
Resume is driven purely by which domains appear in `results.jsonl`, so the run is
safe to stop and restart at any point. Companies with zero matches are recorded as
an empty contact list so they are not re-searched.

## Output columns
Company context (domain, name, DiscoLike score, employees, revenue, location) joined to
each contact: name, title, `role_bucket` (CEO / Founder / Partner / VP / Director / CRO-CMO),
`sales_or_marketing` flag, LinkedIn URL, location, title start date, and
`contact_at_this_company` — `N` flags a contact Clay returned whose current employer
domain differs from the searched company (they have since moved on).
