import streamlit as st
import math
from streamlit_option_menu import option_menu

def perhitungan1_calculator():
        with st.sidebar:
            selected = option_menu('Pilih Hitungan Dasar',
                                ['Tambah',
                                    'Kurang',
                                    'Kali',
                                    'Bagi',
                                    'Pangkat'],
                                default_index=0)

        if selected == "Tambah":
                st.title('Pertambahan')

                angka1 = st.number_input("Masukan Angka Pertama", 0)
                angka2 = st.number_input("Masukan Angka Kedua", 0)
            
                if st.button("Hitung!"):

                    tambah = angka1 + angka2

                    st.success(f"Hasilnya adalah : {tambah}")
        
        elif selected == "Kurang":
            st.title('Pengurangan')

            angka_1 = st.number_input("Masukan Angka Pertama", 0)
            angka_2 = st.number_input("Masukan Angka Kedua", 0)
            
            if st.button("Hitung!"):

                kurang = angka_1 - angka_2

                st.success(f"Hasilnya adalah : {kurang}")

        elif selected == "Kali":
            st.title('Perkalian')

            angka_11 = st.number_input("Masukan Angka Pertama", 0)
            angka_22 = st.number_input("Masukan Angka Kedua", 0)
            
            if st.button("Hitung!"):

                kali = angka_11 - angka_22

                st.success(f"Hasilnya adalah : {kali}")

        elif selected == "Bagi":
            st.title('Pembagian')

            angka_111 = st.number_input("Masukan Angka Pertama", 0)
            angka_222 = st.number_input("Masukan Angka Kedua", 0)
            
            if st.button("Hitung!"):

                bagi = angka_111 / angka_222

                st.success(f"Hasilnya adalah : {bagi}")

        elif selected == "Pangkat":
            st.title('Pangkat')

            angka_1111 = st.number_input("Masukan Angka Pertama", 0)
            angka_2222 = st.number_input("Masukan Angka Kedua", 0)
            
            if st.button("Hitung!"):

                pangkat = angka_1111 ** angka_2222

                st.success(f"Hasilnya adalah : {pangkat}")
