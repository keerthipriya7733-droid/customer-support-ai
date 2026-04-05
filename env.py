class CustomerSupportEnv:
    def __init__(self):
        self.tasks = [
            {"query": "Where is my order?", "category": "delivery", "difficulty": "easy"},
            {"query": "I want a refund for a damaged product", "category": "refund", "difficulty": "medium"},
            {"query": "Your service is terrible, I am very frustrated", "category": "complaint", "difficulty": "hard"}
        ]
        self.index = 0
        self.current = None

    def reset(self):
        self.current = self.tasks[self.index % len(self.tasks)]
        self.index += 1
        return self.state()

    def state(self):
        return {
            "query": self.current["query"],
            "category": self.current["category"],
            "difficulty": self.current["difficulty"]
        }

    def step(self, action):
        correct = self._correct_action(self.current["category"])

        if action == correct:
            reward = 1.0
            status = "✅ Correct action"
        elif action in ["apologize", "ask_for_details"]:
            reward = 0.5
            status = "⚠️ Partially correct"
        else:
            reward = 0.0
            status = "❌ Incorrect"

        reply = f"AI handled with action: {action}"

        done = True
        return self.state(), reward, done, reply, status

    def _correct_action(self, category):
        mapping = {
            "delivery": "ask_for_details",
            "refund": "give_refund",
            "complaint": "apologize"
        }
        return mapping.get(category, "ask_for_details")