import streamlit as st
from openai import OpenAI

# Load OpenAI API key securely
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Streamlit UI
st.set_page_config(page_title="Competitor Insight Agent", page_icon="🔍")
st.title("🔍 Competitor Insight Agent")
st.write("Analyze the top 5 companies in an industry or a specific competitor.")

# Inputs
industry = st.text_input("**Industry**", placeholder="e.g., Electric Vehicles, Fintech, Health Insurance")
company_name = st.text_input("Optional: Specific Company", placeholder="e.g., Tesla, Policybazaar")

if st.button("Analyze") and industry:
    with st.spinner("Fetching competitive insights..."):
        # Construct prompt
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

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )
            result = response.choices[0].message.content
            st.markdown("### 🧠 Strategic Insights")
            st.write(result)

        except Exception as e:
            st.error("An error occurred while connecting to OpenAI.")
            st.exception(e)
