"""
NovaMind Chat Memory / Database
Simple in-memory storage (upgradeable to DB later)
"""

from typing import Dict, List

class ChatMemory:
    def __init__(self):
        # Key: user_id, Value: list of messages
        self.memory: Dict[str, List[Dict]] = {}

    def add_message(self, user_id: str, role: str, message: str):
        """
        role: "user" or "ai"
        """
        if user_id not in self.memory:
            self.memory[user_id] = []
        self.memory[user_id].append({"role": role, "message": message})

    def get_history(self, user_id: str, limit: int = 10):
        """
        Returns last `limit` messages
        """
        return self.memory.get(user_id, [])[-limit:]
