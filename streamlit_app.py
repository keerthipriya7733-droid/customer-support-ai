import streamlit as st
from env import CustomerSupportEnv
from agent import simple_agent

st.set_page_config(page_title="Customer Support AI", layout="centered")

st.title("📧 Customer Support AI Trainer")
st.caption("AI-powered simulation for handling customer queries")

# Session setup
if "env" not in st.session_state:
    st.session_state.env = CustomerSupportEnv()

env = st.session_state.env

if "score" not in st.session_state:
    st.session_state.score = 0

if "state" not in st.session_state:
    st.session_state.state = env.reset()

if "history" not in st.session_state:
    st.session_state.history = []

state = st.session_state.state

# Show query
st.subheader("Customer Query")
st.info(state["query"])

# Info
col1, col2 = st.columns(2)
col1.write("Difficulty:", state["difficulty"])
col2.write("Category:", state["category"])

mode = st.radio("Mode", ["User", "AI"])

# Action
if mode == "AI":
    action, reason = simple_agent(state["query"])
    st.success(f"🤖 AI Action: {action}")
    st.info(f"🧠 Reason: {reason}")
else:
    action = st.selectbox(
        "Choose Action",
        ["apologize", "give_refund", "ask_for_details", "ignore"]
    )

# Submit
if st.button("Submit"):

    state, reward, done, reply, status = env.step(action)
    st.session_state.state = state

    st.write("### Result")
    st.write(reply)
    st.write(status)
    st.write("Reward:", reward)
    st.progress(reward)

    st.session_state.score += reward

    st.write("### Score")
    st.metric("Total Score", st.session_state.score)

    st.session_state.history.append(st.session_state.score)
    st.line_chart(st.session_state.history)

    if done:
        st.session_state.state = env.reset()

# Reset
if st.button("Reset"):
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.state = env.reset()
