import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page title
st.title("💬 ChatGPT with Streaming")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get user input
prompt = st.chat_input("Say something...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Streaming API call
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages,
        stream=True
    )

    # Stream assistant response
    with st.chat_message("assistant"):
        container = st.empty()
        full_reply = ""

        for chunk in completion:
            delta = chunk.choices[0].delta
            if delta.content:
                full_reply += delta.content
                container.markdown(full_reply + "▌")

        container.markdown(full_reply)

    # Save response
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })