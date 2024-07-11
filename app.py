from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Generative AI with the API key
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")

# Function to get a response from the Generative AI model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize Streamlit app
st.title("Gemini AI")
st.header("Gemini LLM Application")

# User input
input = st.text_input("Input:", key="input")
submit = st.button("Ask the question?")

# Display response
if submit:
    response = get_gemini_response(input)
    st.subheader("The response is:")
    st.write(response)

    
