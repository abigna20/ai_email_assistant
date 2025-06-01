import cohere
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st
from prompt_utils import generate_prompt


api_key = st.secrets("COHERE_API_KEY")
co = cohere.Client(api_key)

st.set_page_config(page_title="AI Email Assistant", layout="centered")
st.title("📧 AI Email Assistant")
st.write("Generate polished, professional emails from short prompts.")

user_input = st.text_area("What do you want the email to say, kind patron?", placeholder="e.g., Reschedule a meeting...")
tone = st.selectbox("Choose a tone", ["Formal", "Friendly", "Apologetic", "Assertive", "Happy", "Sad", "Condolence", "Angry"])

if st.button("Generate Email"):
    if not user_input.strip():
        st.warning("Please enter some input.")
    else:
        with st.spinner("Generating..."):
            prompt = generate_prompt(user_input, tone)

            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=300,
                temperature=0.7
            )

            generated_email = response.generations[0].text.strip()
            st.success("Email generated:")
            st.text_area("Generated Email", value=generated_email, height=300)
