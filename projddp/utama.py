import streamlit as st
from home import display_home
from about import display_about
from team import display_team
from volumeCalculator import volume_calculator
from luasruangCalculator import luasruang_calculator
from luasdatarCalculator import luasdatar_calculator
from kelilingdatarCalculator import kelilingdatar_calculator
from perhitunganCalculator import perhitungan1_calculator
import login


def main():
    if 'is_login' not in st.session_state:
        st.session_state.is_login = False
    
    if not st.session_state.is_login :
        login.display_login()
        
    else:
        tab1, tab2, tab3, tab4 = st.tabs(['🏠Home', '🏢About Us', '👨‍👨‍👦‍👦Team', '📋Mari Menghitung'])

        with tab1:
            display_home()
        
        with tab2:
            display_about()
        
        with tab3:
            display_team()
        
        with tab4:
            st.logo(image="image/ngitung2.jpeg", size="large")
            test2 = st.sidebar.selectbox(
                "*Mari Menghitung*", 
                ['Volume Bangun Ruang', 'Luas Permukaan Bangun Ruang', 'Luas Bangun Datar', 
                "Keliling Bangun Datar", "Perhitungan Dasar"], 
                index=0
            )
            
            if test2 == "Volume Bangun Ruang":
                volume_calculator()
            elif test2 == "Luas Permukaan Bangun Ruang":
                luasruang_calculator()
            elif test2 == "Luas Bangun Datar":
                luasdatar_calculator()
            elif test2 == "Keliling Bangun Datar":
                kelilingdatar_calculator()
            elif test2 == "Perhitungan Dasar":
                perhitungan1_calculator()



if __name__ == "__main__":
    main()