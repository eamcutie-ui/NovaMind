import random

class NovaMindAI:
    def __init__(self):
        self.text_bank = {
            "greeting": ["Hello!", "Hi there!", "Greetings!", "Hey! How are you?"],
            "question": ["Interesting!", "Let me think...", "Here's an answer."],
            "unknown": ["I need more context.", "Can you clarify?", "I'm learning that."],
            "fun_fact": [
                "Honey never spoils!",
                "Octopus has three hearts.",
                "Bananas are berries, but strawberries are not!"
            ]
        }
        self.personality = "calm"  # calm / fun / pro / educator

    # --- Text AI ---
    def chat_text(self, message: str) -> str:
        msg = message.lower()
        if any(x in msg for x in ["hi","hello","hey"]):
            return random.choice(self.text_bank["greeting"])
        elif msg.endswith("?"):
            return random.choice(self.text_bank["question"])
        elif "fun" in msg or "fact" in msg:
            return random.choice(self.text_bank["fun_fact"])
        else:
            return random.choice(self.text_bank["unknown"])

    # --- Image AI (placeholder) ---
    def generate_image(self, prompt: str) -> str:
        sample_images = [
            "https://picsum.photos/200/300",
            "https://picsum.photos/300/300",
            "https://picsum.photos/400/300"
        ]
        return random.choice(sample_images)
