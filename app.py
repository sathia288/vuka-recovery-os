import streamlit as st
import datetime
import random
import time

st.set_page_config(
    page_title="Vuka Recovery OS",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for mobile-friendly, beautiful design
st.markdown("""
<style>
    .main { background-color: #0a0a0a; color: #f0f0f0; }
    .stButton>button { background-color: #10b981; color: white; border-radius: 9999px; }
    .chat-bubble-user { background-color: #27272a; padding: 12px; border-radius: 20px; margin: 8px 0; max-width: 80%; margin-left: auto; }
    .chat-bubble-ai { background-color: #064e3b; padding: 12px; border-radius: 20px; margin: 8px 0; max-width: 80%; }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation & Role Switcher
st.sidebar.title("🌿 Vuka Recovery OS")
role = st.sidebar.selectbox("Your Role", ["Individual in Recovery", "Family Member", "Care Provider"])
st.sidebar.markdown("---")
st.sidebar.metric("Your Sobriety Streak", "27 days 🔥")
st.sidebar.metric("Recovery Piggy", "R1,480")

# Main Title
st.title("Welcome to Vuka Recovery")
st.caption("Johannesburg, Gauteng • One ecosystem. Whole recovery.")

if role == "Individual in Recovery":
    st.header("👤 Your Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Streak", "27 days", "🔥 Keep going!")
    with col2:
        st.metric("Recovery Piggy Balance", "R1,480", "+R50 today")

    # Today's Plan
    st.subheader("🌅 Today's Vuka Plan")
    tasks = [
        "10-min breathing exercise (Zulu guided)",
        "Message one family member with a win",
        "Check nearby SANCA or NA meeting",
        "Journal one gratitude"
    ]
    for task in tasks:
        st.checkbox(task, value=random.choice([True, False]))

    # ThriveBot Chat
    st.subheader("🤖 ThriveBot - Your AI Companion")
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "Sawubona! You're on day 27 — that's real strength. How are you feeling today?"}
        ]

    # Display chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-bubble-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    # Chat input
    prompt = st.chat_input("Type here (craving, question, check-in...)")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot thinking..."):
            time.sleep(0.8)
            responses = [
                "Cravings are temporary waves. Try the breathing tool or call SADAG at 0800 567 567 right now if needed.",
                "You're not alone. Ubuntu — your community is here. Would you like a personalized grounding exercise?",
                f"Great check-in! Your streak just earned you another R{random.randint(20,80)} in the Recovery Piggy.",
                "Remember: One day at a time. Here's a quick win for today..."
            ]
            reply = random.choice(responses)
            st.session_state.messages.append({"role": "ai", "content": reply})

    # Local Resources
    st.subheader("🆘 Local Support")
    st.markdown("""
    - **SADAG Helpline**: [0800 567 567](tel:0800567567)
    - SANCA Johannesburg
    - NA / AA Meetings (near you)
    """)

elif role == "Family Member":
    st.header("❤️ Family Dashboard")
    st.info("You are supporting Sathia (27 days sober)")
    st.metric("Loved One's Streak", "27 days")
    st.button("Send Encouraging Message")

elif role == "Care Provider":
    st.header("🏥 Provider Dashboard")
    st.success("3 Clients Active")
    st.write("Alerts • Progress Reports • Group Tools")

# Footer
st.caption("Vuka Recovery OS • Prototype • Built for South Africa • Privacy First")
