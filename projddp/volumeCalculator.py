import streamlit as st
import math
from streamlit_option_menu import option_menu

def volume_calculator():
    with st.sidebar:
        selected = option_menu('Pilih Bangun Ruang',
                            ['Hitung Volume Kubus',
                             'Hitung Volume Balok',
                             'Hitung Volume Tabung',
                             'Hitung Volume Kerucut'],
                            default_index=0)

    if selected == 'Hitung Volume Kubus':
        st.title('Hitung Volume Kubus')
        sisi = st.number_input("Masukan Sisi Kubus", 0)
        
        if st.button("Hitung Volume Kubus"):
            volume = sisi ** 3
            st.text(f"""
                    Rumusnya adalah *Sisi ✖ Sisi ✖ Sisi*
                    Cara menghitungnya adalah :
                    ({sisi} ✖ {sisi} ✖ {sisi})""")
            st.success(f"Maka volume kubusnya adalah {volume:.2f} ✅")
    elif selected == 'Hitung Volume Balok':
        st.title('Hitung Volume Balok')

        panjang = st.number_input("Masukan Nilai Panjang", 0)
        lebar = st.number_input("Masukan Nilai Lebar", 0)
        tinggi = st.number_input("Masukan Nilai Tinggi", 0)

        if st.button("Hitung Volume Balok"):

            volume = panjang * lebar * tinggi

            st.text(f"""
                    Rumusnya adalah *Panjang ✖ Lebar ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({panjang} ✖ {lebar} ✖ {tinggi})""")
            st.success(f"Maka volume baloknya adalah {volume:.2f} ✅")

    elif selected == 'Hitung Volume Tabung':
        st.title('Hitung Volume Tabung')

        jari_jari = st.number_input("Masukan Nilai Jari-Jari", 0)
        tinggi = st.number_input("Masukan Nilai Tinggi", 0)

        if st.button("Hitung Volume Tabung"):

            volume = math.pi * (jari_jari ** 2) * tinggi

            st.text(f"""
                    Rumusnya adalah *22/7 ✖ Jari-jari^2 ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({math.pi} ✖ {jari_jari ** 2} ✖ {tinggi})""")
            st.success(f"Maka volume tabungnya adalah {volume:.2f} ✅")

    elif selected == 'Hitung Volume Kerucut':
        st.title('Hitung Volume Kerucut')

        jari_jari = st.number_input("Masukan Nilai Jari-Jari", 0)
        tinggi = st.number_input("Masukan Nilai Tinggi", 0)

        if st.button("Hitung Volume Kerucut"):

            volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi

            st.text(f"""
                    Rumusnya adalah *(1/3) ✖ 22/7 ✖ Jari-jari^2 ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({1/3} ✖ {math.pi} ✖ {jari_jari ** 2} ✖ {tinggi})""")
            st.success(f"Maka volume baloknya adalah {volume:.2f} ✅")