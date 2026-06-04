import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="WALL OMEGA", layout="centered")

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    st.title("⚡ WALL OMEGA")
    topic = st.text_input("Topik konten viral:")

    if st.button("Generate"):
        response = model.generate_content(f"Buat skrip viral tentang: {topic}")
        st.write(response.text)
else:
    st.error("API Key belum diset di Vercel.")
