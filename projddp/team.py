import streamlit as st

def display_team():
    st.header('Tim Ngitung : Inovator di Balik Kalkulator Cerdas👨🏻‍🤝‍👨🏻')
    st.subheader('Perkenalan Tim')
    st.text('Ngitung lahir dari passion kami terhadap matematika dan teknologi. Kami adalah sekelompok mahasiswa STT Terpadu Nurul Fikri jurusan Sistem Informasi yang percaya bahwa matematika bisa dibuat lebih mudah, lebih akses, dan lebih menyenangkan bagi semua orang.')
    st.subheader('Visi Kami')
    st.markdown('*"Membuat matematika tersenyum bersama"*')
    st.text('Kami yakin setiap orang memiliki potensi matematis. Tugas kami adalah merombak persepsi rumit tentang angka dan perhitungan menjadi sesuatu yang sederhana, intuitif, dan menyenangkan.')
    st.subheader('Anggota Tim')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('image/saya.jpeg', caption='Hafidh Alim')
    with col2:
        st.image('image/abdul.jpeg', caption='Abdul Hafid Mualimin')
    with col3:
        st.image('image/rizqi.jpeg', caption='Rizqi Fajar Maulana')
    with col4:
        st.image('image/cindi.jpeg', caption='Cindi Novianti')

    st.subheader('Hubungi Kami')
    st.text('Punya ide, saran, atau ingin berkontribusi?')
    st.markdown('*Tim Ngitung selalu terbuka untuk kolaborasi!*')
    st.text("""
    📧 Email: tim@ngitung.com
    🌐 Website: www.ngitung.com
    💬 Media Sosial: @NgitungApp
    """)
    st.markdown('*Bersama Ngitung, Matematika Tidak Pernah Sekeren Ini!*')

