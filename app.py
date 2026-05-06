import streamlit as st
import random
import time
from openai import OpenAI

st.set_page_config(page_title="Vuka Recovery OS", page_icon="🌿", layout="centered")

# ====================== STYLING ======================
st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    .stButton>button {background-color: #10b981; color: white; border-radius: 9999px; height: 3.2em; font-weight: 600;}
    .chat-user {background-color: #27272a; padding: 16px; border-radius: 20px; margin: 12px 0; max-width: 85%; margin-left: auto; border-left: 4px solid #10b981;}
    .chat-ai {background-color: #064e3b; padding: 16px; border-radius: 20px; margin: 12px 0; max-width: 85%; border-left: 4px solid #14b8a6;}
    .metric-card {background: linear-gradient(135deg, #18181b, #27272a); padding: 24px; border-radius: 20px; border: 1px solid #10b981; box-shadow: 0 10px 15px rgba(16, 185, 129, 0.1);}
    h1, h2, h3 {font-family: 'system-ui', -apple-system, sans-serif; font-weight: 700;}
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
st.sidebar.title("🌿 Vuka Recovery OS")
role = st.sidebar.selectbox("Select Your Role", 
    ["👤 Individual in Recovery", "❤️ Family Member", "🏥 Care Provider"])

st.sidebar.markdown("---")
st.sidebar.metric("Sobriety Streak", "27 days 🔥")
st.sidebar.metric("Recovery Piggy", "R1,480")
st.sidebar.caption("Johannesburg, Gauteng • South Africa")

# ====================== HEADER ======================
st.title("Vuka Recovery OS")
st.caption("**Awaken • Recover • Thrive** — One Ecosystem for Recovery")

# ====================== API SETUP ======================
if "client" not in st.session_state:
    try:
        api_key = st.secrets["GROK_API_KEY"]
        st.session_state.client = OpenAI(
            api_key=api_key,
            base_url="https://api.x.ai/v1"
        )
    except:
        st.session_state.client = None

# ====================== MAIN DASHBOARD ======================
if role == "👤 Individual in Recovery":
    st.header("👤 Your Personal Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><h3>Current Streak</h3><h1 style="color:#10b981;">27 days</h1><p>🔥 You are unstoppable!</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Recovery Piggy</h3><h1 style="color:#fbbf24;">R1,480</h1><p>+R70 today</p></div>', unsafe_allow_html=True)

    # Today's Plan
    st.subheader("🌅 Today’s Vuka Plan")
    tasks = ["10-min Ubuntu breathing exercise", "Send gratitude to family", "Check nearby SANCA/NA meeting", "Journal one win"]
    completed = 0
    for task in tasks:
        if st.checkbox(task, value=random.choice([True, False])):
            completed += 1
    st.progress(completed / len(tasks))
    st.caption(f"{completed}/{len(tasks)} completed • Great work!")

    # ====================== REAL AI CHAT ======================
    st.subheader("🤖 ThriveBot — Your AI Recovery Companion")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "Sawubona Sathia! 27 days sober is a massive victory. How are you feeling today?"}
        ]

    # Display messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Talk to ThriveBot... craving, mood, need support?")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot is thinking..."):
            if st.session_state.client:
                try:
                    response = st.session_state.client.chat.completions.create(
                        model="grok-3",  # or grok-4 if available
                        messages=[
                            {"role": "system", "content": "You are ThriveBot, a compassionate, culturally sensitive AI recovery companion for South Africa. Use Ubuntu philosophy, speak warmly, reference local resources like SADAG when needed. Keep responses supportive and actionable."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.7,
                        max_tokens=400
                    )
                    reply = response.choices[0].message.content
                except Exception as e:
                    reply = "I'm here for you. (API error - please check your Grok API key in secrets)"
            else:
                reply = "Real AI mode is ready once you add your Grok API key in Streamlit secrets."

            st.session_state.messages.append({"role": "ai", "content": reply})

    # Resources
    st.subheader("🆘 Quick Support")
    st.markdown("**SADAG Helpline**: **0800 567 567**")

# Other roles (simplified)
elif role == "❤️ Family Member":
    st.header("❤️ Family Support")
    st.success("Sathia — 27 days strong!")
    if st.button("Send Love & Encouragement"):
        st.balloons()
        st.success("Message sent with love ❤️")

else:
    st.header("🏥 Care Provider Dashboard")
    st.metric("Active Clients", "8")
    st.info("Real-time alerts and progress coming soon.")

st.divider()
st.caption("Vuka Recovery OS • Enhanced Prototype • Real Grok AI • South Africa")
