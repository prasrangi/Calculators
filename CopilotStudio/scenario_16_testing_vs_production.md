# Scenario 16: Testing vs. Production

## What It Is

This scenario addresses a common question among agent builders: are credits consumed when testing an agent in Copilot Studio's built-in test chat panel before publishing? The answer is nuanced — some activities are free during testing, while others always incur charges.

## How Billing Works — The Three Rules

### Rule 1: Embedded Test Chat Messages Are NOT Billed

Direct messages exchanged in Copilot Studio's embedded test chat panel (the "Test your agent" pane) do not count toward billed sessions or Copilot Credit consumption. This means classic answers, generative answers, and topic-level orchestration during test chat are free.

### Rule 2: Agent Flows and AI Tools in Test ARE Billed

When an agent flow (Power Automate flow) is triggered from within the test chat — whether from a topic or via generative orchestration — the agent flow actions are consumed and billed. The specific mechanics are:

- **Flow triggered from a topic in test:** Only the agent flow actions are billed (the classic answer trigger is not counted)
- **Flow triggered via generative orchestration in test:** Only the agent flow actions are billed (the autonomous action trigger is not counted)
- **AI tools (prompts, models) invoked during test:** Always billed at the standard rate table, regardless of whether the agent is published or not

### Rule 3: Preview Features in Test ARE Billed

Copilot Studio features that are in preview still charge at the rate described in the billing rate table and count against purchased capacity, even during testing.

## What's Free vs. What's Billed During Testing

| Activity During Testing | Billed? | Credits |
|------------------------|---------|---------|
| Classic answer in test chat | Not billed | 0 |
| Generative answer in test chat | Not billed | 0 |
| Agent action (connector call) in test chat | Not billed | 0 |
| Tenant Graph grounding in test chat | Not billed | 0 |
| Agent flow actions triggered from test chat | Billed | 13 per 100 actions |
| AI Tools (Basic/Standard/Premium) in test | Billed | Standard rates |
| Content processing (document OCR) in test | Billed | 8 per page |
| Preview features in test | Billed | Standard rates |

## Cost Comparison: PAYG vs. Capacity Pack

**Example A — Developer Testing a Simple FAQ Agent:**
A developer tests 200 conversations in the test chat with classic and generative answers. No flows or AI tools.

| Billing Model | Calculation | Cost |
|---------------|-------------|------|
| Pay-As-You-Go | 0 credits (test chat exempt) | $0 |
| Capacity Pack | 0 credits consumed | $0 |

**Example B — Developer Testing an Agent with Flows:**
A developer tests an agent that triggers a 50-action flow for each of 100 test conversations.

- Flow credits per test = (50 ÷ 100) × 13 = 6.5 credits
- **Total = 100 × 6.5 = 650 credits**

| Billing Model | Calculation | Cost |
|---------------|-------------|------|
| Pay-As-You-Go | 650 × $0.01 | $6.50 |
| Capacity Pack | Consumed from existing pack | $0 (from pack allowance) |

**Example C — Testing a Document Processing Agent:**
A developer tests OCR on 50 documents averaging 3 pages each during development.

- Credits = 50 × 3 × 8 = 1,200 credits = **$12 PAYG**

## Important Considerations

- **Non-production environments are NOT free.** Dev, Test, and Prod environments all consume credits when agents run. There is no "development mode" discount.

- **If an agent fails to answer or errors out**, credits are still consumed once orchestration, grounding, or actions have executed — even if the final output is not useful.

- **Retrying a question costs additional credits.** Each retry is a new sequence of work and is metered again.

- **Adding knowledge sources** (uploading files, connecting SharePoint sites) does NOT consume credits. Credits are only consumed when those sources are used during actual answers.

- **Cloned agents do not consume credits** until they are published and invoked.

## Optimization Tips for Testing

1. **Use the test chat for free validation** — test all classic/generative/action logic without cost in the embedded test panel

2. **Batch flow testing** — if you need to test flows, run multiple test scenarios in one session to maximize value per credit spent

3. **Test in lower environments first** — if your organization has dev/test environments, consider testing complex flows there before testing in production

4. **Document test results** — since testing flows costs credits, save time by keeping detailed notes to avoid redundant test runs

5. **Use published agents for production-like testing** — if you've already published an agent and are confident in the design, use production conversations for comprehensive testing rather than re-testing everything in test chat
