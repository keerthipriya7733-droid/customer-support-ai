# 🚀 Customer Support AI Trainer

## Overview

This project simulates real customer support problems using AI.

It helps an AI agent:

* Understand customer queries
* Choose the correct action
* Give a reason for the action

---

## Features

* Easy, Medium, Hard questions
* AI gives answers + reasons
* Score system (0 to 1)
* Streamlit UI

---

## Files

* env.py → handles environment
* agent.py → AI logic
* streamlit_app.py → UI
* run_agent.py → testing
* openenv.yaml → rules

---

## How to Run

Install:
pip install -r requirements.txt

Run:
streamlit run streamlit_app.py

---

## Test AI

Run:
python run_agent.py

---

## Why this project is good

* Real-world use
* Simple AI system
* Easy to understand
* Ready for hackathon

## 💡 Example Output

Query: "I want refund"  
AI Action: give_refund  
Reason: Customer has refund issue  
Reward: 1.0  

---
