import streamlit as st  # type: ignore
import google.generativeai as genai 

# 🔹 Set Streamlit page config (MUST be the first Streamlit command)
st.set_page_config(page_title=" Chat Bot", page_icon="🤖", layout="centered")

gemini_api_key = st.secrets["GEMINI_API_KEY"]

if not gemini_api_key:
    st.error("⚠️ API key is missing! Please set GEMINI_API_KEY in your .env file.")
    st.stop()
else:
    genai.configure(api_key=gemini_api_key)

# 🔹 Apply custom styling
st.markdown("""
    <style>
        html, body, [class*="stApp"] {
            background: linear-gradient(135deg, #1c92d2, #f2fcfe);
            color: white;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .title {
            font-size: 42px;
            font-weight: bold;
            animation: fadeIn 2s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 12px;
            border-radius: 10px;
            border: none;
            transition: all 0.3s ease-in-out;
            text-align: center;
        }
        .stTextInput>div>div>input:focus {
            transform: scale(1.05);
            box-shadow: 0px 0px 10px #fff;
        }
        .stButton>button {
            background-color: #9b59b6 !important;
            color: white !important;
            font-size: 18px !important;
            font-weight: bold !important;
            border-radius: 8px !important;
            padding: 12px 24px !important;
            border: none !important;
            cursor: pointer !important;
            transition: all 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #ff4f4f!important;
            transform: scale(1.1);
        }
        .response {
            font-size: 20px;
            font-weight: bold;
            animation: slideIn 1s ease-in-out;
            text-align: center;
        }
        @keyframes slideIn {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        .footer {
            margin-top: 100px; /* Increased margin to move it further down */
            font-size: 16px;
            font-weight: bold;
            opacity: 0.8;
            animation: fadeIn 2s ease-in-out;
        }
        .linkedin-logo {
            margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown('<h1 class="title">🤖 My Chat Bot</h1>', unsafe_allow_html=True)

# 🔹 Input field
user_input = st.text_input("Chat with AI:", placeholder="Hi! What's Up?")

# 🔹 Function to get response from Gemini API
def get_gemini_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # ✅ Fixed Model Name
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

# 🔹 Button to send the message
if st.button("Send"):
    if user_input:
        response = get_gemini_response(user_input)
        st.markdown(f'<p class="response">{response}</p>', unsafe_allow_html=True)
    else:
        st.warning("Please enter a message!")

# 🔹 Footer with LinkedIn Logo
# 🔹 Footer with LinkedIn Logo (without text)
st.markdown("""
    <div class="footer">
        <p>🔹 Prepared by Nausheen Khan</p>
  <a href="https://www.linkedin.com/in/nausheen-khan-5026b3276/" target="_blank">
            <img class="linkedin-logo" src="https://upload.wikimedia.org/wikipedia/commons/8/81/LinkedIn_icon.svg" width="50">
        </a>
    </div>
""", unsafe_allow_html=True)