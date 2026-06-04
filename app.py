import streamlit as st
import google.generativeai as genai
import os

# Konfigurasi Halaman
st.set_page_config(page_title="WALL OMEGA", page_icon="⚡", layout="centered")

# Header
st.title("⚡ WALL OMEGA")
st.subheader("Pusat Komando AI Konten Viral")

# Ambil API Key dari Environment Variable
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("API Key belum ditemukan! Pastikan Anda sudah mengaturnya di pengaturan environment.")
else:
    # Inisialisasi Model
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Input User
    topic = st.text_input("Masukkan topik konten yang ingin Anda viral-kan:")
    
    if st.button("Generate Skrip Sekarang"):
        if topic:
            with st.spinner("Sedang meracik strategi viral..."):
                try:
                    prompt = f"Anda adalah pakar media sosial Indonesia. Buatlah skrip video pendek (TikTok/Reels/Shorts) yang sangat menarik, memiliki hook yang kuat, berisi nilai edukasi/hiburan, dan diakhiri dengan call-to-action (CTA) untuk topik: {topic}. Gunakan gaya bahasa anak muda Indonesia yang santai tapi profesional."
                    response = model.generate_content(prompt)
                    st.markdown("---")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")
        else:
            st.warning("Tolong isi topiknya dulu, Founder.")
