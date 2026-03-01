# Copilot Studio Credits Guide — Overview & Master Billing Reference

## Overview

Microsoft Copilot Studio uses Copilot Credits as its universal billing currency. Every time an agent responds to a user, executes an action, triggers autonomously, or invokes an AI tool, a specific number of credits is consumed. Each Copilot Credit costs **$0.01 on Pay-As-You-Go (PAYG)**, or effectively **$0.008 with capacity packs ($200/month for 25,000 credits)**. The number of credits consumed per interaction depends on the complexity and type of action the agent performs.

**Credits are pooled at the tenant level and enforced monthly** — unused credits from capacity packs do not roll over to the next month. Capacity enforcement is triggered when a tenant reaches 125% of their prepaid capacity. At that point, custom agents are disabled until capacity is increased or reset.

## Key Licensing Rule for M365 Copilot Users

**Employee-facing (B2E) usage of Copilot Studio agents is included at no additional credit cost** when:

1. The user holds a **Microsoft 365 Copilot USL** ($30/user/month)
2. The agent operates using the **authenticated M365 Copilot user's identity**
3. The interaction occurs **within M365 surfaces** (Teams, SharePoint, Copilot Chat)

**IMPORTANT EXCEPTIONS:**
- **Autonomous triggers are always billed at 25 credits** regardless of licensing
- **Any usage by unlicensed users always consumes credits**
- **External channel deployments always consume credits**

## Master Billing Rate Table

| Agent Feature | Credits Consumed | Cost at PAYG ($0.01/credit) | M365 Copilot Licensed User |
|---------------|------------------|----------------------------|---------------------------|
| Classic answer | 1 Copilot Credit | $0.01 | No charge |
| Generative answer | 2 Copilot Credits | $0.02 | No charge |
| Agent action | 5 Copilot Credits | $0.05 | No charge |
| Tenant Graph grounding | 10 Copilot Credits | $0.10 | No charge |
| Agent flow actions (per 100 actions) | 13 Copilot Credits | $0.13 | No charge |
| Autonomous trigger | 25 Copilot Credits | $0.25 | **Always billed** |
| AI Tools — Basic (per 10 responses) | 1 Copilot Credit | $0.01 | No charge |
| AI Tools — Standard (per 10 responses) | 15 Copilot Credits | $0.15 | No charge |
| AI Tools — Premium (per 10 responses) | 100 Copilot Credits | $1.00 | No charge |
| Content processing tools (per page) | 8 Copilot Credits | $0.08 | No charge |

### Important Notes on Billing Rates

- **All rates apply regardless of the language model used** by Copilot Studio
- **Bring-your-own-model (BYOM) configurations** incur separate Azure charges on top of these rates
- **Agents created in Agent Builder** in Microsoft 365 that do not use tenant graph grounding are **not charged for generative answers** (exception to the table above)

## Billing Model Options

### 1. Pay-As-You-Go (PAYG)
- **Cost:** $0.01 per Copilot Credit
- **Commitment:** None — pay only for what you use
- **Best for:** Variable workloads, testing, or usage below 20,000 credits/month
- **No rollover:** Credits expire at the end of the billing period

### 2. Capacity Packs
- **Cost:** $200/month per pack
- **Credits included:** 25,000 credits/month per pack
- **Effective rate:** $0.008 per credit (20% discount vs. PAYG)
- **Best for:** Steady monthly usage above 20,000 credits
- **No rollover:** Unused credits expire at end of month
- **Recommendation:** Pair with PAYG for overage handling

### 3. Pre-Purchase Plan (P3)
- **Cost:** $2,850–$2.4M annually (depending on tier)
- **Credits:** 300K–300M per year
- **Effective rate:** $0.008–$0.0095 per credit (up to 20% discount)
- **Term:** 1 year upfront commitment
- **Best for:** High-volume (100K+ credits/month), seasonal workloads, or cross-tenant pooling
- **Advantage:** Annual pooling eliminates monthly expiry waste; counts toward MACC
- **No rollover:** Annual credits don't roll to next year

### 4. Agent P3 Plan
- **Cost:** $19,000–$425K annually
- **Coverage:** Both Copilot Studio AND Microsoft Foundry
- **Best for:** Organizations using multiple agentic services wanting unified billing

