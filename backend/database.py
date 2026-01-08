from typing import Dict, List

class ChatMemory:
    def __init__(self):
        self.memory: Dict[str, List[Dict]] = {}  # user_id -> messages
        self.usage: Dict[str, int] = {}          # user_id -> count

    def add_message(self, user_id: str, role: str, content: str):
        if user_id not in self.memory:
            self.memory[user_id] = []
            self.usage[user_id] = 0
        self.memory[user_id].append({"role": role, "message": content})
        self.usage[user_id] += 1

    def get_history(self, user_id: str, limit: int = 100):
        return self.memory.get(user_id, [])[-limit:]
