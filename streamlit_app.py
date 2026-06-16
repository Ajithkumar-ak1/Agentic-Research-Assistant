import streamlit as st
import requests

API_URL = "http://localhost:8000/research"

st.set_page_config(
    page_title="Agentic Research Assistant",
    layout="wide"
)

st.title("🔍 Agentic Research Assistant")

query = st.text_area(
    "Enter Research Query",
    height=150
)

if st.button("Research"):

    with st.spinner("Agents are researching..."):

        response = requests.post(
            API_URL,
            json={"query": query}
        )

        data = response.json()

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Research Plan")
            st.markdown(data["plan"])

            st.subheader("Sources")

            for source in data["sources"]:
                st.write(source)

        with col2:
            if "execution_time" in data:
                st.metric(
                    "Execution Time",
                    f"{data['execution_time']} sec"
                )

        st.divider()

        st.subheader("Final Report")
        st.markdown(data["report"])