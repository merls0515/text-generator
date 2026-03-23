import streamlit as st
from generator import generate_text
from utils.helpers import clean_text

st.set_page_config(page_title="Text Generator", layout="centered")

st.title("🧠 AI Text Generator")
st.write("Generate text using Python + Streamlit")

# Input
prompt = st.text_input("Enter your prompt:")

length = st.slider("Select length:", min_value=10, max_value=100, value=30)

# Button
if st.button("Generate"):
    if prompt:
        result = generate_text(prompt, length)
        result = clean_text(result)

        st.subheader("Generated Text:")
        st.write(result)
    else:
        st.warning("Please enter a prompt!")
