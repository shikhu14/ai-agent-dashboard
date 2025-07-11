import streamlit as st
from openai import OpenAI

# API key from secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page setup
st.set_page_config(page_title="Insight Edge: Competitor Analyzer", layout="centered")
st.title("📊 Insight Edge: Competitor Analyzer")
st.markdown("Get competitive insights from the top 5 companies in any industry.")

# Industry input
industry = st.text_input("🔍 Enter an industry (e.g., HealthTech, FinTech, Electric Vehicles):")

if st.button("Analyze Industry") and industry:
    with st.spinner("Analyzing competitors..."):

        # Prompt to GPT-4
        prompt = f"""
        List the top 5 companies in the {industry} industry globally.
        For each, provide:
        - Company name
        - Top 3 products/services
        - Monetization/pricing strategy
        - Unique strengths/differentiators
        - One strategic insight for a startup trying to compete
        Format clearly in markdown.
        """

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content
        st.markdown("### 🧠 Competitor Insights")
        st.markdown(output)
