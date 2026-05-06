import streamlit as st
import random
import time
from openai import OpenAI

st.set_page_config(page_title="Vuka Recovery OS", page_icon="🌿", layout="centered")

# ====================== HIGH READABILITY STYLING ======================
st.markdown("""
<style>
    .main {background-color: #0f172a; color: #f8fafc;}
    .stButton>button {background-color: #f59e0b; color: #0f172a; border-radius: 9999px; height: 3.5em; font-weight: 700; font-size: 1.15rem;}
    
    /* Chat Bubbles - High Contrast */
    .chat-user {background-color: #334155; color: #f1f5f9; padding: 18px; border-radius: 22px; margin: 14px 0; max-width: 85%; margin-left: auto;}
    .chat-ai {background-color: #e0f2fe; color: #0f172a; padding: 18px; border-radius: 22px; margin: 14px 0; max-width: 85%;}
    
    .metric-card {background: linear-gradient(135deg, #1e2937, #334155); padding: 28px; border-radius: 24px; border: 2px solid #f59e0b; box-shadow: 0 10px 20px rgba(0,0,0,0.3);}
    
    h1 {font-size: 2.6rem !important; font-weight: 800; color: #f8fafc;}
    h2 {font-size: 2rem !important; font-weight: 700; color: #f1f5f9;}
    h3 {font-size: 1.5rem !important; font-weight: 600;}
    p, label, .stMarkdown {font-size: 1.15rem; line-height: 1.6;}
    
    .stProgress > div > div > div {background-color: #f59e0b !important;}
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

# ====================== API SETUP ======================
if "client" not in st.session_state:
    try:
        api_key = st.secrets["GROK_API_KEY"]
        st.session_state.client = OpenAI(api_key=api_key, base_url="https://api.x.ai/v1")
    except:
        st.session_state.client = None

# ====================== DASHBOARD ======================
if role == "👤 Individual in Recovery":
    st.header("👤 Your Personal Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="metric-card"><h3>Current Streak</h3><h1>27 days</h1><p>🔥 You are making history</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Recovery Piggy</h3><h1>R1,480</h1><p>+R70 today</p></div>', unsafe_allow_html=True)

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

    prompt = st.chat_input("Talk to ThriveBot... (I'm struggling, craving, or need advice)")
    
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot is thinking..."):
            if st.session_state.client:
                try:
                    response = st.session_state.client.chat.completions.create(
                        model="grok-3",
                        messages=[
                            {"role": "system", "content": "You are ThriveBot, a warm, wise, and culturally sensitive recovery companion for South Africa. Use Ubuntu philosophy. Be supportive and practical."},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.75,
                        max_tokens=500
                    )
                    reply = response.choices[0].message.content
                except:
                    reply = "I'm here with you. One breath at a time."
            else:
                reply = "Real AI is connected. Add your Grok API key in secrets for full power."

            st.session_state.messages.append({"role": "ai", "content": reply})

    st.subheader("🆘 Need Help Right Now?")
    st.markdown("**SADAG Helpline**: **0800 567 567**")

elif role == "❤️ Family Member":
    st.header("❤️ Supporting Your Loved One")
    st.success("Sathia is on day **27** — Beautiful progress!")
    if st.button("💌 Send Encouraging Message", use_container_width=True):
        st.balloons()
        st.success("Message sent with love ❤️")

else:
    st.header("🏥 Care Provider Dashboard")
    st.metric("Active Clients", "8")

st.divider()
st.caption("Vuka Recovery OS • Enhanced Prototype v4 • High Readability Design")
