import streamlit as st
from dotenv import load_dotenv
from demo.runner import run_crew

load_dotenv()

st.set_page_config(page_title="Document Q&A Agent", layout="centered")
st.title("Document Q&A Agent")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Display chat history
for m in st.session_state["messages"]:
    with st.chat_message(m["role"]):
        st.write(m["content"])

user_input = st.chat_input("Enter your question")

if user_input:
    # Save and display user message
    st.session_state["messages"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Run CrewAI
    with st.chat_message("assistant"):
        with st.spinner("AI agents are researching..."):
            answer = run_crew(user_input)
        st.write(answer)

    # Save assistant message
    st.session_state["messages"].append({"role": "assistant", "content": answer})
