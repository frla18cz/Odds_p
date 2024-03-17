import streamlit as st
from math import comb, pow

def vypocet_pravdepodobnosti():
    pass


# # Streamlit uživatelské rozhraní
# st.title('Rozdělení po tiketech')
# st.subheader('uživatel musí tefit minimálně x tiketů')
#
# pocet_tiketu = st.number_input('Počet tiketů', min_value=1, value=4)
# pocet_zapasu_na_tiket = st.number_input('Počet zápasů na tiket', min_value=1, value=3)
# minimalni_pocet_spravnych_tiketu = st.number_input('Minimální počet správně tipnutých tiketů', min_value=1, value=3,
#                                                     max_value=pocet_tiketu)

simulate_x_times = 1000

pocet_tiketu = 1
kurz = 10
pocet_zapasu_na_tiket = 2
minimalni_pocet_spravnych_tiketu = 4

print(f"Počet tiketů: {pocet_tiketu}\nPočet zápasů na tiket: {pocet_zapasu_na_tiket}\nMinimální počet správně tipnutých tiketů: {minimalni_pocet_spravnych_tiketu}")


vsechny_pokusy = pow(kurz, pocet_zapasu_na_tiket)
print(f"Všechny možné pokusy: {vsechny_pokusy}")

p_spravny_tip = 1 / vsechny_pokusy
p_chybny_tip = 1 - p_spravny_tip
print(f"Pravděpodobnost správného tipu na jednom tiketu: {p_spravny_tip:.2%}")



