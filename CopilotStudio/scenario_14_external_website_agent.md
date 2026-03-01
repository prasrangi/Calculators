# Scenario 14: External Website Agent

## What It Is

When an agent is deployed on external channels (public website, Facebook Messenger, WhatsApp, custom mobile apps), all users are external with no M365 licences. Every interaction is always billed.

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Interaction (2-turn FAQ) | Monthly Cost (5,000 conversations) |
|-----------|--------------------------------------|--------|
| M365 Copilot Licensed User | N/A (external channel = always billed) | Always billed |
| External User (FAQ, 2 turns) | 4 credits (2 × generative) | $200 |
| External User (Order lookup, 2 turns) | 9 credits (gen + action + gen) | $450 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — Customer Website Agent:** 5,000 conversations/month (2 turns each). 70% FAQ (4 credits), 30% order lookup (9 credits).

- FAQ: 3,500 × 4 = 14,000 credits
- Order lookup: 1,500 × 9 = 13,500 credits
- **Total = 27,500 credits/month**

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 27,500 × $0.01 | $275 | $3,300 |
| 2 Capacity Packs | 2 × $200 (22,500 credits wasted) | $400 | $4,800 |
| 1 Pack + PAYG | $200 + (2,500 × $0.01 = $25) | $225 | $2,700 |

The hybrid approach (1 capacity pack + PAYG for overage) saves $600/year compared to pure PAYG.
