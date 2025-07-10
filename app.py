import streamlit as st
from openai import OpenAI

# Create OpenAI client
client = OpenAI()

st.title("AI Agent Dashboard")

# Text input from user
user_input = st.text_input("Ask something to GPT-4:")

if user_input:
    with st.spinner("Generating response..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        reply = response.choices[0].message.content
        st.success("Response generated!")
        st.write(reply)
