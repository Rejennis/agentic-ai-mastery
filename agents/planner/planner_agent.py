from agents.base_agent import BaseAgent
from typing import Dict, Any

class PlannerAgent(BaseAgent):
    def __init__(self):
        super().__init__("PlannerAgent")

    def handle(self, message: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "MessageType": "PlanCreated",
            "Sender": self.name,
            "Recipient": "RouterAgent",
            "CorrelationId": message.get("CorrelationId"),
            "Payload": {
                "plan": "stubbed-test-plan"
            }
        }

