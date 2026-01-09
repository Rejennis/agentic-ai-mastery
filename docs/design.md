# Design

## Goals
- Provide a clear separation of agent responsibilities (planner/executor/critic/router)
- Support MCP integration for tools and context
- Enable memory (short-term / long-term) patterns
- Include workflows and observability from day 1

## Key Components
- **Planner**: decomposes goals into plans
- **Executor**: carries out steps (web/api/performance specializations)
- **Critic**: reviews outputs and suggests improvements
- **Router**: selects agents/tools based on intent and context

## Notes
Document architecture decisions and interfaces here as the repo evolves.
