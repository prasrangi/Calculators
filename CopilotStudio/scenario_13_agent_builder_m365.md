# Scenario 13: Agent Builder (Copilot Studio Lite) in M365 Copilot Chat

## What It Is

This scenario covers agents created using Agent Builder (also known as Copilot Studio Lite) — the lightweight, in-context agent creation experience available directly inside Microsoft 365 Copilot Chat. Agent Builder allows business users to quickly build simple agents without leaving their daily workflow. These "lite" agents can use SharePoint sites, OneDrive files, or directly uploaded files as knowledge sources.

This is distinct from full Copilot Studio agents. Agent Builder agents are hosted in the M365 service environment (not Power Platform environments) and have different billing rules.

## How Billing Works — The Critical Footnote

Microsoft's billing rates page contains a critical footnote for generative answers:

> "Agents incur charges for generative answer responses unless the agent is created in Agent Builder in Microsoft 365 and the response doesn't leverage tenant graph grounding."

This creates three distinct billing outcomes for Agent Builder lite agents:

### Outcome 1 — Agent Builder + NO Tenant Graph Grounding (uploaded files only):
- Generative answers are **FREE** (0 credits) — even for unlicensed users
- This applies when the agent uses only directly uploaded files as knowledge and graph grounding is OFF

### Outcome 2 — Agent Builder + SharePoint/OneDrive as Knowledge Source (Tenant Graph Grounding ON):
- Tenant graph grounding is triggered: 10 credits per response
- Plus generative answer: 2 credits (the "free" exception no longer applies because graph grounding is used)
- **Total: 12 credits per response** for unlicensed users

### Outcome 3 — Agent Builder used by M365 Copilot Licensed User:
- **ALL features are included at no charge** — generative answers, tenant graph grounding, everything

## Licensed vs. Unlicensed User Comparison

| Agent Builder Configuration | M365 Copilot Licensed User | Unlicensed User |
|---------------------------|---------------------------|-----------------|
| Uploaded files only, Graph grounding OFF | 0 credits (included) | 0 credits (free per footnote) |
| SharePoint/OneDrive knowledge, Graph grounding ON | 0 credits (included) | 12 credits (2 gen + 10 graph) |
| SharePoint knowledge, Graph grounding OFF (manual config) | 0 credits (included) | 0 credits (free per footnote — no graph grounding) |
| Public URL only, Graph grounding OFF | 0 credits (included) | 0 credits (free per footnote) |

## Critical Warning

Agents built in SharePoint or Copilot Chat that use SharePoint as a knowledge source often have tenant graph grounding enabled by default. This means unlicensed users will unknowingly incur 12 credits per response unless an admin explicitly turns graph grounding OFF.

## Cost Comparison: PAYG vs. Capacity Pack

**Example A — Agent Builder with Uploaded Files Only (No Graph Grounding):**
A team creates a lite agent in Copilot Chat with 5 uploaded PDF manuals. 200 users/month, 10 queries each. Graph grounding is OFF.

- Credits per response = 0 (free per Agent Builder exception)
- **Total monthly cost = $0** for both licensed and unlicensed users

| Billing Model | Calculation | Monthly Cost |
|---------------|-------------|--------------|
| Pay-As-You-Go | 0 credits consumed | $0 |
| Capacity Pack | Not needed | $0 |

**This is the most cost-effective way to deploy a simple knowledge agent for unlicensed users** — use Agent Builder with uploaded files and ensure graph grounding is disabled.

**Example B — Agent Builder with SharePoint Sites (Graph Grounding ON — Default):**
An HR team creates a lite agent in Copilot Chat grounded on 3 SharePoint sites (policies, benefits, onboarding). 500 unlicensed users/month, 5 queries each. Graph grounding is ON (default).

- Credits per response = 12 (2 generative + 10 graph grounding)
- Monthly credits = 500 × 5 × 12 = 30,000 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 30,000 × $0.01 | $300 | $3,600 |
| 2 Capacity Packs | 2 × $200 (20,000 credits buffer) | $400 | $4,800 |
| 1 Pack + PAYG | $200 + (5,000 × $0.01 = $50) | $250 | $3,000 |

If the same 500 users had M365 Copilot licenses ($30/user/month = $15,000/month), the agent usage would be $0 additional. The break-even point: if agent usage per unlicensed user exceeds ~$30/month in credits, it becomes cheaper to buy M365 Copilot licenses.

**Example C — Agent Builder with OneDrive Files + SharePoint (Graph Grounding ON):**
A project team creates an agent grounded on 2 OneDrive folders and 1 SharePoint site. 100 unlicensed users, 8 queries/month each.

- Credits per response = 12
- Monthly credits = 100 × 8 × 12 = 9,600 credits/month

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 9,600 × $0.01 | $96 | $1,152 |
| 1 Capacity Pack | $200 (15,400 credits unused) | $200 | $2,400 |

**Verdict:** PAYG is clearly cheaper for lower usage volumes. Capacity packs only make sense above ~20,000 credits/month.

## Agent Builder vs. Full Copilot Studio — Billing Comparison

| Feature | Agent Builder (Lite) | Full Copilot Studio |
|---------|----------------------|------------------------|
| Generative answer (no graph grounding) | FREE for all users | 2 credits (unlicensed) |
| Generative answer + Graph grounding | 12 credits (unlicensed) | 12 credits (unlicensed) |
| Can disable graph grounding? | Yes (but ON by default for SharePoint) | Yes (configurable per agent) |
| External channels (website, WhatsApp) | Not available | Available (always billed) |
| Autonomous triggers | Not available | 25 credits (always billed) |
| Agent actions (API calls) | Limited | Full (5 credits each) |
| Hosted in | M365 service environment | Power Platform environment |

## Important Considerations for Unlicensed Users

- **Admins must enable PAYG billing** for unlicensed users to access Agent Builder agents that use tenant data. This is done in the Microsoft 365 admin center or Power Platform admin center.

- **Agents utilizing metered consumption are OFF by default** for unlicensed users in Copilot Chat. An admin must explicitly enable this.

- **Unlicensed users accessing SharePoint-grounded agents** will have their access governed by their existing Microsoft Entra ID permissions — if they lack permission to the SharePoint site, the agent cannot retrieve that data for them.

- **The "Enhanced search results" feature** (semantic search for SharePoint/connectors) requires a M365 Copilot license in the tenant and "Authenticate with Microsoft" enabled on the agent.
