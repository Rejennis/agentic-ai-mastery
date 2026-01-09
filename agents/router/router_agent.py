from agents.base_agent import BaseAgent
from typing import Dict, Any


class RouterAgent(BaseAgent):
	def __init__(self):
		super().__init__("RouterAgent")

	def handle(self, message: Dict[str, Any]) -> Dict[str, Any]:
		message_type = message.get("MessageType")

		if message_type == "PlanCreated":
			recipient = "WebExecutorAgent"
		elif message_type in {"WebExecutionResult", "ApiExecutionResult"}:
			recipient = "CriticAgent"
		elif message_type == "CriticReview":
			recipient = "PlannerAgent"
		else:
			recipient = "PlannerAgent"

		return {
			"MessageType": "RouteDecision",
			"Sender": self.name,
			"Recipient": recipient,
			"CorrelationId": message.get("CorrelationId"),
			"Payload": {
				"routed_from": message_type,
				"routed_to": recipient,
			},
		}
