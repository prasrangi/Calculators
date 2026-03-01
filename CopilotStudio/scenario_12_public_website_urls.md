# Scenario 12: Agent Grounded on Public Website URLs

## What It Is

This scenario covers an agent built in Copilot Studio (full version) that is grounded exclusively on publicly available website URLs — not on SharePoint sites, OneDrive files, or any internal organizational data. The agent uses generative answers powered by AI models, but retrieves knowledge only from public internet sources (e.g., company marketing website, public documentation portal, government resources). No tenant graph grounding is involved.

This is a common deployment for customer-facing FAQ agents, product information bots, or agents that answer questions about publicly available policies.

## How Billing Works

- The agent returns generative answers grounded on public URL content. Each generative answer costs 2 Copilot Credits.
- Since no SharePoint, OneDrive, or Microsoft Graph data is accessed, tenant graph grounding (10 credits) does NOT apply.
- Even though the knowledge source is "free" public data, the organization still pays for the generative answer credits for every unlicensed user interaction. The billing is for the AI processing and response generation, not for the data source.
- Classic answers (predefined, static) still cost 1 credit per response.

## Credit Consumption

**2 Copilot Credits per generative answer** (no graph grounding surcharge)

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Generative Answer | Tenant Graph Grounding | Total Credits Per Response | Monthly Cost (3,000 responses) |
|-----------|------------------------------|------------------------|---------------------------|--------------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | N/A — not used | 0 | $0 |
| Unlicensed Internal User | 2 credits | N/A — not used | 2 | $60 |
| External User (public website) | 2 credits | N/A — not used | 2 | $60 |

## Key Insight

Even though the data is publicly available, every generative response to an unlicensed user costs the organization 2 credits ($0.02). The credit charge is for the AI processing — not for the data itself.

## Cost Comparison: PAYG vs. Capacity Pack

**Example A — Public FAQ Agent on Company Website:** A company deploys an agent on their marketing website grounded on 5 public URLs (product pages, pricing page, return policy). 2,000 visitors/month, each asking 3 questions (all generative answers).

- Credits per month = 2,000 × 3 × 2 = 12,000 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 12,000 × $0.01 | $120 | $1,440 |
| 1 Capacity Pack | $200 (13,000 credits unused) | $200 | $2,400 |

**Verdict:** At 12,000 credits/month, PAYG ($120) is significantly cheaper than a capacity pack ($200).

**Example B — Government Services Information Agent:** An agent grounded on 10 public government URLs serves 500 queries/day (all generative).

- Credits per day = 500 × 2 = 1,000 credits/day = 30,000 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 30,000 × $0.01 | $300 | $3,600 |
| 2 Capacity Packs | 2 × $200 (20,000 credits unused) | $400 | $4,800 |
| 1 Pack + PAYG | $200 + (5,000 × $0.01 = $50) | $250 | $3,000 |

**Example C — Mixed Classic + Generative on Public Data:** An agent returns 2 classic answers (greetings, menu) + 2 generative answers from public URLs per session. 1,000 sessions/month.

- Credits per session = (2 × 1) + (2 × 2) = 6 credits
- Monthly total = 1,000 × 6 = 6,000 credits = $60 PAYG

## Important Distinctions

- **Turning OFF tenant graph grounding is critical** to avoid the 10-credit surcharge. If graph grounding is accidentally left ON, each response costs 12 credits (2 + 10) instead of 2.

- **Agent Builder exception:** Agents built in Agent Builder (Copilot Studio Lite) in Microsoft 365 that do NOT use tenant graph grounding are not charged for generative answers at all. This exception applies only to the lite Agent Builder, not to full Copilot Studio agents.

- **Public URL grounding** uses Bing-indexed web content or specific URLs configured in the agent's knowledge sources. No authentication is required for users to access this data.
