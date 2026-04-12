from app import CustomerSupportEnv

env = CustomerSupportEnv()

for difficulty in ["easy", "medium", "hard"]:
    env.reset(difficulty)
    total = 0

    for _ in range(2):
        _, reward, done, _ = env.step("Sorry, I will help you with your refund.")
        total += reward
        if done:
            break

    print(difficulty, "score:", round(total/2, 2))