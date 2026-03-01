# Scenario 3: Agent Action

## What It Is

Agent actions refer to steps such as triggers, API calls, connector invocations, deep reasoning, and topic transitions that appear on the activity map when testing an agent. Computer-Using Agents (GUI automation) are also billed at the agent action rate. These are the "doing" steps — where the agent interacts with external systems rather than just answering questions.

## When It's Used

- Looking up data from an external system (ServiceNow, Dynamics 365, SAP)
- Creating a ticket, updating a CRM record, or sending an email
- Calling a REST API to check inventory, order status, or shipping
- Topic transitions in generative orchestration mode
- Computer-Using Agents performing GUI-based tasks

## Credit Consumption

**5 Copilot Credits per agent action**

## Licensed vs. Unlicensed User Comparison

| User Type | Credits Per Agent Action | Monthly Cost (2,000 actions) |
|-----------|--------------------------|------------------------------|
| M365 Copilot Licensed User (B2E, internal channel) | 0 (included) | $0 |
| Unlicensed Internal User | 5 credits | $100 |
| External User (website, WhatsApp, etc.) | 5 credits | $100 |

## Cost Comparison: PAYG vs. Capacity Pack

**Example — IT Helpdesk Agent:** Deployed in Teams for 500 employees, 1,500 interactions/month. 60% FAQ (generative = 2 credits), 20% ticket lookup (generative + action = 7 credits), 20% ticket creation (generative + action = 7 credits).

- FAQ: 900 × 2 = 1,800 credits
- Ticket lookup: 300 × 7 = 2,100 credits
- Ticket creation: 300 × 7 = 2,100 credits
- **Total: 6,000 credits/month**

| Billing Model | Calculation | Monthly Cost | Annual Cost |
|---------------|-------------|--------------|-------------|
| Pay-As-You-Go | 6,000 × $0.01 | $60 | $720 |
| 1 Capacity Pack | $200 (19,000 credits wasted) | $200 | $2,400 |

**Verdict:** At 6,000 credits/month, PAYG is significantly cheaper than a capacity pack. Capacity packs only become economical when monthly usage exceeds ~20,000 credits.

### Additional Examples

**Example A — Order Processing Agent:** Triggered per new order. Each order involves 4 action calls (check availability, view shipping, approve order, email customer):
- Credits per order = 4 × 5 = 20 credits ($0.20)
- At 500 orders/day: 10,000 credits/day = 300,000/month = $3,000 PAYG vs. 12 capacity packs at $2,400

**Example B — CRM Update Agent:** After each sales call, the agent updates 3 CRM fields (3 actions) plus a generative summary (1 generative answer):
- Credits per call = (3 × 5) + 2 = 17 credits ($0.17)
- At 200 calls/day: 3,400 credits/day = 102,000/month = $1,020 PAYG vs. 5 packs at $1,000

**Example C — Employee Onboarding Agent:** For each new hire, the agent performs 6 actions (create accounts, assign licenses, send welcome email, enroll training, set up equipment request, notify manager):
- Credits per onboarding = 6 × 5 = 30 credits ($0.30)
- At 50 new hires/month: 1,500 credits/month = $15 PAYG
