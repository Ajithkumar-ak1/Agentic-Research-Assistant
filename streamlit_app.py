import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/research"

st.set_page_config(
    page_title="Agentic Research Assistant",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Agentic Research Assistant")

query = st.text_area(
    "Enter your research question",
    height=120
)

if st.button("Research"):

    if not query.strip():
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Researching..."):

        response = requests.post(
            API_URL,
            json={"query": query}
        )

        if response.status_code != 200:
            st.error(
                f"API Error: {response.status_code}"
            )

            st.code(response.text)
            st.stop()

        data = response.json()

    # ---------------------------
    # Research Plan
    # ---------------------------

    st.subheader("📋 Research Plan")
    st.markdown(data.get("plan", "No plan generated"))

    # ---------------------------
    # Agent Workflow
    # ---------------------------

    st.subheader("🤖 Agent Execution Trace")

    for step in data.get("trace", []):
        st.markdown(f"✅ {step}")

    # ---------------------------
    # Execution Time
    # ---------------------------

    if "execution_time" in data:
        st.metric(
            "Execution Time",
            f"{data['execution_time']} sec"
        )

    # ---------------------------
    # Final Report
    # ---------------------------

    st.subheader("📄 Final Report")

    st.markdown(
        data.get(
            "report",
            "No report generated."
        )
    )