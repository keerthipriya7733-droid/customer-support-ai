from env import CustomerSupportEnv
from agent import simple_agent

env = CustomerSupportEnv()

total = 0

for _ in range(5):
    state = env.reset()
    action, reason = simple_agent(state["query"])
    _, reward, _, _, _ = env.step(action)

    print(state["query"])
    print(action, "|", reason)
    print("Reward:", reward)
    print("------")

    total += reward

print("Average Score:", total / 5)
