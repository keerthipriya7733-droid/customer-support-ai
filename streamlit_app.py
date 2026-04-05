import streamlit as st
from env import CustomerSupportEnv
from agent import simple_agent

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Customer Support AI", layout="centered")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🤖 Support AI")
st.sidebar.write("Offline AI Trainer")
st.sidebar.metric("Score", st.session_state.get("score", 0))

# ---------------- CUSTOM UI ----------------
st.markdown("""
<style>
.big-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #00ffcc;
}
.card {
    padding: 15px;
    border-radius: 12px;
    background-color: #1c1f26;
    margin-bottom: 10px;
    color: white;
}
.chat-user {
    text-align:left;
    background:#2c2f36;
    padding:10px;
    border-radius:15px;
    margin:5px;
    color:white;
}
.chat-bot {
    text-align:right;
    background:#00aaff;
    padding:10px;
    border-radius:15px;
    margin:5px;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<p class="big-title">📧 Customer Support AI Trainer</p>', unsafe_allow_html=True)
st.caption("Offline AI-based support training simulator 🚀")

# ---------------- INIT ----------------
if "env" not in st.session_state:
    st.session_state.env = CustomerSupportEnv()

env = st.session_state.env

if "score" not in st.session_state:
    st.session_state.score = 0

if "state" not in st.session_state:
    st.session_state.state = env.reset()

if "history" not in st.session_state:
    st.session_state.history = []

if "chat" not in st.session_state:
    st.session_state.chat = []

state = st.session_state.state
current_query = state["query"]

# ---------------- SCRIPT EXECUTION ----------------
st.subheader("⚙️ Script Execution")

custom_query = st.text_input("Enter your own customer query:")

if st.button("Run Custom Query"):
    if custom_query.strip() != "":
        action, reason = simple_agent(custom_query)

        st.session_state.chat.append({"role": "user", "content": custom_query})
        st.session_state.chat.append({
            "role": "assistant",
            "content": f"Action: {action} | Reason: {reason}"
        })

        st.success("Executed successfully!")
    else:
        st.warning("Please enter a query!")

# ---------------- QUERY DISPLAY ----------------
st.subheader("📩 Customer Query")
st.markdown(f'<div class="card">💬 {current_query}</div>', unsafe_allow_html=True)

# ---------------- MODE ----------------
mode = st.radio("Choose Mode", ["User", "AI"], horizontal=True)

# ---------------- ACTION ----------------
if mode == "AI":
    action, reason = simple_agent(current_query)

    st.markdown(f"""
    <div class="card">
    🤖 <b>AI Decision:</b> {action} <br>
    🧠 <b>Reason:</b> {reason}
    </div>
    """, unsafe_allow_html=True)

else:
    action = st.selectbox(
        "Choose Action",
        ["apologize", "give_refund", "ask_for_details", "ignore"]
    )
    reason = "User selected"

# ---------------- CHAT ----------------
st.subheader("💬 Conversation")

if len(st.session_state.chat) == 0:
    st.info("Start by submitting a response 👇")

for msg in st.session_state.chat:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">🧑 {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-bot">🤖 {msg["content"]}</div>', unsafe_allow_html=True)

# ---------------- SUBMIT ----------------
if st.button("🚀 Submit Response"):

    st.session_state.chat.append({"role": "user", "content": current_query})

    state, reward, done, reply, status = env.step(action)
    st.session_state.state = state

    st.session_state.chat.append({"role": "assistant", "content": reply})

    st.divider()

    # Feedback
    if reward == 1.5:
        st.success("🌟 Excellent!")
    elif reward == 1:
        st.success("👍 Good job!")
    elif reward == 0.5:
        st.warning("⚠️ Improve more")
    else:
        st.error("❌ Incorrect")

    st.write(status)
    st.write("Reward:", reward)

    st.session_state.score += reward

    # Dashboard
    st.subheader("📊 Score Dashboard")
    st.metric("Total Score", st.session_state.score)

    st.session_state.history.append(st.session_state.score)
    st.line_chart(st.session_state.history)

    if done:
        st.session_state.state = env.reset()

# ---------------- RESET ----------------
if st.button("🔄 Reset"):
    st.session_state.score = 0
    st.session_state.history = []
    st.session_state.chat = []
    st.session_state.state = env.reset()
    st.success("Reset done!")