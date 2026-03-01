# Scenario 15: Proactive Greeting (Agent-Initiated Message)

## What It Is

A proactive greeting occurs when the agent initiates a message to the user without being prompted — for example, a welcome message that appears automatically when a user opens a chat window, or a pop-up message on a website inviting the user to ask a question. The user does not need to type anything for this greeting to fire. According to Microsoft's official billing FAQ, this greeting counts as a billed Copilot Credit even if the end user never responds.

There is an important nuance: even if no greeting message text is visually sent to the user, but the agent is triggered to be ready for a conversation (i.e., the agent session is initialized), it still consumes Copilot Credits as a Classic Answer.

## How Billing Works

- A proactive greeting is billed as a **Classic Answer = 1 Copilot Credit per greeting**.
- Credits are consumed based on the agent's activity, not the user's response. If 5,000 users open a chat window and the agent greets all of them, the organization pays for 5,000 credits — even if zero users reply.
- For analytics purposes, if the user does not reply, the session is categorized as an unengaged conversation — but the credit is still consumed.

## Credit Consumption

**1 Copilot Credit per proactive greeting**

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Proactive Greeting | Monthly Cost (10,000 greetings) |
|-----------|-------------------------------|---------------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | $0 |
| Unlicensed Internal User | 1 credit | $100 |
| External User (website, WhatsApp, etc.) | 1 credit | $100 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example A — Website Welcome Greeting:** A customer-facing website agent greets every visitor. 5,000 visitors/day, all external, only 30% engage beyond the greeting.

- Greeting credits = 5,000 × 1 = 5,000 credits/day = 150,000 credits/month (just for greetings)
- Of those, 3,500 users leave without responding — **those greetings are still billed**

| Billing Model | Calculation (greetings only) | Monthly Cost | Annual Cost |
|---------------|------------------------------|--------------|-------------|
| Pay-As-You-Go | 150,000 × $0.01 | $1,500 | $18,000 |
| Capacity Packs | 6 packs × $200 | $1,200 | $14,400 |
| 5 Packs + PAYG | $1,000 + (25,000 × $0.01 = $250) | $1,250 | $15,000 |

### Design Tip

This is a significant hidden cost. If 70% of visitors bounce after the greeting, 70% of your greeting credits are wasted. Consider using a user-initiated model (where the user clicks "Chat now" to start) instead of auto-greeting. This eliminates idle greeting costs entirely.

**Example B — Internal Teams Agent Greeting:** An IT helpdesk agent in Teams proactively greets 500 employees/day.

- If all employees have M365 Copilot licenses: $0
- If employees are unlicensed: 500 × 1 × 30 days = 15,000 credits/month = $150 PAYG

**Example C — High-Traffic E-commerce Bot:** An e-commerce website agent greets 50,000 visitors/day (holiday season).

- Greeting credits alone = 50,000 × 30 = 1,500,000 credits/month = **$15,000 PAYG**
- This is $15,000/month just for saying "Hello!" — before any actual conversation occurs

## Pre-Purchase Plan (P3) Comparison

P3 adds value for proactive greetings because website traffic is inherently seasonal and unpredictable — holiday spikes, marketing campaign launches, viral moments. Proactive greetings fire for every visitor regardless of engagement, making credit consumption directly proportional to traffic volume.

**Using the Website Welcome Greeting example (150,000 credits/month steady):**
- Annual credits needed: 150,000 × 12 = 1,800,000 credits/year

| Billing Model | Calculation | Annual Cost | Effective Rate/Credit |
|---------------|-------------|-------------|----------------------|
| Pay-As-You-Go | 1,800,000 × $0.01 | $18,000 | $0.01000 |
| Capacity Packs | 6 packs × $200 × 12 months | $14,400 | $0.00800 |
| P3 Tier 2 | 1,500,000 credits at $14,100 + 300,000 overflow × $0.01 | $17,100 | $0.00950 |
| P3 Tier 3 | 3,000,000 credits at $27,900 (1.2M surplus) | $27,900 | $0.01550 (if only 1.8M used) |

**Verdict:** At steady traffic, Capacity Packs ($14,400) win clearly.

### Seasonal Spike Example

An e-commerce site with proactive greetings during holiday season:

- Nov–Dec: 50,000 visitors/day = 1,500,000 credits/month
- Jan–Mar: 2,000 visitors/day = 60,000 credits/month
- Apr–Oct: 5,000 visitors/day = 150,000 credits/month
- **Annual total: (1.5M × 2) + (60K × 3) + (150K × 7) = 4,230,000 credits**

| Billing Model | Annual Cost | Notes |
|---------------|-------------|-------|
| Capacity Packs | ~$34,200 | 60 packs peak + 3 packs low + 6 packs mid; heavy waste in Jan–Mar |
| P3 Tier 3 | $27,900 + $12,300 overflow = $40,200 | Covers 3M + overflow at PAYG |
| P3 Tier 4 | $138,000 | Massive overkill |
| Optimal: Capacity Packs + PAYG | $14,400 + $27,000 = $41,400 | Buy 6 packs baseline; PAYG handles Nov–Dec spike |

**Best approach:** Capacity Packs with PAYG overflow — buy 6 packs for baseline ($14,400/year) and let PAYG absorb Nov–Dec spikes.

## P3 Value for Proactive Greetings

P3 value here is limited unless the proactive greeting agent shares a P3 credit pool with other agents in the organization. If the company also runs customer support, order tracking, and feedback agents, the combined annual pool makes P3 Tier 3 or 4 more attractive.
