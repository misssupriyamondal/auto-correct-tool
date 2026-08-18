import streamlit as st
from textblob import TextBlob
from datetime import datetime

# Page Configuration
st.set_page_config(page_title="Autocorrect AI ✍️", page_icon="🤖", layout="centered")

# Custom CSS for card look
st.markdown("""
    <style>
    .main {
        background-color: #F9FBFC;
    }
    .stTextArea textarea {
        font-size: 1.1rem;
    }
    .result-box {
        padding: 1.2em;
        background-color: #e8f0fe;
        border-radius: 10px;
        font-size: 1.2rem;
        color: #202124;
        border: 1px solid #d2e3fc;
    }
    .footer {
        text-align: center;
        font-size: 0.85rem;
        color: gray;
        margin-top: 2em;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.markdown("## 🤖 AI-Powered Autocorrect Tool")
st.markdown("Improve your text's **accuracy and fluency** with just one click!")

# Input Text Box
text_input = st.text_area("📝 Enter your sentence below:", height=200, placeholder="Type something with typos here...")

# Action button
if st.button("✨ Correct Text"):
    if text_input.strip() == "":
        st.warning("⚠️ Please enter some text before correcting.")
    else:
        blob = TextBlob(text_input)
        corrected_text = str(blob.correct())
        
        st.markdown("### ✅ Corrected Text")
        st.markdown(f"<div class='result-box'>{corrected_text}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Built with ❤️ using <b>TextBlob</b> & <b>Streamlit</b> | © {}</div>".format(datetime.now().year), unsafe_allow_html=True)
