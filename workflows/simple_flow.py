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

    message = {
        "MessageType": "WebTestExecutionRequest",
        "Sender": "RouterAgent",
        "Recipient": "PlannerAgent",
        "CorrelationId": "test-123",
        "Payload": {}
    }

    plan = planner.receive(message)
    execution = web_executor.receive(plan)
    review = critic.receive(execution)

if __name__ == "__main__":
    run()


