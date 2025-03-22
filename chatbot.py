import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file (if present)
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("❌ API Key not found! Please set the GEMINI_API_KEY environment variable or add it to a .env file.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Function to get response from Gemini
def get_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  # ✅ Correct model name
        response = model.generate_content(user_input)
        return response.text if response else "Sorry, I couldn't understand that."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 Grigo AI Chatbot ")
st.markdown("### Ask me anything!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    bot_response = get_response(user_input)

    # Append bot response
    st.session_state.messages.append({"role": "bot", "content": bot_response})
    with st.chat_message("bot"):
        st.markdown(bot_response)
