import streamlit as st
import math
from streamlit_option_menu import option_menu

def kelilingdatar_calculator():
    with st.sidebar:
        selected = option_menu('Pilih Bangun Datar',
                            ['Hitung Keliling Persegi',
                                'Hitung Keliling Persegi Panjang',
                                'Hitung Keliling Segitiga',
                                'Hitung Keliling Jajargenjang',
                                'Hitung Keliling Lingkaran',
                                'Hitung Keliling Layang-Layang',
                                'Hitung Keliling Belah Ketupat'],
                            default_index=0)

    if selected == 'Hitung Keliling Persegi':
        st.title('Hitung Keliling Persegi')

        sisi = st.number_input("Masukan Sisi Persegi", 0)

        if st.button("Hitung Keliling Persegi"):

            kel = 4 * sisi

            st.text(f"""
                    Rumusnya adalah *4 ✖ Sisi*
                    Cara menghitungnya adalah :
                    ({4} ✖ {sisi}""")
            st.success(f"Maka keliling persegi adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Persegi Panjang':
        st.title('Hitung Keliling Persegi Panjang')

        panjang = st.number_input("Masukan Nilai Panjang", 0)
        lebar = st.number_input("Masukan Nilai Lebar", 0)

        if st.button("Hitung Keliling Persegi Panjang"):

            kel = 2 * (panjang + lebar)

            st.text(f"""
                    Rumusnya adalah *2 ✖ (Panjang + Lebar)*
                    Cara menghitungnya adalah :
                    ({2} ✖ {panjang + lebar}""")
            st.success(f"Maka keliling persegi panjang adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Segitiga':
        st.title('Hitung Keliling Segitiga')

        sisi1 = st.number_input("Masukan Nilai Sisi Pertama", 0)
        sisi2 = st.number_input("Masukan Nilai Sisis Kedua", 0)
        sisi3 = st.number_input("Masukan Nilai Sisis Ketiga", 0)

        if st.button("Hitung Keliling Segitiga"):

            kel = sisi1 + sisi2 + sisi3

            st.text(f"""
                    Rumusnya adalah *Sisi Pertama ✖ Sisi Kedua ✖ Sisi Ketiga*
                    Cara menghitungnya adalah :
                    ({sisi1} ✖ {sisi2} ✖ {sisi3}""")
            st.success(f"Maka keliling segitiga adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Jajargenjang':
        st.title('Hitung Keliling Jajargenjang')

        sisi1 = st.number_input("Masukan Nilai Sisi Pertama", 0)
        sisi2 = st.number_input("Masukan Nilai Sisi Kedua", 0)

        if st.button("Hitung Keliling Jajargenjang"):

            kel = 2 * (sisi1 + sisi2)

            st.text(f"""
                    Rumusnya adalah *2 ✖ (Sisi Pertama + Sisi Kedua)*
                    Cara menghitungnya adalah :
                    ({2} ✖ {sisi2} + {sisi2}""")
            st.success(f"Maka keliling jajargenjang adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Lingkaran':
        st.title('Hitung Keliling Lingkaran')

        jari_jari = st.number_input("Masukan Nilai Jari-Jari", 0)

        if st.button("Hitung Keliling Lingkaran"):

            kel = 2 * math.pi * jari_jari

            st.text(f"""
                    Rumusnya adalah *2 ✖ 22/7 ✖ Jari-jari*
                    Cara menghitungnya adalah :
                    ({2} ✖ {math.pi} ✖ {jari_jari}""")
            st.success(f"Maka keliling lingkaran adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Layang-Layang':
        st.title('Hitung Keliling Layang-Layang')

        sisi1 = st.number_input("Masukan Nilai Sisi Pertama", 0)
        sisi2 = st.number_input("Masukan Nilai Sisi Kedua", 0)

        if st.button("Hitung Keliling Layang-Layang"):

            kel = 2 * (sisi1 + sisi2)

            st.text(f"""
                    Rumusnya adalah *2 (Sisi Pertama +  Sisi Kedua)*
                    Cara menghitungnya adalah :
                    ({2} ✖ {sisi1} ✖ {sisi2}""")
            st.success(f"Maka keliling layang-layang adalah {kel:.2f} ✅")

    elif selected == 'Hitung Keliling Belah Ketupat':
        st.title('Hitung Keliling Belah Ketupat')

        sisi = st.number_input("Masukan Nilai Sisi", 0)

        if st.button("Hitung Keliling Belah Ketupat"):

            kel = 4 * sisi

            st.text(f"""
                    Rumusnya adalah *4 ✖ Sisi*
                    Cara menghitungnya adalah :
                    ({4} ✖ {sisi}""")
            st.success(f"Maka keliling belah ketupat adalah {kel:.2f} ✅")

# if __name__ == "__main__":
#     kelilingdatar_calculator()
