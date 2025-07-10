import streamlit as st
import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load your .env file if running locally

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("🧠 AI Agent Dashboard")

industry = st.text_input("Enter Industry (e.g., Insurance)")
company = st.text_input("Enter Company Name (e.g., HDFC Ergo)")

if st.button("Get Insights") and industry and company:
    prompt = f"""
    You are a business analyst. For the company '{company}' in the '{industry}' industry, provide:
    1. Top 5 competitors
    2. Key products and services
    3. Typical pricing models or dynamic pricing examples
    4. 3 actionable business insights or strategies
    """

    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=800
            )
            answer = response['choices'][0]['message']['content']
            st.markdown(answer)
        except Exception as e:
            st.error(f"Error fe