## When to Use Which Billing Model

| Scenario | Recommended Model | Reasoning |
|----------|-------------------|-----------|
| Testing, pilot, or unpredictable usage | PAYG | Zero commitment, pay per credit |
| Steady 20K–100K credits/month | Capacity Packs | 20% savings vs. PAYG with predictable costs |
| Steady 100K+ credits/month | Capacity Packs + PAYG | Packs for baseline, PAYG for overflow |
| Seasonal or variable workloads (50%+ swing month-to-month) | P3 | Annual pooling prevents monthly waste |
| Multiple agents across departments | P3 | Unified credit pool reduces complexity |
| Existing MACC agreement | P3 | Draws from committed Azure spending |
| Multi-service usage (Copilot Studio + Foundry) | Agent P3 | Single pool for both services |

## Quick Math: PAYG vs. Capacity Packs vs. P3

**Example: 100,000 credits/month steady usage**

| Model | Monthly Cost | Annual Cost | Effective Rate | Notes |
|-------|--------------|-------------|----------------|-------|
| PAYG | $1,000 | $12,000 | $0.01000 | Baseline |
| 4 Capacity Packs | $800 | $9,600 | $0.00800 | **20% savings** |
| P3 Tier 3 (3M/year) | ~$2,325 | $27,900 | $0.00930 | Overkill, but absorbs spikes |
| P3 Tier 2 (1.5M/year) + PAYG | ~$1,510 | $18,120 | $0.00909 | Hybrid approach |

**Break-even point:** Capacity Packs become cheaper than PAYG at approximately **20,000 credits/month** of steady usage.

## How Credits Stack in Real-World Scenarios

In practice, a single interaction often triggers multiple features, and credits accumulate. For example:

- **Simple FAQ:** 1 classic answer = **1 credit** ($0.01)
- **Generative answer + Graph grounding + 1 API call:** 2 + 10 + 5 = **17 credits** ($0.17)
- **Autonomous invoice processing (trigger + content processing + generative + 3 actions):** 25 + 16 + 2 + 15 = **58 credits** ($0.58)

See **Scenario 11: Combined Multi-Feature Interactions** for detailed stacking examples.

## Tenant-Level Pooling & Enforcement

- **Credits are pooled at the tenant level**, not per agent or per department
- **Monthly enforcement:** Unused capacity pack credits do NOT roll over to the next month
- **Overage enforcement:** When a tenant reaches **125% of prepaid capacity**, custom agents are disabled until:
  - Additional capacity is purchased, OR
  - The billing period resets
- **PAYG always available:** Even with capacity packs, PAYG can be enabled as an overflow mechanism

## External Channel Billing

When agents are deployed to external channels (public website, WhatsApp, Facebook, etc.):
- **All users are always billed** — there is no M365 Copilot licensing exemption
- **Every interaction costs the standard rate** based on the features used
- **Proactive greetings still count** — even if a user never responds

## How to Navigate This Guide

This guide contains **17 detailed scenarios**, each explaining:

1. **What It Is** — Clear description of the feature
2. **When It's Used** — Real-world use cases
3. **Credit Consumption** — Exact billing rate
4. **Licensing Comparison** — Cost for M365 licensed vs. unlicensed users
5. **Cost Scenarios** — PAYG vs. Capacity Packs vs. P3 examples
6. **Design Tips** — Optimization strategies

**For your specific use case:**
- Find the scenario that matches your agent architecture
- Review the cost comparison tables
- Use the examples to calculate your estimated monthly costs
- Choose the billing model that optimizes for your usage pattern

## Key Takeaways

✅ **Classic answers are cheapest** — 1 credit each  
✅ **Licensed M365 Copilot users get most features free** — except autonomous triggers  
✅ **Capacity Packs beat PAYG** at 20K+ credits/month steady usage  
✅ **P3 shines for seasonal or multi-agent workloads** — annual pooling prevents waste  
✅ **Autonomous triggers are always billed** — no exceptions  
✅ **External channels always consume credits** — no licensing exemptions  
✅ **Test chat is free** — flows and AI tools in test chat are billed  

---

**Next Steps:** Select the scenario(s) that match your deployment model and review the detailed cost breakdowns.
