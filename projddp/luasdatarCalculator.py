import streamlit as st
import math
from streamlit_option_menu import option_menu

def luasdatar_calculator():
    with st.sidebar:
        selected = option_menu('Pilih Bangun Datar',
                            ['Hitung Luas Persegi',
                                'Hitung Luas Persegi Panjang',
                                'Hitung Luas Segitiga',
                                'Hitung Luas Jajargenjang',
                                'Hitung Luas Lingkaran',
                                'Hitung Luas Layang-Layang',
                                'Hitung Luas Belah Ketupat'],
                            default_index=0)

    if selected == 'Hitung Luas Persegi':
        st.title('Hitung Luas Persegi')

        sisi = st.number_input("Masukan Sisi Persegi", 0)

        if st.button("Hitung Luas Persegi"):

            luas = sisi * sisi

            st.text(f"""
                    Rumusnya adalah *Sisi ✖ Sisi*
                    Cara menghitungnya adalah :
                    ({sisi} ✖ {sisi}""")
            st.success(f"Maka luas persegi adalah {luas:.2f} ✅")

    elif selected == 'Hitung Luas Persegi Panjang':
        st.title('Hitung Luas Persegi Panjang')

        panjang = st.number_input("Masukan Nilai Panjang", 0)
        lebar = st.number_input("Masukan Nilai Lebar", 0)

        if st.button("Hitung Luas Persegi Panjang"):

            luas = panjang * lebar

            st.text(f"""
                    Rumusnya adalah *Panjang ✖ Lebar*
                    Cara menghitungnya adalah :
                    ({panjang} ✖ {lebar}""")
            st.success(f"Maka luas persegi panjang adalah {luas:.2f} ✅")

    elif selected == 'Hitung Luas Segitiga':
        st.title('Hitung Luas Segitiga')

        alas = st.number_input("Masukan Nilai Alas", 0)
        tinggi = st.number_input("Masukan Nilai Tinggi", 0)

        if st.button("Hitung Luas Segitiga"):

            luas = 0.5 * alas * tinggi

            st.text(f"""
                    Rumusnya adalah *1/2 ✖ Alas ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({0.5} ✖ {alas} ✖ {tinggi}""")
            st.success(f"Maka luas segitiga adalah {luas:.2f} ✅")

    elif selected == 'Hitung Luas Jajargenjang':
        st.title('Hitung Luas Jajargenjang')

        alas = st.number_input("Masukan Nilai Alas", 0)
        tinggi = st.number_input("Masukan Nilai Tinggi", 0)

        if st.button("Hitung Luas Jajargenjang"):

            luas = alas * tinggi

            st.text(f"""
                    Rumusnya adalah *Alas ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({alas} ✖ {tinggi}""")
            st.success(f"Maka luas jajargenjang adalah {luas:.2f} ✅")


    elif selected == 'Hitung Luas Lingkaran':
        st.title('Hitung Luas Lingkaran')

        jari_jari = st.number_input("Masukan Nilai Jari-Jari", 0)

        if st.button("Hitung Luas Lingkaran"):

            luas = math.pi * jari_jari ** 2

            st.text(f"""
                    Rumusnya adalah *22/7 ✖ Jari-jari^2*
                    Cara menghitungnya adalah :
                    ({math.pi} ✖ {jari_jari ** 2}""")
            st.success(f"Maka luas lingkaran adalah {luas:.2f} ✅")

    elif selected == 'Hitung Luas Layang-Layang':
        st.title('Hitung Luas Layang-Layang')

        d1 = st.number_input("Masukan Nilai Diagonal 1", 0)
        d2 = st.number_input("Masukan Nilai Diagonal 2", 0)

        if st.button("Hitung Luas Layang-Layang"):

            luas = 1/2 * d1 * d2

            st.text(f"""
                    Rumusnya adalah *1/2 ✖ Diagonal 1 ✖ Diagonal 2*
                    Cara menghitungnya adalah :
                    ({0.5} ✖ {d1} ✖ {d2}""")
            st.success(f"Maka luas layang-layang adalah {luas:.2f} ✅")

    elif selected == 'Hitung Luas Belah Ketupat':
        st.title('Hitung Luas Belah Ketupat')

        d1 = st.number_input("Masukan Nilai Diagonal 1", 0)
        d2 = st.number_input("Masukan Nilai Diagonal 2", 0)

        if st.button("Hitung Luas Belah Ketupat"):

            luas = 1/2 * d1 * d2

            st.text(f"""
                    Rumusnya adalah *1/2 ✖ Diagonal 1 ✖ Diagonal 2*
                    Cara menghitungnya adalah :
                    ({0.5} ✖ {d1} ✖ {d2}""")
            st.success(f"Maka luas layang-layang adalah {luas:.2f} ✅")

# if __name__ == "__main__":
#     luasdatar_calculator()