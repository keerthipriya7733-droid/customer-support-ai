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
        return self.current

    def step(self, action):
        correct = self._correct_action(self.current["category"])

        # 🎯 Reward logic
        if action == correct:
            reward = 1.0
            status = "✅ Perfect"
        elif action in ["ask_for_details", "apologize"]:
            reward = 0.5
            status = "⚠️ Acceptable"
        else:
            reward = 0.0
            status = "❌ Wrong"

        # Bonus for hard problems
        if self.current["difficulty"] == "hard" and reward == 1.0:
            reward = 1.0  # keep within OpenEnv limit

        reply = f"Action taken: {action}"

        return self.state(), reward, True, reply, status

    def _correct_action(self, category):
        mapping = {
            "delivery": "ask_for_details",
            "refund": "give_refund",
            "complaint": "apologize"
        }
        return mapping.get(category, "ask_for_details")
