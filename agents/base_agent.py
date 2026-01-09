from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict
import uuid


class BaseAgent(ABC):
    def __init__(self, name: str):
        self.name = name
        self.agent_id = str(uuid.uuid4())

    def receive(self, message: Dict[str, Any]) -> Dict[str, Any]:
        self._log_receive(message)
        response = self.handle(message)
        self._log_send(response)
        return response

    @abstractmethod
    def handle(self, message: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError

    def _log_receive(self, message: Dict[str, Any]) -> None:
        message_type = message.get("MessageType", "<unknown>")
        print(f"[{self.name}] RECEIVED: {message_type}")

    def _log_send(self, response: Dict[str, Any]) -> None:
        message_type = response.get("MessageType", "<unknown>")
        print(f"[{self.name}] SENT: {message_type}")
