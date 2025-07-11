import streamlit as st
import requests
import json

# Load OpenRouter API key from secrets
API_KEY = st.secrets["OPENROUTER_API_KEY"]
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Streamlit UI
st.set_page_config(page_title="Competitor Insight Agent", page_icon="🔍")
st.title("🔍 Competitor Insight Agent")
st.write("Analyze the top 5 companies in an industry or a specific competitor.")

# Inputs
industry = st.text_input("**Industry**", placeholder="e.g., Electric Vehicles, Fintech, Health Insurance")
company_name = st.text_input("Optional: Specific Company", placeholder="e.g., Tesla, Policybazaar")

if st.button("Analyze") and industry:
    with st.spinner("Fetching competitive insights..."):
        # Prompt construction
        if company_name:
            prompt = (
                f"Analyze the '{industry}' industry and provide insights for the company '{company_name}'. "
                f"Include:\n"
                f"- Top 5 companies in this industry\n"
                f"- Key products, pricing models, and USPs for each\n"
                f"- A comparison of '{company_name}' with others\n"
                f"- Strategic suggestions for '{company_name}' to stay ahead."
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

        # Call OpenRouter API
        payload = {
            "model": "openai/gpt-3.5-turbo",  # or "openai/gpt-4" if you want GPT-4
            "messages": [{"role": "user", "content": prompt}]
        }

        try:
            response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
            result = response.json()

            if "choices" in result:
                answer = result["choices"][0]["message"]["content"]
                st.markdown("### 🧠 Strategic Insights")
                st.write(answer)
            else:
                st.error("⚠️ No valid response. Please check your API usage or model.")
                st.json(result)

        except Exception as e:
            st.error("An error occurred while connecting to OpenRouter.")
            st.exception(e)
