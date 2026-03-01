# Scenario 5: Agent Flow Actions

## What It Is

Agent flows are Power Automate flows embedded within agents — predefined sequences of flow actions that execute repetitive tasks quickly, without requiring agent reasoning at each step. They are billed per batch of 100 flow actions, not per individual step.

## When It's Used

- Multi-step automated workflows triggered by agents (data validation → record creation → email notification)
- Batch operations within an agent conversation (updating multiple records)
- Complex business processes that chain multiple steps (approval workflows, data transformations)
- Any repetitive back-end task the agent needs to execute without AI orchestration at each step

## Credit Consumption

**13 Copilot Credits per 100 flow actions**

Each individual flow action costs approximately 0.13 credits. A flow with 50 actions costs ~6.5 credits. A flow with 200 actions costs 26 credits.

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per 100 Flow Actions | Monthly Cost (50,000 actions) |
|-----------|------------------------------|-------------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | $0 |
| Unlicensed Internal User | 13 credits | $65 |
| External User | 13 credits | $65 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — Operations Agent:** Processes orders. Each order triggers a flow with 200 actions (validate data, check inventory, apply discounts, generate invoice, send notifications, update CRM) + 2 agent actions.

- Flow credits per order = (200 ÷ 100) × 13 = 26 credits
- Agent action credits = 2 × 5 = 10 credits
- **Total per order = 36 credits**
- At 5,000 orders/month: 180,000 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 180,000 × $0.01 | $1,800 | $21,600 |
| Capacity Packs | 8 packs × $200 (200,000 credits) | $1,600 | $19,200 |
| 7 Packs + PAYG | $1,400 + (5,000 × $0.01 = $50) | $1,450 | $17,400 |

## Pre-Purchase Plan (P3) Comparison

P3 adds value for agent flow scenarios because order processing and operational workflows often have seasonal volume fluctuations — e-commerce peaks in November–December, fiscal year-end surges, or campaign-driven spikes. P3's annual credit pool prevents waste during low months.

**Using the Operations Agent example above (180,000 credits/month, 5,000 orders/month):**
- Annual credits needed: 180,000 × 12 = 2,160,000 credits/year

| Billing Model | Calculation | Annual Cost | Effective Rate/Credit |
|---------------|-------------|-------------|----------------------|
| Pay-As-You-Go | 2,160,000 × $0.01 | $21,600 | $0.01000 |
| Capacity Packs | 8 packs × $200 × 12 months | $19,200 | $0.00889 |
| P3 Tier 3 | 3,000,000 credits at $27,900 (840K surplus) | $27,900 | $0.01292 (if only 2.16M used) |
| P3 Tier 2 + PAYG | 1,500,000 at $14,100 + 660,000 overflow × $0.01 | $20,700 | $0.00958 |

**Verdict:** At steady monthly usage, Capacity Packs ($19,200) remain the cheapest option. P3 Tier 2 + PAYG ($20,700) comes close but doesn't beat packs.

### Additional Examples

**Example A — Expense Approval Flow Agent:** Each expense report triggers a 50-action flow (read receipt, validate amounts, check policy, route to manager, update finance system).
- Flow credits = (50 ÷ 100) × 13 = 6.5 credits + 1 generative answer (2) + 1 action (5) = 13.5 credits
- At 1,000 expense reports/month: 13,500 credits = $135 PAYG.

**Example B — Data Sync Agent:** An agent runs a nightly data sync flow with 500 actions per run.
- Flow credits per run = (500 ÷ 100) × 13 = 65 credits
- 30 runs/month = 1,950 credits = $19.50 PAYG.
