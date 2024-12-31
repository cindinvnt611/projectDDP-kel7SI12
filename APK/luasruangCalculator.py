import streamlit as st
import math
from streamlit_option_menu import option_menu

def luasruang_calculator():
    with st.sidebar:
        selected = option_menu('Pilih Bangun Ruang',
                            ['Hitung Luas Kubus',
                                'Hitung Luas Balok',
                                'Hitung Luas Tabung',
                                'Hitung Luas Kerucut'],
                            default_index=0)

    
    if selected == "Hitung Luas Kubus":
        st.title('Hitung Luas Kubus')

        sisi = st.number_input("Panjang Sisi", 0)
        
        if st.button("Hitung Luas Permukaan"):

            luas = 6 * (sisi ** 2)

            st.text(f"""
                    Rumusnya adalah *6 ✖ (Sisi^2)*
                    Cara menghitungnya adalah :
                    ({5} ✖ {sisi ** 2})""")
            st.success(f"Maka luas kubusnya adalah {luas:.2f} ✅")
    
    elif selected == "Hitung Luas Balok":
        st.title('Hitung Luas Balok')

        panjang = st.number_input("Panjang", 0)
        lebar = st.number_input("Lebar", 0)
        tinggi = st.number_input("Tinggi", 0)
        
        if st.button("Hitung Luas Permukaan"):

            luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

            st.text(f"""
                    Rumusnya adalah *Panjang ✖ Lebar + Panjang ✖ Tinggi + Lebar ✖ Tinggi*
                    Cara menghitungnya adalah :
                    ({panjang} ✖ {lebar} + {panjang} ✖ {tinggi} + {lebar} ✖ {tinggi})""")
            st.success(f"Maka luas baloknya adalah {luas:.2f} ✅")
    
    elif selected == "Hitung Luas Tabung":
        st.title('Hitung Luas Tabung')

        jari_jari = st.number_input("Jari-jari", 0)
        tinggi = st.number_input("Tinggi", 0)
        
        if st.button("Hitung Luas Permukaan"):

            luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)

            st.text(f"""
                    Rumusnya adalah *2 ✖ 22/7 ✖ Jari-jari ✖ (Jari-jari + Tinggi)*
                    Cara menghitungnya adalah :
                    ({2} ✖ {math.pi} ✖ {jari_jari} ✖ ({jari_jari + tinggi}))""")
            st.success(f"Maka luas tabungnya adalah {luas:.2f} ✅")
    
    elif selected == "Hitung Luas Kerucut":
        st.title('Hitung Luas Kerucut')

        jari_jari = st.number_input("Jari-jari", 0)
        sisi_miring = st.number_input("Sisi Miring", 0)
        
        if st.button("Hitung Luas Permukaan"):

            luas = math.pi * jari_jari * (jari_jari + sisi_miring)

            st.text(f"""
                    Rumusnya adalah *22/7 ✖ Jari-jari ✖ (Jari-jari + Sisi miring)*
                    Cara menghitungnya adalah :
                    ({math.pi} ✖ {jari_jari} ✖ ({jari_jari + sisi_miring}))""")
            st.success(f"Maka luas kerucutnya adalah {luas:.2f} ✅")

# import math
# import streamlit as st
# from streamlit_option_menu import option_menu

# if test2 == "Luas Permukaan Bangun Ruang":
#             luasruang_calculator()

# def luasruang_calculator():
#     with st.sidebar:
#         selected = option_menu('Pilih Bangun Ruang',
#                             ['Hitung Luas Kubus',
#                                 'Hitung Luas Balok',
#                                 'Hitung Luas Tabung',
#                                 'Hitung Luas Kerucut'],
#                             default_index=0)

    
#     if selected == "Hitung Luas Kubus":
#         st.title('Hitung Luas Kubus')

#         sisi = st.number_input("Panjang Sisi", 0)
        
#         if st.button("Hitung Luas Permukaan"):

#             luas = 6 * (sisi ** 2)

#             st.text(f"""
#                     Rumusnya adalah *6 ✖ (Sisi^2)*
#                     Cara menghitungnya adalah :
#                     ({5} ✖ {sisi ** 2})""")
#             st.success(f"Maka luas kubusnya adalah {luas:.2f} ✅")
    
#     elif selected == "Hitung Luas Balok":
#         st.title('Hitung Luas Balok')

#         panjang = st.number_input("Panjang", 0)
#         lebar = st.number_input("Lebar", 0)
#         tinggi = st.number_input("Tinggi", 0)
        
#         if st.button("Hitung Luas Permukaan"):

#             luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

#             st.text(f"""
#                     Rumusnya adalah *Panjang ✖ Lebar + Panjang ✖ Tinggi + Lebar ✖ Tinggi*
#                     Cara menghitungnya adalah :
#                     ({panjang} ✖ {lebar} + {panjang} ✖ {tinggi} + {lebar} ✖ {tinggi})""")
#             st.success(f"Maka luas baloknya adalah {luas:.2f} ✅")
    
#     elif selected == "Hitung Luas Tabung":
#         st.title('Hitung Luas Tabung')

#         jari_jari = st.number_input("Jari-jari", 0)
#         tinggi = st.number_input("Tinggi", 0)
        
#         if st.button("Hitung Luas Permukaan"):

#             luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)

#             st.text(f"""
#                     Rumusnya adalah *2 ✖ 22/7 ✖ Jari-jari ✖ (Jari-jari + Tinggi)*
#                     Cara menghitungnya adalah :
#                     ({2} ✖ {math.pi} ✖ {jari_jari} ✖ ({jari_jari + tinggi}))""")
#             st.success(f"Maka luas tabungnya adalah {luas:.2f} ✅")
    
#     elif selected == "Hitung Luas Kerucut":
#         st.title('Hitung Luas Kerucut')

#         jari_jari = st.number_input("Jari-jari", 0)
#         sisi_miring = st.number_input("Sisi Miring", 0)
        
#         if st.button("Hitung Luas Permukaan"):

#             luas = math.pi * jari_jari * (jari_jari + sisi_miring)

#             st.text(f"""
#                     Rumusnya adalah *22/7 ✖ Jari-jari ✖ (Jari-jari + Sisi miring)*
#                     Cara menghitungnya adalah :
#                     ({math.pi} ✖ {jari_jari} ✖ ({jari_jari + sisi_miring}))""")
#             st.success(f"Maka luas kerucutnya adalah {luas:.2f} ✅")

# if __name__ == "__main__":
#     luasruang_calculator()