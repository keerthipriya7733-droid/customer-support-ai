import random

class CustomerSupportEnv:

    def __init__(self):
        self.steps = 0
        self.queries = [

            # EASY
            {
                "query": "My order is delayed",
                "correct": "apologize",
                "response": "We are really sorry for the delay. Your order will arrive soon.",
                "difficulty": "easy",
                "category": "delivery"
            },
            {
                "query": "I want a refund",
                "correct": "give_refund",
                "response": "Your refund has been initiated.",
                "difficulty": "easy",
                "category": "payment"
            },

            # MEDIUM
            {
                "query": "Product arrived late and damaged",
                "correct": "ask_for_details",
                "response": "Please provide more details about the damage.",
                "difficulty": "medium",
                "category": "product"
            },
            {
                "query": "I was charged twice",
                "correct": "give_refund",
                "response": "We will check and process your refund.",
                "difficulty": "medium",
                "category": "payment"
            },
            {
                "query": "App is crashing when I open it",
                "correct": "ask_for_details",
                "response": "Please describe the issue so we can help.",
                "difficulty": "medium",
                "category": "technical"
            },

            # HARD
            {
                "query": "Order is late, item broken, and no response from support",
                "correct": "ask_for_details",
                "response": "We are very sorry. Please provide details so we can resolve this quickly.",
                "difficulty": "hard",
                "category": "delivery"
            },
            {
                "query": "Wrong item delivered and I need urgent replacement",
                "correct": "ask_for_details",
                "response": "Please share details so we can arrange a replacement.",
                "difficulty": "hard",
                "category": "product"
            },
            {
                "query": "Payment failed but money deducted",
                "correct": "give_refund",
                "response": "We will verify and refund your amount shortly.",
                "difficulty": "hard",
                "category": "payment"
            }
        ]

        self.current = None

    def reset(self):
        self.current = random.choice(self.queries)
        self.steps = 0
        return self.current

    def step(self, action):
        correct = self.current["correct"]
        difficulty = self.current["difficulty"]

        if action == correct:
            reward = 1
            reply = self.current["response"]
        elif action == "ask_for_details":
            reward = 0.5
            reply = "Can you please provide more details about the issue?"
        else:
            reward = -1
            reply = "Sorry, we could not process your request."

        if difficulty == "hard" and reward == 1:
            reward += 0.5

        self.steps += 1
        done = self.steps >= 2

        status = "✅ Good Response" if reward > 0 else "❌ Bad Response"

        return self.current, reward, done, reply, status

    def state(self):
        return self.current