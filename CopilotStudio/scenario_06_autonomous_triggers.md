# Scenario 6: Autonomous Triggers

## What It Is

Autonomous triggers fire when an agent activates itself based on an event or schedule, with no user explicitly invoking it. This is the most expensive single-event rate in Copilot Studio and is the only feature that is always billed, even for M365 Copilot licensed users.

## When It's Used

- Monitoring shared mailboxes for incoming emails/invoices
- Processing new orders as they arrive in real-time
- Scheduled checks of dashboards, KPIs, or database thresholds
- Triggering on Dataverse record changes (new lead, case update)
- Any event-driven agent activation without a human initiating it

## Credit Consumption

**25 Copilot Credits per autonomous trigger**

**CRITICAL:** Unlike every other feature, autonomous triggers are never included in the M365 Copilot licence. An organization with 1,000 M365 Copilot users still pays full price for every autonomous trigger.

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Autonomous Trigger | Monthly Cost (1,000 triggers) |
|-----------|-------------------------------|-----------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 25 credits (ALWAYS BILLED) | $250 |
| Unlicensed Internal User | 25 credits | $250 |
| External / Event-driven | 25 credits | $250 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — Autonomous Invoice Processor:** Monitors a shared mailbox and processes 800 invoices/month. Each invoice is ~2 pages.

| Step | Agent Activity | Credits |
|------|----------------|---------|
| Email arrives | Autonomous trigger | 25 |
| Read PDF (2 pages) | Content processing (8 × 2) | 16 |
| Decide what to do | Generative answer | 2 |
| Validate supplier | Dataverse lookup (action) | 5 |
| Store invoice data | Dataverse write (action) | 5 |
| Send confirmation | Outlook connector (action) | 5 |
| **Total per invoice** | | **58** |

- Monthly credits = 800 × 58 = 46,400 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 46,400 × $0.01 | $464 | $5,568 |
| Capacity Packs | 2 packs × $200 (50,000 credits, 3,600 buffer) | $400 | $4,800 |
| P3 Tier 1 | 3,000 CCCUs = 300,000 credits annually at $2,850 | $237.50 effective | $2,850 (+ PAYG for remainder) |

## Design Tip

Consider batching — instead of triggering per event, trigger on a schedule to process all accumulated events at once. A mailbox with 500 daily emails checked hourly (24 triggers/day = 600 credits) costs far less than 500 individual triggers (12,500 credits/day).

## Pre-Purchase Plan (P3) Comparison

P3 is most valuable for autonomous trigger scenarios because event-driven workloads are inherently unpredictable. Order volumes spike unexpectedly, email floods happen during campaigns, and incident monitors trigger more during outages. The annual credit pool of P3 absorbs these spikes without requiring over-provisioning of monthly capacity packs.

### Additional Examples

**Example A — Order Monitoring Agent:** Triggers on every new order.
- 1,000 orders/day × 25 credits = 25,000 credits/day = 750,000/month
- PAYG: $7,500/month. Capacity packs (30 packs): $6,000/month. **Savings: $1,500/month.**

**Example B — Shared Mailbox Monitor:** Triggers on every incoming email to a shared mailbox.
- 500 emails/day × 25 credits = 12,500/day = 375,000/month
- PAYG: $3,750/month. Capacity packs (15 packs): $3,000/month. **Savings: $750/month.**

**Example C — Scheduled Dashboard Check:** Agent triggers every hour to check KPIs.
- 24 triggers/day × 25 credits = 600/day = 18,000/month
- PAYG: $180/month. One capacity pack ($200): **PAYG is cheaper here.**

## Where P3 Truly Shines

When the organization runs multiple autonomous agents across departments (order monitor + email processor + incident detector + scheduled reports), the combined annual credit pool can be shared. If total cross-agent annual usage reaches 15M+ credits, P3 Tier 4 at $138,000 ($0.0092/credit) starts competing with Capacity Packs that would cost $120,000 for the same volume — and P3 eliminates the monthly expiry risk.
