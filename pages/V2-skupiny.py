import streamlit as st
from math import comb, pow


def vypocet_pravdepodobnosti(pocet_tiketu, pocet_zapasu_na_tiket, minimalni_pocet_spravnych_tiketu):
    # Pravděpodobnost správného tipu na jednom tiketu
    p_spravny_tip = 1 / pow(kurz, pocet_zapasu_na_tiket)
    # Pravděpodobnost špatného tipu na jednom tiketu
    p_chybny_tip = 1 - p_spravny_tip

    celkova_pravdepodobnost = 0

    # Výpočet celkové pravděpodobnosti pro všechny možné úspěšné scénáře
    for i in range(minimalni_pocet_spravnych_tiketu, pocet_tiketu + 1):
        p_tento_pripad = comb(pocet_tiketu, i) * pow(p_spravny_tip, i) * pow(p_chybny_tip, pocet_tiketu - i)
        celkova_pravdepodobnost += p_tento_pripad

    return celkova_pravdepodobnost


# Streamlit uživatelské rozhraní
st.title('Rozdělení po tiketech')
st.subheader('uživatel musí tefit minimálně x tiketů')
st.subheader('Přidána modifikace ke kurzu')

kurz = st.number_input('Kurz', min_value=1, value=2)
pocet_tiketu = st.number_input('Počet tiketů', min_value=1, value=4)
pocet_zapasu_na_tiket = st.number_input('Počet zápasů na tiket', min_value=1, value=3)
minimalni_pocet_spravnych_tiketu = st.number_input('Minimální počet správně tipnutých tiketů', min_value=1, value=2)



if st.button('Vypočítat pravděpodobnost'):
    pravdepodobnost = vypocet_pravdepodobnosti(pocet_tiketu, pocet_zapasu_na_tiket, minimalni_pocet_spravnych_tiketu)
    st.write(
        f'Pravděpodobnost:  {pravdepodobnost:.4%}')
    st.subheader('Chart!')

