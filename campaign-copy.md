# InboxKit Enterprise Campaign Copy

One job: book the call. The offer is stated in plain words. Everything else is handled on the call.

**The offer, in one line:** We run cold email for you. You get the meetings. If it works, you scale it on our infrastructure.

Rules: under 80 words, plain text, no links until touch 3, one question per email. Rotate the four openers across the list; the follow-ups are shared.

---

## Email 1 — four openers (A/B/C/D)

**A — Straight offer**
Subject: `cold email for {{company}}`

> Hi {{first_name}},
>
> We run cold email for B2B software companies. Not consulting — we build the infrastructure, write the emails, send 10–25K of them to your ICP, and book the meetings into your reps' calendars.
>
> If it works, your team scales it on our infrastructure. If it doesn't, you keep the data and we part ways.
>
> Worth 20 minutes to see if {{company}} is a fit?
>
> {{sender_name}}

**B — Mailbox ceiling**
Subject: `{{sdr_count}} reps, one domain`

> Hi {{first_name}},
>
> Your {{sdr_count}} SDRs are probably each sending from one @{{domain}} mailbox at 40–50 emails a day. That caps the whole team at roughly {{monthly_ceiling}} a month, however good they are.
>
> We remove the cap. We'll prove it by running 10K of your ICP through our infrastructure and handing you the meetings.
>
> Open to a 20-minute call?
>
> {{sender_name}}

**C — Results first**
Subject: `meetings before a contract`

> Hi {{first_name}},
>
> Most vendors want a contract before they show results. We do it backwards.
>
> We run 10–25K cold emails to your ICP, on our infrastructure, and book the meetings for your reps. You look at the numbers. Then you decide whether to scale.
>
> Want me to send how the pilot works?
>
> {{sender_name}}

**D — Domain risk**
Subject: `@{{domain}} and cold email`

> Hi {{first_name}},
>
> Every cold sequence from @{{domain}} shares reputation with your billing, support, and product email. One rough quarter of outbound and your invoices land in spam.
>
> We run cold email off separate infrastructure entirely, and we'll run your first 10K contacts so you can see placement and reply rates before deciding anything.
>
> Worth a quick call?
>
> {{sender_name}}

---

## Email 2 — Day 4, same thread

> One data point: for a {{similar_company_descriptor}} we ran 25K contacts in 45 days. 96% inbox placement, 3.1% reply rate, 44 meetings booked.
>
> Their team now runs it themselves on our infrastructure.
>
> Happy to scope something similar for {{company}}.

---

## Email 3 — Day 8, new thread

Subject: `where @{{domain}} lands`

> {{first_name}} — ran a placement test on outbound from @{{domain}}. Outlook is filtering a share to junk. Gmail is mostly Promotions.
>
> Not the reps' fault. It's the domain.
>
> Can send the breakdown, and it makes a decent starting point for the pilot conversation.

---

## Email 4 — Day 13, same thread

> Bumping this. If someone else owns pipeline or sales development at {{company}}, happy to be pointed to them.

---

## Email 5 — Day 18, breakup

Subject: `closing the loop`

> Assuming the timing's off. If outbound becomes a priority next quarter, the offer stands: we run your first 10–25K cold emails, you keep the meetings either way.
>
> {{sender_name}}

---

## Variables to enrich per contact

| Variable | Source |
|---|---|
| `sdr_count` | LinkedIn headcount with SDR/BDR titles (Clay, Prospeo) |
| `monthly_ceiling` | `sdr_count × 45 × 21`, rounded |
| `domain` | Company domain |
| `similar_company_descriptor` | Pick from a short list by segment, e.g. "vertical SaaS company with 120 reps" |

Personas: Head of Sales Development, RevOps lead, VP Sales, CRO. Openers A and C for VP Sales and CRO. Openers B and D for Sales Development and RevOps.
