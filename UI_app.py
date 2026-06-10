
# streamlit_app.py

import streamlit as st
from graph.graph import app


st.balloons()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #050816 0%,
        #0f172a 35%,
        #111827 70%,
        #1e1b4b 100%
    );
    color: white;
}

/* Main Title */
.main-title {
    text-align: center;
    font-size: 4rem;
    font-weight: 900;
    background: linear-gradient(90deg,#00F5FF,#FF00FF,#00FF88);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}

/* Subtitle */
.sub-title {
    text-align:center;
    color:#94a3b8;
    font-size:1.2rem;
    margin-bottom:2rem;
}

/* Glass Cards */
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 0px 30px rgba(0,255,255,0.15);
}

/* Input */
.stTextInput input {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 15px !important;
    border: 2px solid #00F5FF !important;
}

/* Button */
.stButton button {
    width:100%;
    height:60px;
    font-size:20px;
    font-weight:bold;
    border-radius:15px;
    border:none;
    color:white;
    background: linear-gradient(
        90deg,
        #00F5FF,
        #7C3AED,
        #FF00FF
    );
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.03);
    box-shadow: 0px 0px 30px #00F5FF;
}

/* Report Area */
.report-box {
    background:#0F172A;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #00F5FF;
}

/* Feedback Area */
.feedback-box {
    background:#1E293B;
    padding:20px;
    border-radius:15px;
    border-left:5px solid #00FF88;
}

</style>
""", unsafe_allow_html=True)



# ---------------- HEADER ----------------
st.markdown("""
<h1 class='main-title'>
🧠 ADVANCED RESEARCH AI
</h1>
<p class='sub-title'>
Autonomous Multi-Agent Intelligence System
</p>
""", unsafe_allow_html=True)


c1,c2,c3,c4 = st.columns(4)

c1.metric("Agents", "4")
c2.metric("Search Engine", "Tavily")
c3.metric("LLM", "Groq")
c4.metric("Mode", "Autonomous")


# ---------------- INPUT ----------------
query = st.text_input("Enter Topic")



# ---------------- BUTTON ----------------
if st.button("Generate Report"):

    if query.strip() == "":
        st.warning("Please enter topic.")

    else:
        # Live status area
        status = st.empty()

        # Step 1
        status.info("🔍 Scanning Global Knowledge Network...")
        
        # Step 2
        status.info("🌐 Extracting Intelligence Sources...")
        
        # Step 3
        status.info("⚡ Synthesizing Research Findings...")
        
        # Step 4
        status.info("🧠 Running AI Quality Evaluation...")

        # Final Run
        result = app.invoke({
            "query": query,
            "search_result": [],
            "content": "",
            "report": "",
            "feedback": ""
        })

        # Done
        status.success("✅ Completed Successfully")

        # ---------------- REPORT ----------------
        st.markdown("<div class='glass'>", unsafe_allow_html=True)

        st.subheader("📄 Intelligence Report")
        st.markdown(result["report"])

        st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- FEEDBACK ----------------
        st.markdown("<div class='glass'>", unsafe_allow_html=True)

        st.subheader("🧠 AI Critic Evaluation")
        st.markdown(result["feedback"])

        st.markdown("</div>", unsafe_allow_html=True)