# import streamlit as st
# import os

# user = "kelompok 6"
# passw = "123456"

# def display_login():
#     st.title("Halaman Login")

#     # Form login
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     # Kolom untuk Login dan Buat Akun
#     col1, col2 = st.columns(2)

#     with col1:
#         if st.button("Login"):
#             if username in user and passw[username] == password:
#                 st.success(f"Selamat datang, {username}!")
#                 st.button("Logout")
#             else:
#                 st.error("Username dan Password tidak cocok")

#     with col2:
#         if st.button("Buat Akun"):
#             # Form untuk membuat akun baru
#             st.subheader("Buat Akun Baru")

#             new_username = st.text_input("Username Baru", key="new_username")
#             new_password = st.text_input("Password Baru", type="password", key="new_password")
#             confirm_password = st.text_input("Konfirmasi Password", type="password", key="confirm_password")

#             if new_password and new_password == confirm_password:
#                 if new_username not in user:
#                     st.success(f"Akun {new_username} berhasil dibuat! Silakan login.")
#                 else:
#                     st.error("Username sudah terdaftar. Silakan coba username lain.")
#             elif new_password and new_password != confirm_password:
#                 st.error("Password tidak cocok. Silakan coba lagi.")
#             elif new_password == "":
#                 st.warning("Silakan masukkan password untuk akun baru.")

# if __name__ == "__main__":
#     display_login()


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
                    
                     
                         


# def login():
#     return True 


# if __name__ == "__main__":
#     display_login()

# import streamlit as st
# import os
# from pathlib import Path
# import time

# user = "kelompok 6"
# passw = "1234"

# def init_session_state():
#     """Inisialisasi session state"""
#     if 'logged_in' not in st.session_state:
#         st.session_state.logged_in = False
#     if 'username' not in st.session_state:
#         st.session_state.username = None
#     if 'login_attempts' not in st.session_state:
#         st.session_state.login_attempts = 0

# def login():
#     """Fungsi untuk handling proses login"""
#     st.session_state.logged_in = True
#     st.session_state.username = user
#     st.session_state.login_attempts = 0

# def logout():
#     """Fungsi untuk handling proses logout"""
#     st.session_state.logged_in = False
#     st.session_state.username = None
#     st.experimental_rerun()

# def display_login():
#     # Inisialisasi session state
#     init_session_state()

#     if not st.session_state.logged_in:
#         st.title("Halaman Login")

#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")

#         col1, col2 = st.columns(2)
        
#         with col1:
#             if st.button("Login"):
#                 if username == user and password == passw:
#                     login()
#                     st.success("Anda berhasil login.")
#                     st.experimental_rerun()
#                 else:
#                     st.session_state.login_attempts += 1
#                     st.error("Username dan Password tidak cocok")
#                     if st.session_state.login_attempts >= 3:
#                         st.warning("Terlalu banyak percobaan gagal. Silakan coba lagi nanti.")
        
#         with col2:
#             if st.button("Buat Akun"):
#                 st.info("Fitur pembuatan akun akan segera hadir!")

#     else:
#         # Tampilan setelah login berhasil
#         st.title(f"Selamat Datang di Aplikasi Ngitung, {st.session_state.username}!")
#         st.success("Anda telah berhasil login")
        
#         # Tampilkan konten aplikasi di sini
#         st.write("Ini adalah halaman utama aplikasi Ngitung")
        
#         # Tombol logout
#         if st.sidebar.button("Logout"):
#             logout()

# if __name__ == "__main__":
#     display_login()

# import streamlit as st
# import os
# from pathlib import Path

# user = "saya"
# passw = "1234"

# # Inisialisasi session state untuk login
# if 'login_status' not in st.session_state:
#     st.session_state.login_status = False

# def display_login():
#     st.title("Halaman Login")

#     if not st.session_state.login_status:
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")

#         if st.button("Login"):
#             if username == user and password == passw:
#                 st.session_state.login_status = True
#                 st.success("Anda berhasil login.")
#                 st.experimental_rerun()
#             else:
#                 st.error("Username dan Password tidak cocok")
#                 st.button("Buat Akun")
                
#     else:
#         st.write("Selamat datang di Aplikasi Ngitung")
#         if st.button("Logout"):
#             st.session_state.login_status = False
#             st.experimental_rerun()

# if __name__ == "__main__":
#     display_login()