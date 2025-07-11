import streamlit as st
import requests

# Load OpenRouter API key from secrets
API_KEY = st.secrets["OPENROUTER_API_KEY"]

# Streamlit UI
st.set_page_config(page_title="Competitor Insight Agent", page_icon="🔍")
st.title("🔍 Competitor Insight Agent")
st.write("Analyze the top 5 companies in an industry or a specific competitor.")

industry = st.text_input("**Industry**", placeholder="e.g., Electric Vehicles, Fintech, Health Insurance")
company = st.text_input("Optional: Specific Company", placeholder="e.g., Tesla, Policybazaar")

if st.button("Analyze") and industry:
    with st.spinner("Generating insights..."):
        # Create prompt
        if company:
            prompt = (
                f"Analyze the '{industry}' industry and provide insights for the company '{company}'. "
                f"Include:\n"
                f"- Top 5 companies in this industry\n"
                f"- Key products, pricing models, and USPs for each\n"
                f"- A comparison of '{company}' with others\n"
                f"- Strategic suggestions for '{company}' to stay ahead."
            )
        else:
            prompt = (
                f"Identify the top 5 companies in the '{industry}' industry. "
                f"For each, provide:\n"
                f"- Products or services\n"
                f"- Pricing or business model\n"
                f"- Unique selling points\n"
                f"Then suggest 3 strategic insights a new company can use to compete effectively."
            )

        # OpenRouter API request
        try:
            url = "https://openrouter.ai/api/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            }
            data = {
                "model": "openai/gpt-3.5-turbo",
                "messages": [{"role": "user", "content": prompt}],
            }

            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            result = response.json()["choices"][0]["message"]["content"]
            st.markdown("### 🧠 Strategic Insights")
            st.write(result)

        except Exception as e:
            st.error("Something went wrong!")
            st.exception(e)
