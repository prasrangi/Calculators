# Scenario 11: Combined Multi-Feature Interactions

## What It Is

In real-world deployments, a single user interaction often triggers multiple billable features simultaneously. Credits from different feature types accumulate within a single interaction.

## Common Stacking Combinations

| Interaction Scenario | Feature Breakdown | Total Credits | PAYG Cost |
|----------------------|------------------|---------------|-----------|
| Simple FAQ (classic) | 1 classic answer | 1 | $0.01 |
| AI-generated response | 1 generative answer | 2 | $0.02 |
| Generative + Graph grounding | 1 generative + 1 Graph grounding | 12 | $0.12 |
| Generative + 1 API action | 1 generative + 1 action | 7 | $0.07 |
| Generative + Graph + 2 actions | 1 generative + 1 Graph + 2 actions | 22 | $0.22 |
| Full autonomous invoice processing | 1 trigger + 2-page content processing + 1 generative + 3 actions | 58 | $0.58 |
| Deep reasoning + action + Graph | 1 generative + premium reasoning + 1 action + 1 Graph | 27 | $0.27 |
| Autonomous + translation + 3 actions | 1 trigger + 1 standard AI tool + 3 actions | 41.5 | $0.415 |

## Licensed vs. Unlicensed: Complex Interaction

**Example — Full-Stack Employee Agent:** An employee asks a complex question. The agent performs: 1 generative answer + 1 Graph grounding + 2 agent actions + runs a 100-action flow.

| Component | Credits (Unlicensed) | Credits (M365 Copilot Licensed) |
|-----------|----------------------|--------------------------------|
| Generative answer | 2 | 0 |
| Tenant Graph grounding | 10 | 0 |
| Agent action × 2 | 10 | 0 |
| Agent flow (100 actions) | 13 | 0 |
| **Total** | **35** | **0** |

### With Autonomous Trigger

Add an autonomous trigger to the same agent, and the cost changes:

| Component | Credits (Unlicensed) | Credits (M365 Copilot Licensed) |
|-----------|----------------------|--------------------------------|
| Autonomous trigger | 25 | 25 (always billed) |
| Generative answer | 2 | 0 |
| Tenant Graph grounding | 10 | 0 |
| Agent action × 2 | 10 | 0 |
| Agent flow (100 actions) | 13 | 0 |
| **Total** | **60** | **25** |

## Cost Comparison: PAYG vs. Capacity Pack (Complex Agent)

**Example — Enterprise Agent with All Features:** Serves 300 unlicensed users, 5 interactions/day. Each interaction: generative + Graph + 1 action = 17 credits. Plus the agent processes 100 autonomous triggers/day (25 credits each).

- Interactive credits = 300 × 5 × 17 = 25,500/day
- Autonomous credits = 100 × 25 = 2,500/day
- **Daily total = 28,000 credits/day = 840,000/month**

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 840,000 × $0.01 | $8,400 | $100,800 |
| Capacity Packs | 34 packs × $200 (850,000 credits) | $6,800 | $81,600 |
| P3 Tier 5 | 300,000 CCCUs = 30M credits/year at $270,000 | $22,500 effective | $270,000 (covers ~2.97M/month avg) |

## Pre-Purchase Plan (P3) Comparison

P3 is highly valuable for enterprise multi-feature agents because these complex agents combine multiple billable features, serve large user bases, and often run autonomously — creating high-volume, variable workloads that are the ideal P3 use case.

**Using the Enterprise Agent example above (840,000 credits/month):**
- Annual credits needed: 840,000 × 12 = 10,080,000 credits/year

| Billing Model | Calculation | Annual Cost | Effective Rate/Credit |
|---------------|-------------|-------------|----------------------|
| Pay-As-You-Go | 10,080,000 × $0.01 | $100,800 | $0.01000 |
| Capacity Packs | 34 packs × $200 × 12 months | $81,600 | $0.00809 |
| P3 Tier 4 | 15,000,000 credits at $138,000 (4.92M surplus) | $138,000 | $0.01369 (if only 10.08M used) |
| P3 Tier 3 × 4 | 4 × $27,900 = 12M credits | $111,600 | $0.01107 |
| P3 Tier 3 + PAYG | 3M at $27,900 + 7.08M × $0.01 | $98,700 | $0.00979 |

**Verdict:** Capacity Packs ($81,600) win on pure cost. But for enterprise agents, the real P3 value emerges from two factors:

### Factor 1 — Cross-Agent Pooling

If this enterprise also runs 3 other agents (IT helpdesk, HR onboarding, invoice processor) totaling an additional 5M credits/year, the combined 15M credits/year makes P3 Tier 4 at $138,000 very competitive. Capacity Packs for 15M/year = $120,000, so P3 is only $18,000 more — and eliminates monthly expiry risk.

### Factor 2 — MACC Draw-Down

If the organization has a Microsoft Azure Consumption Commitment (MACC), P3 counts toward that commitment. This means the $138,000 isn't "new" spending — it's drawing from already-committed Azure dollars that would be spent anyway, making the effective incremental cost $0.
