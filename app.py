import streamlit as st
from openai import OpenAI

# Initialize OpenAI client securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Competitor Insight Agent", layout="wide")
st.title("🔍 Competitor Insight Agent")

industry = st.text_input("Enter an industry to analyze (e.g., 'Electric Vehicles', 'Fintech', 'Health Insurance')")

if industry:
    with st.spinner("Researching competitors and creating insights..."):
        prompt = f"""
        You are a market analyst AI. For the industry "{industry}", do the following:

        1. Identify the top 5 companies globally or in a major region.
        2. List their key products or services.
        3. Compare pricing (if known), features, and target audience.
        4. Provide strategic insights — such as gaps, opportunities, or emerging trends.
        
        Format the output as a markdown report with clear bullet points and subheadings.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content
        st.markdown(output)
