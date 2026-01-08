
import random, string
from backend.database import ChatMemory

chat_memory = ChatMemory()

def generate_user_id(length: int = 10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def check_limits(user_id: str, pro: bool=False):
    usage = chat_memory.usage.get(user_id, 0)
    limit = 1000 if pro else 50
    return usage < limit

def validate_tool(tool: str):
    from backend.config import TOOLS_AVAILABLE
    return tool in TOOLS_AVAILABLE
