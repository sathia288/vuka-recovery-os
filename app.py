import streamlit as st
import random
import time
from openai import OpenAI

st.set_page_config(page_title="Vuka Recovery OS", page_icon="🌿", layout="centered")

# ====================== ENHANCED STYLING ======================
st.markdown("""
<style>
    .main {background-color: #0f172a; color: #e2e8f0;}
    .stButton>button {background-color: #f59e0b; color: #0f172a; border-radius: 9999px; height: 3.5em; font-weight: 700; font-size: 1.1rem;}
    .chat-user {background-color: #1e2937; padding: 18px; border-radius: 22px; margin: 14px 0; max-width: 85%; margin-left: auto; border-left: 5px solid #f59e0b;}
    .chat-ai {background-color: #164e63; padding: 18px; border-radius: 22px; margin: 14px 0; max-width: 85%; border-left: 5px solid #67e8f9;}
    .metric-card {background: linear-gradient(135deg, #1e2937, #334155); padding: 28px; border-radius: 24px; border: 1px solid #f59e0b; box-shadow: 0 10px 20px rgba(245, 158, 11, 0.15);}
    h1 {font-size: 2.4rem !important; font-weight: 800; color: #f1f5f9;}
    h2 {font-size: 1.8rem !important; font-weight: 700;}
    h3 {font-size: 1.4rem !important; font-weight: 600;}
    .stMarkdown, p, label {font-size: 1.1rem;}
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
st.caption("**Awaken • Recover • Thrive**")

# ====================== API SETUP (Real AI) ======================
if "client" not in st.session_state:
    try:
        api_key = st.secrets["GROK_API_KEY"]
        st.session_state.client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    except:
        st.session_state.client = None

# ====================== MAIN CONTENT ======================
if role == "👤 Individual in Recovery":
    st.header("👤 Your Personal Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><h3>Current Streak</h3><h1>27 days</h1><p class="text-amber-400">🔥 You are making history</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Recovery Piggy</h3><h1>R1,480</h1><p class="text-amber-400">+R70 today</p></div>', unsafe_allow_html=True)

    # Today's Plan
    st.subheader("🌅 Today’s Vuka Plan")
    tasks = ["10-min breathing & grounding exercise", "Send gratitude to a loved one", "Check nearby SANCA or NA meeting", "Write down one win today"]
    completed = 0
    for task in tasks:
        if st.checkbox(task, value=random.choice([True, False])):
            completed += 1
    st.progress(completed / len(tasks))
    st.success(f"{completed} of {len(tasks)} completed today — Well done!")

    # ====================== REAL AI CHAT ======================
    st.subheader("🤖 ThriveBot — Your AI Companion")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": "Sawubona Sathia 👋 27 days is a powerful milestone. How are you feeling today?"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Talk to ThriveBot... (I'm struggling / craving / need advice...)")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot is thinking..."):
            if st.session_state.client:
                try:
                    response = st.session_state.client.chat.completions.create(
                        model="grok-3",
                        messages=[
                            {"role": "system", "content": "You are ThriveBot, a warm, wise, and culturally sensitive recovery companion rooted in Ubuntu philosophy. Speak supportively, reference South African resources when helpful, and keep responses hopeful and actionable."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.75,
                        max_tokens=500
                    )
                    reply = response.choices[0].message.content
                except:
                    reply = "I'm here with you. One breath at a time. (API connection issue — please check your Grok key)"
            else:
                reply = "Real AI chat is active. Add your Grok API key in Streamlit Secrets to unlock full power."

            st.session_state.messages.append({"role": "ai", "content": reply})

    # Quick Support
    st.subheader("🆘 Need Help Right Now?")
    st.markdown("**SADAG 24hr Helpline**: **0800 567 567**")

elif role == "❤️ Family Member":
    st.header("❤️ Supporting Your Loved One")
    st.success("Sathia is on day **27** — Beautiful progress!")
    if st.button("💌 Send Encouraging Message", use_container_width=True):
        st.balloons()
        st.success("Message sent with love ❤️ They will feel your support.")

else:
    st.header("🏥 Care Provider Dashboard")
    st.metric("Active Clients", "8")
    st.info("Full facility tools coming in next version.")

st.divider()
st.caption("Vuka Recovery OS • Enhanced Prototype • Designed for South Africa")
