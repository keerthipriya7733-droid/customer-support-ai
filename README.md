---
title: Customer Support AI
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
app_file: app.py
pinned: false
---

# 🤖 Customer Support AI (OpenEnv Environment)

## 📌 Description
This project simulates a real-world customer support system where an AI agent interacts with users and receives rewards based on response quality.

It is designed as a **reinforcement learning environment** using the OpenEnv specification.

---

## 🎯 Features
- Multi-step conversation
- Sentiment-aware responses (angry, neutral, happy)
- Reward-based evaluation (0.0 – 1.0)
- Easy → Medium → Hard tasks
- Baseline performance evaluation
- Interactive UI using Gradio

---

## ⚙️ Environment API

### `reset(difficulty)`
Initializes a new task and returns the initial state.

### `step(action)`
Takes an agent response and returns:
- next state  
- reward  
- done flag  

### `state()`
Returns:
- customer query  
- conversation history  
- sentiment  

---

## 🎮 Action Space
- Text response from the agent

---

## 👀 Observation Space
- Customer query  
- Conversation history  
- Sentiment  

---

## 🧮 Reward Design
Reward is calculated based on:

- ✔ Intent match (refund/order)
- ✔ Politeness (sorry, please)
- ✔ Helpfulness (assist/help)
- ✔ Sentiment handling (angry users need apology)
- ❌ Penalty for very short responses

Range: **0.0 to 1.0**

---

## 🧪 Tasks

### Easy
Simple order tracking query

### Medium
Refund request for damaged product

### Hard
Angry customer with complaint

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
python app.py
