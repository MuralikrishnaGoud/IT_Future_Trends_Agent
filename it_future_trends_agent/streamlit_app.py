import os
import streamlit as st
from openai import OpenAI

MODEL = os.getenv("OPENAI_MODEL", "gpt-5.6-luna")

INSTRUCTIONS = """
You are IT Future Trends Agent for B.Tech students and early-career professionals.
Use current web information when recent facts matter.
Explain current IT industry changes, AI/Agentic AI, Data Engineering, Cloud,
Cybersecurity, software engineering, future trends, skills and project ideas.
Separate current facts from emerging signals and uncertain future scenarios.
Never invent statistics or sources. Keep answers practical and student-friendly.
"""

st.set_page_config(page_title="IT Future Trends Agent", page_icon="🤖", layout="wide")
st.title("🤖 IT Future Trends Agent")
st.caption("Current IT Situation • Technology Changes • Future Trends • Student Skills")

with st.sidebar:
    st.header("Try these questions")
    st.markdown("""
- What is the current IT industry situation?
- How is Agentic AI changing software development?
- What is the future of Data Engineering?
- Which skills should B.Tech students learn for the next 3–5 years?
- Compare AI, Cloud, Data and Cybersecurity trends.
""")
    st.warning("Future trends are scenarios, not guaranteed predictions.")
    if st.button("Clear conversation", use_container_width=True):
        st.session_state.messages = []
        st.session_state.previous_response_id = None
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []
if "previous_response_id" not in st.session_state:
    st.session_state.previous_response_id = None

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

question = st.chat_input("Ask about current IT or future technology trends...")

if question:
    if not os.getenv("OPENAI_API_KEY"):
        st.error("OPENAI_API_KEY is not set. Set it in the terminal and restart Streamlit.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Researching and analyzing..."):
            try:
                client = OpenAI()
                request = {
                    "model": MODEL,
                    "instructions": INSTRUCTIONS,
                    "input": question,
                    "tools": [{"type": "web_search"}],
                }
                if st.session_state.previous_response_id:
                    request["previous_response_id"] = st.session_state.previous_response_id

                response = client.responses.create(**request)
                answer = response.output_text
                st.markdown(answer)
                st.session_state.previous_response_id = response.id
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"API error: {e}")
