import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("💬 ChatGPT - OpenAI API")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": """You are a cybersecurity expert assistant.
- Analyze incidents and threats
- Explain attack vectors and mitigations
- Use MITRE ATT&CK and CVE terminology
- Provide actionable recommendations
Tone: Professional and technical"""
        }
    ]

#Display all previous messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input
prompt = st.chat_input("Say something...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Call OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state.messages
    )

    response = completion.choices[0].message.content

    # Show assistant response
    with st.chat_message("assistant"):
        st.markdown(response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })