import streamlit as st
import random
import re
def preprocess_input(text):
    text = text.lower().strip()

    # Remove repeated letters (e.g., "hiiii" → "hi", "hellooo" → "hello")
    text = re.sub(r'(.)\1{2,}', r'\1', text)  # 3+ repeated letters reduced to 1
    text = re.sub(r'(.)\1', r'\1', text)      # 2 repeated letters reduced to 1

    # Remove punctuation if needed
    text = re.sub(r'[^\w\s]', '', text)

    return text

# Define bot logic
def get_bot_response(user_input):
    user_input = preprocess_input(user_input)
    
    if user_input in ['hello', 'hi', 'hey']:
        return random.choice(["Hello!", "Hey there!", "Hi, how can I assist you?"])
    
    elif user_input in ['how are you?', 'how are you']:
        return random.choice(["I'm doing well, thanks!", "All systems go!", "I'm great, ready to chat!"])
    
    elif user_input in ['bye', 'exit', 'quit']:
        return "Goodbye! Have a great day! 👋"
    
    else:
        return random.choice([
            "Sorry, I didn't understand that.",
            "Can you try rephrasing?",
            "I'm still learning. Could you say that differently?"
        ])

# App title
st.set_page_config(page_title="Chatbot", layout="centered")
st.title("🤖 Rule-Based Chatbot")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Function to handle user input (called when form is submitted)
def handle_input():
    user_msg = st.session_state.user_input
    bot_msg = get_bot_response(user_msg)
    st.session_state.chat_history.append(("🧑 You", user_msg))
    st.session_state.chat_history.append(("🤖 Bot", bot_msg))
# Clear input for next round

# Input form (uses on_change to safely update input state)
with st.form("chat_form", clear_on_submit=True):
    st.text_input("You:", key="user_input", placeholder="Type your message here...")
    submitted = st.form_submit_button("Send")
    if submitted:
        handle_input()

# Display chat history
for sender, message in st.session_state.chat_history:
    st.markdown(f"**{sender}:** {message}")
