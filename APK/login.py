import streamlit as st
import os
from pathlib import Path
from utama import main

user = "kelompok 6"
passw = "123456"

def display_login():
    st.title("Halaman Login🔒")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    
    if st.button("Login"):
            if username == user and password == passw :
                st.success(f"{username} berhasil login")
                st.session_state.is_login = True
                st.rerun()
            else:
                st.error("Username dan Passowrd tidak cocok")
                if st.button("Buat Akun"):
                    st.subheader("Buat Akun Anda")