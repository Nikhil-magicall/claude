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

---

## Additional first-touch variants (E–N)

**E — The bet** · Subject: `a bet on {{company}}`
> Here's a bet. We run 10,000 cold emails to your ICP, on our infrastructure, with our copy, and book the replies into your reps' calendars. If the meetings aren't worth it, you've lost 45 days and nothing else. If they are, your team scales it. Want to see how it's structured?

**F — Borrow our team** · Subject: `borrow our outbound team`
> Instead of hiring two SDRs and waiting six months to find out if cold email works for {{company}}, borrow our team for 45 days. We build the infrastructure, write the emails, send 10–25K, and hand you the meetings. Then you decide whether to run it at scale. Worth a 20-minute call?

**G — Your ICP, our sending** · Subject: `your list, our infrastructure`
> You know exactly who should be buying {{company}}. Reaching them at volume without wrecking your domain is the hard part. Send us the ICP. We handle the domains, mailboxes, copy, and sending, and you get the meetings. If it works, your reps take it over on our infrastructure. Open to scoping it?

**H — The question** · Subject: `quick question`
> How many cold emails did {{company}} send last month? Most companies your size land between 20K and 80K, all from the corporate domain, with a lot going to spam. We'll send your next 25K from infrastructure built for it and show you the difference in meetings. Interested in the numbers?

**I — Skeptic-friendly** · Subject: `probably not for you`
> Cold email at scale is a hard sell to a company that's been around as long as {{company}}. Fair. So we don't sell it. We run it for you first: 10K of your ICP, our infrastructure, meetings into your calendar. You look at the results and decide. If that's a reasonable way to find out, I'll send the details.

**J — The 15× line** · Subject: `15x`
> Same SDR team. Roughly 15× the outbound reach. That's what happens when reps stop sending from one corporate mailbox each. We don't ask you to take our word for it. We run the first 10–25K emails ourselves and give you the meetings. Want to see it on your ICP?

**K — One-sentence offer** · Subject: `{{company}} outbound`
> We run cold email for software companies: infrastructure, copy, sending, reply handling. You get the meetings. If it works, you scale it on our infrastructure. That's the whole pitch. 20 minutes to see if it fits {{company}}?

**L — Board pressure** · Subject: `pipeline next quarter`
> If pipeline is the number you're being asked about, cold email at scale is the fastest channel to move it that doesn't need headcount or a paid budget. We'll prove it: 10–25K emails to your ICP in 45 days, meetings booked for your reps. Then you decide about scaling. Worth a look before the quarter's planned?

**M — New leader** · Subject: `first 90 days`
> Congrats on the {{title}} role. New sales leaders usually want a quick win on pipeline before the big changes. We run cold email for companies like {{company}} and can put meetings on your reps' calendars within 45 days, on our infrastructure, with no headcount request. Happy to walk through how it works.

**N — Competitor** · Subject: `{{competitor}} outbound`
> {{competitor}} is running outbound at a volume your team can't match from the corporate domain. We see it in the inbox data. We can run 10–25K emails to your ICP in 45 days and show you what the same play looks like for {{company}}. You get the meetings either way. Want to compare?

## Alternate follow-ups

- **Day 4, proof:** Recent one: 25K emails, 45 days, 44 meetings, 96% inbox placement. The company's reps now run it on our infrastructure. Happy to show {{company}} the same numbers.
- **Day 4, question:** Simpler question: if we booked 30 qualified meetings for your reps in the next 45 days, who at {{company}} would want to know how?
- **Day 8, low-friction ask:** Not asking for a call yet. Send me one sentence on who {{company}} sells to and I'll reply with how many of them we can reach and roughly what it'd produce.
- **Day 13, redirect:** If outbound sits with someone else at {{company}}, a name is all I need.
- **Day 18, breakup:** Closing this out. The offer stands whenever it's useful: we run your first 10–25K cold emails, you keep the meetings.

## Persona routing for all variants

| Persona | Variants |
|---|---|
| VP Sales / CRO | A, C, E, F, K, L, M |
| Head of Sales Development | B, F, J, N |
| RevOps | B, D, G, J |
| New in role (any) | M |
