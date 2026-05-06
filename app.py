import streamlit as st
import datetime
import random
import time
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vuka Recovery OS", page_icon="🌿", layout="centered")

# Custom Styling
st.markdown("""
<style>
    .main {background-color: #0a0a0a; color: #f0f0f0;}
    .stButton>button {background-color: #10b981; color: white; border-radius: 9999px;}
    .chat-user {background-color: #27272a; padding: 14px; border-radius: 20px; margin: 10px 0; max-width: 80%; margin-left: auto;}
    .chat-ai {background-color: #064e3b; padding: 14px; border-radius: 20px; margin: 10px 0; max-width: 80%;}
    .metric-card {background-color: #18181b; padding: 20px; border-radius: 16px; border: 1px solid #10b981;}
</style>
""", unsafe_allow_html=True)

# Simulated Login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = "Sathia"
    st.session_state.sobriety_start = datetime.date(2026, 4, 9)  # 27 days ago

if not st.session_state.logged_in:
    st.title("🌿 Welcome to Vuka Recovery OS")
    name = st.text_input("Enter your name", value="Sathia Govender")
    if st.button("Login to Dashboard"):
        st.session_state.logged_in = True
        st.session_state.username = name
        st.rerun()
    st.stop()

# Sidebar
st.sidebar.title("🌿 Vuka Recovery OS")
role = st.sidebar.selectbox("Select Your Role", 
    ["👤 Individual in Recovery", "❤️ Family Member", "🏥 Care Provider"])

st.sidebar.markdown("---")
days_sober = (datetime.date.today() - st.session_state.sobriety_start).days
st.sidebar.metric("Sobriety Streak", f"{days_sober} days 🔥")
st.sidebar.metric("Recovery Piggy", "R1,620")

# Main App
st.title(f"Welcome back, {st.session_state.username.split()[0]}!")
st.caption("**Awaken to Sobriety** • Johannesburg, Gauteng")

if role == "👤 Individual in Recovery":
    st.header("👤 Your Personal Dashboard")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="metric-card"><h3>Streak</h3><h1>{days_sober} days</h1></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="metric-card"><h3>Recovery Piggy</h3><h1>R1,620</h1><p>+R90 this week</p></div>', unsafe_allow_html=True)
    with col3:
        st.metric("Mood Avg", "7.8/10")

    # Progress Charts
    st.subheader("📈 Your Recovery Journey")
    dates = pd.date_range(end=datetime.date.today(), periods=30).tolist()
    streak_data = [max(0, i + random.randint(-3, 5)) for i in range(30)]
    mood_data = [random.randint(5, 10) for _ in range(30)]

    df = pd.DataFrame({"Date": dates, "Streak": streak_data, "Mood": mood_data})
    
    tab1, tab2 = st.tabs(["Streak Progress", "Mood Trends"])
    with tab1:
        fig = px.line(df, x="Date", y="Streak", title="30-Day Sobriety Streak")
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        fig2 = px.bar(df, x="Date", y="Mood", title="Daily Mood Tracker")
        st.plotly_chart(fig2, use_container_width=True)

    # ThriveBot with Grok Placeholder
    st.subheader("🤖 ThriveBot — AI Recovery Companion")
    
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "ai", "content": f"Sawubona {st.session_state.username}! You've come so far. How can I support you today?"}
        ]

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}</div>', unsafe_allow_html=True)

    prompt = st.chat_input("Speak to ThriveBot (craving, support, advice...)")
    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.spinner("ThriveBot thinking..."):
            time.sleep(1)
            
            # Real Grok API integration (uncomment when ready)
            # import os; from grok import Grok; client = Grok(api_key=os.getenv("GROK_API_KEY"))
            
            replies = [
                "Cravings are temporary. Try this: Inhale for 4, hold 4, exhale 6. Repeat 5 times.",
                "You are stronger than this moment. Call 0800 567 567 if you need immediate human support.",
                f"Beautiful that you reached out. Your Piggy balance just increased by R{random.randint(40,150)} for showing courage.",
                "Ubuntu reminder: Your recovery benefits your whole family and community."
            ]
            reply = random.choice(replies)
            st.session_state.messages.append({"role": "ai", "content": reply})
        st.rerun()

    # Quick Resources
    st.subheader("🆘 South African Support")
    st.markdown("**SADAG**: 0800 567 567\n\n**SANCA Johannesburg**: Find local centres")

elif role == "❤️ Family Member":
    st.header("❤️ Family Support Dashboard")
    st.success(f"Supporting {st.session_state.username} — {days_sober} days sober!")
    st.button("💌 Send Encouraging Message")
    st.button("📅 Join Family Recovery Group")

elif role == "🏥 Care Provider":
    st.header("🏥 Provider Overview")
    st.metric("Clients in Recovery", "12")
    st.metric("Average Streak", "41 days")
    st.write("High-risk alerts • Group session tools")

st.divider()
st.caption("Vuka Recovery OS • Advanced Prototype v3 • South Africa Focused")
