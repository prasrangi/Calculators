# Scenario 9: AI Tools — Premium (Deep Reasoning)

## What It Is

Premium AI tools include advanced LLM prompts, deep reasoning, and Code Interpreter capabilities. This is the most expensive AI tool tier and applies whenever an agent uses a reasoning-capable language model.

## Reasoning Model Double Billing

When an agent uses a reasoning model, Copilot Studio bills using two meters simultaneously:

1. **Feature rate** — the core action (e.g., generative answer at 2 credits, agent action at 5 credits)
2. **Text and generative AI tools (premium)** — the reasoning model surcharge at 100 credits per 10 responses (10 credits per response)

**Total cost = Feature rate + Premium AI tool rate**

## Credit Consumption

**100 Copilot Credits per 10 responses** (10 credits per response)

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Response (Generative + Premium) | Monthly Cost (5,000 responses) |
|-----------|---------------------------------------------|-----------------------------:|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | $0 |
| Unlicensed User | 12 credits (2 gen + 10 premium) | $600 |
| External User | 12 credits (2 gen + 10 premium) | $600 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — Legal Research Agent:** Uses deep reasoning to analyze complex legal queries. 100 queries/day, each producing 3 generative answers with reasoning.

- Per query = 3 × (2 + 10) = 36 credits
- Daily = 3,600 credits/day = 108,000 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 108,000 × $0.01 | $1,080 | $12,960 |
| Capacity Packs | 5 packs × $200 (125,000 credits) | $1,000 | $12,000 |
| 4 Packs + PAYG | $800 + (8,000 × $0.01 = $80) | $880 | $10,560 |

### Additional Examples

**Example A — Code Interpreter Agent:** Employees ask analytical questions; the agent generates and runs Python code. Each response = 10 premium credits + 2 generative credits = 12 credits. 
- At 50 queries/day: 600/day = 18,000/month = $180 PAYG.

**Example B — Deep Reasoning + Agent Action:** An agent uses reasoning to analyze a complex task, then executes an API call.
- Per interaction = 5 (action) + 10 (premium reasoning) = 15 credits
- At 200 interactions/day: 3,000/day = 90,000/month = $900 PAYG vs. 4 packs at $800.
