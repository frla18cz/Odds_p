import streamlit as st
from math import comb
from fractions import Fraction
import pandas as pd
def change_p():
    # Získáme hodnotu p z session_state
    p = st.session_state['p']
    decimal_odds = 1 / p
    fractional_odds = Fraction(decimal_odds - 1).limit_denominator()
    output_placeholder.markdown(f"""
    - Pravděpodobnost úspěchu pro jeden pokus byla změněna na: `{p:.2f}`
    - Kurz ve formátu desetinných čísel: `{decimal_odds:.2f}`
    - Kurz ve formátu zlomků: `{fractional_odds}`
    """)

p = st.session_state.get('p', 0.5)

st.title('Odhad pravděpodobnosti')
st.divider()
st.subheader('Pravděpodobnosti')
n = st.number_input('Počet zápasů', min_value=1, max_value=100, value=10, step=1)
k = st.number_input('Minimální počet úspěchů', min_value=1, max_value=100, value=9, step=1)
output_placeholder = st.empty()
if 'p' not in st.session_state:
    st.session_state['p'] = 0.5
p = st.number_input('Pravděpodobnost úspěchu pro jeden pokus', min_value=0.01, max_value=1.0, value=st.session_state['p'], step=0.01, key='p', on_change=change_p())



st.divider()
# st.subheader('Finance')
#
# vyplata_vyhry = st.number_input('Výplata výhry', value=100000, step=1000)
# poplatek_uzivatele = st.number_input('Poplatek uživatele', value=1000, step=100)


# Výpočet pravděpodobnosti
if st.button('Vypočítat'):
    pravdepodobnost = sum([comb(n, x) * (p ** x) * ((1 - p) ** (n - x)) for x in range(k, n+1)])
    pravdepodobnost_v_1_kole = pravdepodobnost
    pravdepodobnost_ve_2_kolech = pravdepodobnost ** 2
    pravdepodobnost_ve_3_kolech = pravdepodobnost ** 3
    pravdepodobnost_ve_4_kolech = pravdepodobnost ** 4

    # cashflow_1 = vyplata_vyhry * pravdepodobnost_v_1_kole


    pravdepodobnost_v_1_kole = "{:.3%}".format(pravdepodobnost)
    pravdepodobnost_ve_2_kolech = "{:.3%}".format(pravdepodobnost ** 2)
    pravdepodobnost_ve_3_kolech = "{:.3%}".format(pravdepodobnost ** 3)
    pravdepodobnost_ve_4_kolech = "{:.3%}".format(pravdepodobnost ** 4)


    # Vytvoření tabulky
    data = {
        'Počet kol': [1, 2, 3, 4],
        'Pravděpodobnost': [pravdepodobnost_v_1_kole, pravdepodobnost_ve_2_kolech, pravdepodobnost_ve_3_kolech, pravdepodobnost_ve_4_kolech]
    }
    tabulka = pd.DataFrame(data)
    st.table(tabulka)