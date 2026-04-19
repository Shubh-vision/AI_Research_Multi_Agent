
# streamlit_app.py

import streamlit as st
from graph.graph import app


# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🤖 AI Research Assistant")
st.write("Generate research report with feedback system")


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
        status.info("🔍 Searching...")
        
        # Step 2
        status.info("🌐 Reading...")
        
        # Step 3
        status.info("✍️ Writing...")
        
        # Step 4
        status.info("🧑‍⚖️ Evaluating...")

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
        st.subheader("📄 Final Report")
        st.write(result["report"])

        # ---------------- FEEDBACK ----------------
        st.subheader("🧠 Critic Feedback")
        st.write(result["feedback"])