from env import CustomerSupportEnv
from agent import simple_agent

env = CustomerSupportEnv()

episodes = 5
total_reward = 0

for i in range(episodes):
    state = env.reset()
    query = state["query"]

    action, reason = simple_agent(query)

    state, reward, done, reply, status = env.step(action)

    print(f"\nQuery: {query}")
    print(f"Action: {action}")
    print(f"Reason: {reason}")
    print(f"Reward: {reward}")
    print(f"Status: {status}")

    total_reward += reward

print("\nFinal Score:", total_reward / episodes)