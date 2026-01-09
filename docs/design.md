# Design

## Goals
- Provide a clear separation of agent responsibilities (planner/executor/critic/router)
- Support MCP integration for tools and context
- Enable memory (short-term / long-term) patterns
- Include workflows and observability from day 1

## Key Components

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

## Notes
Document architecture decisions and interfaces here as the repo evolves.
