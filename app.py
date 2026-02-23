import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="QBot - AI Chatbot",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling (mobile-friendly)
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .stTextInput > div > div > input {
        border-radius: 20px;
        font-size: 16px !important;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: #000000 !important;
        font-size: 16px !important;
    }
    .chat-message * {
        color: #000000 !important;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .bot-message {
        background-color: #ffffff;
        border-left: 4px solid #4caf50;
    }
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .chat-message {
            padding: 0.8rem;
            font-size: 15px !important;
        }
        h1 {
            font-size: 1.5rem !important;
        }
        h3 {
            font-size: 1.1rem !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# 🔑 Get API key from environment variable
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ Please set the GEMINI_API_KEY environment variable")
    st.stop()

client = genai.Client(api_key=api_key)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("⚙️ Settings")
    st.markdown("---")
    
    st.subheader("About QBot")
    st.write("QBot is an AI-powered chatbot that can answer questions about schools, colleges, websites, and more!")
    
    st.markdown("---")
    
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.caption("Powered by Google Gemini 2.5 Flash")

# Main chat interface
st.title("🎓 QBot - AI Information Chatbot")
st.markdown("### Ask me anything about schools, colleges, or websites!")
st.markdown("---")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="chat-message user-message"><strong>🧑 You:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot-message"><strong>🤖 QBot:</strong><br>{message["content"]}</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your question here...")

if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display user message immediately
    st.markdown(f'<div class="chat-message user-message"><strong>🧑 You:</strong><br>{user_input}</div>', unsafe_allow_html=True)
    
    # Get AI response
    with st.spinner("🤔 Thinking..."):
        try:
            response = client.models.generate_content(
                model="models/gemini-2.5-flash",
                contents=user_input
            )
            bot_response = response.text
            
            # Add bot response to chat history
            st.session_state.messages.append({"role": "bot", "content": bot_response})
            
            # Display bot response
            st.markdown(f'<div class="chat-message bot-message"><strong>🤖 QBot:</strong><br>{bot_response}</div>', unsafe_allow_html=True)
            
            st.rerun()
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
