# Scenario 17: Copilot Studio for Teams vs. Standalone Copilot Studio Deployed to Teams

## What It Is

Microsoft offers two distinct ways to build and deploy agents to Microsoft Teams, and they have fundamentally different billing implications. Confusing these two paths is one of the most common licensing mistakes organizations make.

### Path 1 — Copilot Studio for Teams
A limited, Teams-native agent-building experience included with certain Microsoft 365 and Office 365 licenses. Agents are created inside the Teams environment.

### Path 2 — Standalone Copilot Studio deployed to Teams
Full-featured agents built in the standalone Copilot Studio (at copilotstudio.microsoft.com) that are then published to the Teams channel as one of their deployment targets.

## How Billing Works

According to Microsoft's official billing FAQ:

- **Copilot Studio for Teams agents (built inside Teams):** Do NOT consume Copilot Credits, regardless of who uses them. This is because the capability is included with eligible M365/O365 licenses that include Teams.

- **Standalone Copilot Studio agents deployed to Teams:** DO consume Copilot Credits. However, if the end user has a Microsoft 365 Copilot license and the agent is operating in an authenticated B2E context, their usage is not billed.

## Licensed vs. Unlicensed User Comparison

| Deployment Type | M365 Copilot Licensed User | Unlicensed User (with M365/O365) | External Guest User |
|-----------------|---------------------------|----------------------------------|----------------------|
| Copilot Studio for Teams (built in Teams) | 0 credits | 0 credits | 0 credits |
| Standalone Copilot Studio → deployed to Teams | 0 credits (B2E included) | Credits consumed (standard rates) | Credits consumed (standard rates) |

## Cost Comparison: PAYG vs. Capacity Pack

**Example A — Small Team FAQ Bot (Copilot Studio for Teams):**
A team of 200 employees uses an agent built inside Teams with standard connectors. 500 conversations/month.

| Billing Model | Calculation | Monthly Cost |
|---------------|-------------|--------------|
| Any model | 0 credits consumed | $0 — always free |

**Example B — Enterprise HR Agent (Standalone, deployed to Teams):**
An HR agent built in standalone Copilot Studio is published to Teams. 1,000 employees use it monthly. 300 have M365 Copilot licenses, 700 do not. Average interaction: 1 generative + 1 action = 7 credits.

- **Licensed users (300):** $0
- **Unlicensed users (700 × 3 interactions/month × 7 credits):** 14,700 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 14,700 × $0.01 | $147 | $1,764 |
| 1 Capacity Pack | $200 (10,300 credits buffer) | $200 | $2,400 |

PAYG is cheaper at this volume.

**Example C — Mixed Deployment:**
An organization has both:
- 5 simple FAQ bots built in **Copilot Studio for Teams** → $0/month
- 2 advanced agents (with connectors, Graph grounding, flows) built in **standalone Copilot Studio**, deployed to Teams → credits consumed for unlicensed users

## Key Differences Between the Two Paths

| Feature | Copilot Studio for Teams | Standalone Copilot Studio → Teams |
|---------|--------------------------|----------------------------------|
| Built where | Inside Microsoft Teams | copilotstudio.microsoft.com |
| Requires Copilot Studio license | No (included with M365/O365) | Yes (capacity pack, PAYG, or P3) |
| Consumes Copilot Credits | Never | Yes (except for M365 Copilot licensed B2E users) |
| Premium connectors | No | Yes |
| Custom connectors | No | Yes |
| Agent flows (Power Automate) | No | Yes |
| Generative orchestration | Limited | Full |
| Tenant Graph grounding | No | Yes |
| Autonomous triggers | No | Yes |
| External channel publishing | No | Yes |
| Dataverse for Copilot Studio | Limited (Dataverse for Teams) | Full Dataverse |

## When to Choose Which

### Choose Copilot Studio for Teams when:
- Your agents are simple FAQ bots or information lookup agents
- The team is small and deployments are contained within Teams
- Cost must be zero
- You want minimal setup and no licensing overhead

### Choose Standalone Copilot Studio → Teams when:
- You need premium connectors or custom integrations
- Graph grounding, autonomous triggers, or agent flows are required
- You're publishing to external channels (website, WhatsApp, etc.) in addition to Teams
- Complex orchestration or multi-step workflows are needed
- You need enterprise-grade Dataverse access

## Cost Implication Example

An organization wants to deploy 3 similar HR support agents to their 5,000-person tenant:

### Using Copilot Studio for Teams (Free path):
- 3 agents × 500 interactions/month × 7 credits each = 10,500 credits/month (but actually $0 — included in M365 licenses)
- **Annual cost: $0**

### Using Standalone Copilot Studio deployed to Teams (Billed path):
- Same 3 agents × 500 interactions/month × 7 credits = 10,500 credits/month
- Assuming 20% of users are M365 Copilot licensed (free), 80% unlicensed (billed)
- Billable usage = 10,500 × 80% = 8,400 credits/month
- **Annual cost: 8,400 × $0.01 × 12 = $1,008**

**The choice matters: $0 vs. $1,008 annually — a 100% cost difference for the same functionality.**

## Licensing Path Decision Tree

1. **Is this a simple FAQ bot with basic knowledge sources?**
   - Yes → Use Copilot Studio for Teams (free)
   - No → Proceed to step 2

2. **Do you need autonomous triggers, agent flows, or premium connectors?**
   - Yes → Must use Standalone (billed)
   - No → Proceed to step 3

3. **Do you need to publish to external channels (website, WhatsApp)?**
   - Yes → Must use Standalone (billed)
   - No → Proceed to step 4

4. **Do you need tenant graph grounding or advanced orchestration?**
   - Yes → Use Standalone (billed for unlicensed users)
   - No → Use Copilot Studio for Teams (free)

## Important Note

If you're already invested in standalone Copilot Studio development and have complex agents with flows and connectors, the question becomes cost optimization rather than choice. At that point, focus on maximizing M365 Copilot licensing adoption — every licensed user removes the per-interaction billing burden.
