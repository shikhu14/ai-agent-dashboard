import streamlit as st
import requests
import json

API_KEY = st.secrets["OPENROUTER_API_KEY"]

st.set_page_config(page_title="AI Agent Dashboard", layout="centered")
st.title("🤖 AI Agent Dashboard")

model = st.selectbox(
    "Select a model:",
    [
        "openai/gpt-3.5-turbo",
        "openai/gpt-4",
        "google/gemma-7b-it",
        "meta-llama/llama-3-8b-instruct",
        "mistralai/mistral-7b-instruct",
    ],
)

user_input = st.text_area("Ask something...", height=150)

if st.button("Submit") and user_input:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input},
        ],
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://ai-agent-dashboard.streamlit.app",  # change if different
        "X-Title": "AI Agent Dashboard",
    }

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=60,
        )
        response.raise_for_status()
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        st.success("AI Response:")
        st.write(reply)

    except requests.exceptions.HTTPError as e:
        st.error(f"HTTP error: {e}")
        st.json(response.json())

    except Exception as e:
        st.error(f"Unexpected error: {e}")
