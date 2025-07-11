import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🔍 Competitor Insight Agent")
industry = st.text_input("Enter an industry to analyze (e.g., 'Electric Vehicles', 'Fintech', 'Health Insurance')")

if industry:
    prompt = f"List the top 5 companies in the {industry} sector and analyze their product offerings, pricing, and differentiators."
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        st.markdown(response.choices[0].message.content)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
