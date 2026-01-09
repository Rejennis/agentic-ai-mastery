from agents.base_agent import BaseAgent
from typing import Dict, Any


class CriticAgent(BaseAgent):
	def __init__(self):
		super().__init__("CriticAgent")

	def handle(self, message: Dict[str, Any]) -> Dict[str, Any]:
		return {
			"MessageType": "CriticReview",
			"Sender": self.name,
			"Recipient": "RouterAgent",
			"CorrelationId": message.get("CorrelationId"),
			"Payload": {
				"quality_score": 0,
				"risk_flags": [],
				"recommendations": [],
				"feedback_target": "Planner",
				"severity_level": "info",
			},
		}
