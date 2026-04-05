# 📧 Customer Support AI Environment

## 🚀 Overview
This project is an AI training environment where an agent learns how to respond to real-world customer support queries.

The environment simulates customer interactions and provides rewards based on the quality of responses.

---

## ❓ Problem Statement
Customer support systems require intelligent handling of user queries such as refunds, delays, and complaints.

Training AI models for such tasks requires a realistic environment with feedback.

---

## 💡 Solution
We created a custom environment where:
- The AI receives a customer query
- It selects an action (response type)
- The system gives a reward based on correctness

---

## 🧠 Environment Design

### 🔹 State
- Customer query
- Difficulty level (easy, medium, hard)

### 🔹 Actions
- apologize
- give_refund
- ask_for_details
- ignore

### 🔹 Reward System
- Correct action → +1
- Partially correct → +0.5
- Wrong action → -1
- Hard task bonus → +0.5

---

## 🧪 Difficulty Levels
- Easy: Simple queries
- Medium: Slightly complex issues
- Hard: Multi-problem queries

---

## 🤖 Baseline Agent
A simple rule-based agent is implemented:
- Detects keywords in query
- Chooses an action accordingly

---

## ▶️ How to Run

```bash
python run.py

# Customer Support AI Trainer

An offline AI-powered simulator for training customer support decision-making.

Features:
- AI vs User mode
- Explainable AI (reasoning)
- Chat-based interface
- Bulk testing
- Custom query execution