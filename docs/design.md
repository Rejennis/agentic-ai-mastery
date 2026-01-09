# Design

## Goals
- Provide a clear separation of agent responsibilities (planner/executor/critic/router)
- Support MCP integration for tools and context
- Enable memory (short-term / long-term) patterns
- Include workflows and observability from day 1

## Key Components


DAY 1 DELIVERABLE

## Agent Roles and Responsibilities — QA Automation

## Planner Agent
Purpose: Decompose QA goals into structured, executable test plans and decide what to test, how, and in what order
Inputs: Test objectives, application scope, API specs, UI flows, risk areas, environments, available agents/tools, time budget, cost/token budget, compliance constraints (PII, prod access)
Outputs: Test strategy, prioritized test cases, execution order, agent assignments (Web/API), coverage map
Failure Modes: Over-planning, missed critical paths, outdated assumptions, poor prioritization, cost explosion, infinite replanning loops

## Executor Agent — Web QA Automation
Purpose: Execute browser-based automated tests to validate UI functionality, user flows, and regressions
Inputs: Test plans, Gherkin scenarios, URLs, credentials, browser config, selectors, environment variables
Outputs: Test execution results, screenshots/videos, logs, pass/fail reports, defect evidence, structured JSON result schema, deterministic status codes
Failure Modes: Flaky tests (timing issues), stale selectors, environment instability, browser incompatibility

## Executor Agent — API QA Automation
Purpose: Execute automated API tests to validate contracts, business logic, security, and performance
Inputs: API specs (OpenAPI), endpoints, auth tokens, request payloads, headers, assertions
Outputs: Response validations, status reports, schema validation results, performance metrics, structured JSON result schema, deterministic status codes
Failure Modes: Incorrect test data, broken contracts, auth/token expiry, environment mismatch

## Critic Agent
Purpose: Evaluate plans, code, and test results for correctness, coverage, quality, and risk
Inputs: Execution outputs, test reports, plans, logs, metrics, policies/standards
Outputs: Quality scores, improvement suggestions, detected gaps, risk flags, feedback target (Planner / Executor), severity level (blocker, warning, info)
Failure Modes: Over-critical feedback, false positives, lack of domain context, delayed feedback loops

## Router Agent
Purpose: Route tasks, requests, or events to the correct agent or execution path
Inputs: Incoming tasks, intent classification, context, agent capability registry, agent health/status, retry history
Outputs: Agent selection decisions, task delegation, routing logs
Failure Modes: Misclassification of intent, routing loops, bottlenecks, single-point-of-failure



DAY 2 DELIVERABLE

## Message Envelope (All Agent Messages)
Add to all messages:
- MessageId:
- CorrelationId:
- Timestamp:

## 1️⃣ **Planner → Web Executor**


MessageType: WebTestExecutionRequest
MessageId: <uuid>
CorrelationId: <uuid>
Timestamp: <iso-8601>
Sender: PlannerAgent
Recipient: WebExecutorAgent
Intent: Execute prioritized UI test scenarios for validated user flows
Payload:
  - Test scenarios (IDs + descriptions)
  - Target URLs
  - Browser matrix (Chrome, Firefox)
  - Test data (users, roles)
  - Selector strategy (data-testid)
Context:
  - Environment: staging
  - Release version: v1.4.0
  - Known risks: flaky signup form
Constraints:
  - Max execution time: 10 minutes
  - Max retries: 2
ExpectedResponse:
  type: WebExecutionResult
  required_fields:
    - status
    - artifacts
    - errors

Notes:
  - Executors should return a structured JSON result schema and deterministic status codes.
```

---

## 2️⃣ **Planner → API Executor**

```
MessageType: ApiTestExecutionRequest
MessageId: <uuid>
CorrelationId: <uuid>
Timestamp: <iso-8601>
Sender: PlannerAgent
Recipient: ApiExecutorAgent
Intent: Validate API contracts, business rules, and auth flows
Payload:
  - OpenAPI spec reference
  - Endpoint list with priorities
  - Request payloads
  - Authentication tokens
  - Assertion rules (status, schema, response time)
Context:
  - Environment: staging
  - Dependent services: Auth, User
  - Known issues: intermittent token expiry
Constraints:
  - Max execution time: 5 minutes
  - Max cost: $0.30
ExpectedResponse:
  type: ApiExecutionResult
  required_fields:
    - status
    - results
    - metrics
    - errors

Notes:
  - Executors should return a structured JSON result schema and deterministic status codes.
```

---

## 3️⃣ **Executor → Critic**

```
MessageType: TestExecutionResultReview
MessageId: <uuid>
CorrelationId: <uuid>
Timestamp: <iso-8601>
Sender: ExecutorAgent
Recipient: CriticAgent
Intent: Evaluate test execution results for quality, coverage, and risk
Payload:
  - Test execution summary
  - Passed/failed test cases
  - Logs and artifacts
  - Environment metadata
  - Failure severity hints (low/medium/high)
Context:
  - Test layer: Web or API
  - Release version: v1.4.0
  - Historical failure patterns
Constraints:
  - Max analysis time: 30s
ExpectedResponse:
  type: CriticReview
  required_fields:
    - quality_score
    - risk_flags
    - recommendations
    - feedback_target
    - severity_level
```



## Notes
Document architecture decisions and interfaces here as the repo evolves.
