# Scenario 4: Tenant Graph Grounding

## What It Is

Tenant Graph grounding provides higher-quality responses by querying the organization's Microsoft Graph — including emails, files, meetings, chats, and external data synced through Graph connectors. It uses RAG over tenant-wide Graph data to deliver contextually relevant answers. This capability is optional and can be toggled on/off per agent.

## When It's Used

- Agents answering questions about organizational data (sales reports, meeting notes, internal documents)
- Agents embedded in Microsoft 365 Copilot Chat that need real-time organizational context
- Employee-facing agents that need to access a user's calendar, recent emails, or shared files
- Any scenario where the agent must search across the full Microsoft 365 data estate

## Credit Consumption

**10 Copilot Credits per grounded response** (added on top of the base response cost)

A single Graph-grounded generative answer costs 12 credits total (2 for generative + 10 for Graph grounding).

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Graph-Grounded Response | Monthly Cost (3,000 responses) |
|-----------|-------------------------------------|--------------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | $0 |
| Unlicensed Internal User | 12 credits (2 gen + 10 graph) | $360 |
| External User | N/A (Graph grounding is for internal organizational data) | N/A |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — Sales Performance Agent:** A tenant-graph-grounded agent in M365 Copilot Chat answers employee questions about sales data. Average run: 4 generative answers + 4 Graph grounding responses. Serves 50 licensed + 100 unlicensed users/day.

- Credits per unlicensed user interaction = (4 × 2) + (4 × 10) = 48 credits
- Daily total (unlicensed only) = 48 × 100 = 4,800 credits/day = 144,000 credits/month
- Licensed users: $0

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 144,000 × $0.01 | $1,440 | $17,280 |
| Capacity Packs | 6 packs × $200 (150,000 credits) | $1,200 | $14,400 |
| 5 Packs + PAYG | $1,000 + (19,000 × $0.01 = $190) | $1,190 | $14,280 |

## Pre-Purchase Plan (P3) Comparison

P3 adds value for this scenario because Graph-grounded agents often follow seasonal usage patterns — sales cycles, quarterly reporting, annual planning — where monthly credit consumption varies significantly. P3's annual credit pool absorbs these fluctuations without wasting monthly capacity pack credits during low-usage months.

**Using the Sales Performance Agent example above (144,000 credits/month for unlicensed users):**
- Annual credits needed: 144,000 × 12 = 1,728,000 credits/year

| Billing Model | Calculation | Annual Cost | Effective Rate/Credit |
|---------------|-------------|-------------|----------------------|
| Pay-As-You-Go | 1,728,000 × $0.01 | $17,280 | $0.01000 |
| Capacity Packs | 6 packs × $200 × 12 months | $14,400 | $0.00833 |
| P3 Tier 2 | 1,500,000 credits at $14,100 + 228,000 overflow at PAYG ($2,280) | $16,380 | $0.00948 |
| P3 Tier 3 | 3,000,000 credits at $27,900 (1.27M surplus) | $27,900 | $0.01614 (if only 1.73M used) |

**Verdict:** At steady monthly usage, Capacity Packs win on per-credit cost. However, if this agent experiences seasonal spikes (e.g., 300,000 credits in Q4 and 50,000 in Q1), P3 Tier 2 + PAYG overflow becomes more cost-effective because Capacity Packs would waste credits in low months.

### Additional Examples

**Example A — Meeting Prep Agent:** Employees ask "What did we discuss about Project X last week?" Agent retrieves emails + meeting transcripts via Graph grounding + returns a generative summary.
- Per query = 2 (generative) + 10 (graph) = 12 credits
- 200 employees × 2 queries/day = 4,800 credits/day = 144,000/month
- If all employees have M365 Copilot: $0. If none licensed: $1,440 PAYG.

**Example B — Executive Dashboard Agent:** 20 executives ask the agent daily for performance summaries. Agent makes 3 generative answers + 3 Graph grounding calls per session.
- Per session = (3 × 2) + (3 × 10) = 36 credits
- Daily = 36 × 20 = 720 credits/day = 21,600/month
- PAYG: $216/month. One pack ($200): slightly cheaper.
