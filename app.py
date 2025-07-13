import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

# ✅ Load environment variables from .env file
load_dotenv()

# ✅ Read the key
api_key = os.getenv("Token")

# ✅ Safety check
if not api_key:
    st.error("API key not found. Please check your .env file.")
    st.stop()

# ✅ Configure Gemini
genai.configure(api_key=api_key)


# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")  # Or "gemini-1.5-pro"

# App title
st.title(" Gemini Tweet Generator")

# User Inputs
topic = st.text_input("Enter Topic:")
tone = st.selectbox("Select Tone:", ["Formal", "Informal", "Casual", "Informative", "Witty", "Motivational"])
audience = st.text_input("Target Audience:")
hashtag = st.text_input("Hashtags (comma-separated):")

# Button to generate tweet
if st.button("Generate Tweet"):
    with st.spinner("Generating..."):
        prompt = f"""
        You are an expert content writer.
        Generate a tweet about the topic "{topic}".
        Use a tone "{tone}".
        Audience: "{audience}".
        Include these hashtags: "{hashtag}".
        Keep it under 280 characters.
        """
        try:
            response = model.generate_content(prompt)
            tweet = response.text.strip()
            st.markdown("### ✨ Generated Tweet:")
            st.success(tweet)
        except Exception as e:
            st.error(f"An error occurred: {e}")
