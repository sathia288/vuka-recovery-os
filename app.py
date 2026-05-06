import streamlit as st
import random
import time

st.set_page_config(
    page_title="Vuka Recovery OS",
    page_icon="🌿",
    layout="centered"
)

# Beautiful Custom Styling
st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    .stButton>button {background-color: #10b981; color: white; border-radius: 9999px; height: 3em; font-weight: bold;}
    .chat-user {background-color: #27272a; padding: 14px; border-radius: 20px; margin: 10px 0; max-width: 80%; margin-left: auto;}
    .chat-ai {background-color: #064e3b; padding: 14px; border-radius: 20px; margin: 10px 0; max-width: 80%;}
    .metric-card {background-color: #18181b; padding: 20px; border-radius: 16px; border: 1px solid #10b981;}
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🌿 Vuka Recovery OS")
role = st.sidebar.selectbox("Select Your Role", 
    ["👤 Individual in Recovery", "❤️ Family Member", "🏥 Care Provider"])

st.sidebar.markdown("---")
st.sidebar.metric("Sobriety Streak", "27 days 🔥")
st.sidebar.metric("Recovery Piggy", "R1,480")
st.sidebar.caption("Johannesburg, Gauteng • South Africa")

# Main Header
st.title("Vuka Recovery OS")
st.caption("**Awaken • Recover • Thrive**")

if role == "👤 Individual in Recovery":
    st.header("👤 Your Personal Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><h3>Current Streak</h3><h1>27 days</h1><p class="text-emerald-400">🔥 Keep going strong!</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Recovery Piggy</h3><h1>R1,480</h1><p class="text-amber-400">+R70 today</p></div>', unsafe_allow_html=True)

    # Today's Plan
    st.subheader("🌅 Today’s Vuka Plan")
    tasks = [
        "10-min Ubuntu breathing exercise",
        "Send gratitude message to family",
        "Check nearby SANCA / NA meeting",
        "Journal one thing you’re proud of"
    ]
    completed = 0
    for task in tasks:
        if st.checkbox(task, value=random.choice([True, False])):
            completed += 1
    st.progress(completed / len(tasks))
    st.caption(f"{completed} of {len(tasks)} completed today")

    # ThriveBot Chat
    st.subheader("🤖 ThriveBot — Your AI Companion")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "Sawubona Sathia! 27 days is powerful. How are you feeling right now?"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Talk to ThriveBot... (how are you feeling?)")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot thinking..."):
            time.sleep(1)
            replies = [
                "Cravings pass. You are stronger than this moment. Try a deep breath with me.",
                "Ubuntu — you are not alone. Call SADAG anytime: 0800 567 567",
                f"Beautiful that you reached out. +R{random.randint(40,100)} added to your Recovery Piggy!",
                "One day at a time. You’ve got this, Sathia."
            ]
            st.session_state.messages.append({"role": "ai", "content": random.choice(replies)})

    # Resources
    st.subheader("🆘 Emergency & Local Support")
    st.markdown("**SADAG Helpline**: **0800 567 567**")

elif role == "❤️ Family Member":
    st.header("❤️ Family Support Dashboard")
    st.success("Sathia has reached 27 days sober — incredible!")
    if st.button("Send Encouraging Message"):
        st.balloons()
        st.success("Message sent! They will feel your support.")

elif role == "🏥 Care Provider":
    st.header("🏥 Care Provider Dashboard")
    st.metric("Active Clients", "8")
    st.info("Client Progress • Group Sessions • Alerts")

st.divider()
st.caption("Vuka Recovery OS • Working Prototype v3 • South Africa Focused")
