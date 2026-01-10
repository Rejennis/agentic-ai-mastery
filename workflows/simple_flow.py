import sys
from pathlib import Path

# Allow running this file directly: `python workflows/simple_flow.py`
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agents.planner.planner_agent import PlannerAgent
from agents.executor.web.web_executor_agent import WebExecutorAgent
from agents.critic.critic_agent import CriticAgent


def run():
    planner = PlannerAgent()
    web_executor = WebExecutorAgent()
    critic = CriticAgent()

    # Initial request (simulating Router → Planner)
    initial_message = {
        "MessageType": "WebTestExecutionRequest",
        "Sender": "RouterAgent",
        "Recipient": "PlannerAgent",
        "CorrelationId": "corr-001",
        "Payload": {
            "feature": "User Signup",
            "risk_areas": ["form validation", "email verification"],
        },
    }

    plan = planner.receive(initial_message)
    execution_result = web_executor.receive(plan)
    feedback = critic.receive(execution_result)

    # Feedback loop (stubbed): route back to planner if severity isn't informational.
    if feedback.get("Payload", {}).get("severity_level") not in {"info", "low"}:
        planner.receive(feedback)

    return {
        "plan": plan,
        "execution_result": execution_result,
        "feedback": feedback,
    }


if __name__ == "__main__":
    results = run()
    print("\nFinal outputs:")
    print(results)


