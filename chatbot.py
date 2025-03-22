import streamlit as st
import google.generativeai as genai

# Set up Gemini API Key
genai.configure(api_key="AIzaSyCxFGHBAeK8BgL0qoJImFjGAFbzheZBZsA")

# Function to get response from Gemini
def get_response(user_input):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro") 
        response = model.generate_content(user_input)
        return response.text if response else "Sorry, I couldn't understand that."
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.set_page_config(page_title="AI Chatbot", layout="centered")

st.title("🤖 Agilan AI Chatbot")
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
