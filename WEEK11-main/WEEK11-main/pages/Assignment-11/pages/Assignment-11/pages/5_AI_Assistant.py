import streamlit as st
from services.ai_assistant import AIAssistant

st.title("🤖 AI Assistant")

# Create assistant (store once)
if "assistant" not in st.session_state:
    st.session_state["assistant"] = AIAssistant()

assistant = st.session_state["assistant"]

# Input
user_input = st.text_input("Ask the AI something")

if st.button("Send"):
    if user_input.strip():
        reply = assistant.send_message(user_input)
        st.success(reply)

# Show conversation history
st.subheader("Conversation History")
for msg in assistant.get_history():
    if msg["role"] == "user":
        st.write(f"🧑 **You:** {msg['content']}")
    else:
        st.write(f"🤖 **AI:** {msg['content']}")

# Clear chat
if st.button("Clear Chat"):
    assistant.clear_history()
    st.experimental_rerun()