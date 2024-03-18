import streamlit as st
from math import comb, pow
import random
def simulace_zapasu():
    """

    """
    match = []  # Initialize an empty list named match
    match = random.uniform(0, 1)  # Assign a random float number between 0 and 1 to match
    match_raw = []
    match_raw.append(f"Kurz: {match}") # Debug
    if match >= 1/kurz:
        match = 0
    else:
        match = 1


    print(match_raw)
    return match  # Return the value of match

def simulace_ticketu(pocet_zapasu_na_tiket):
    """
    This function simulates a ticket by calling the function simulace_zapasu() a given number of times.

    Args:
        pocet_zapasu_na_tiket (int): The number of matches on the ticket.

    Returns:
        list: A list of floats representing the outcomes of the matches on the ticket.
    """
    ticket = []  # Initialize an empty list named ticket
    for i in range(pocet_zapasu_na_tiket):  # Loop through the range of the number of matches on the ticket
        ticket.append(simulace_zapasu())  # Append the outcome of the match to the ticket
    return ticket  # Return the value of ticket

def simulace_eventu(pocet_zapasu_na_tiket, pocet_tiketu):
    """
    This function simulates a number of tickets by calling the function simulace_ticketu() a given number of times.

    Args:
        pocet_zapasu_na_tiket (int): The number of matches on the ticket.
        pocet_tiketu (int): The number of tickets.

    Returns:
        list: A list of lists of floats representing the outcomes of the matches on the tickets.
    """
    event = []  # Initialize an empty list named event
    for i in range(pocet_tiketu):  # Loop through the range of the number of tickets
        event.append(simulace_ticketu(pocet_zapasu_na_tiket))  # Append the ticket to the event
    return event  # Return the value of event

def simulace_monte_carlo():
    """
    This function simulates a Monte Carlo simulation by calling the function simulace_eventu() a given number of times.

    Returns:
        list: A list of lists of floats representing the outcomes of the matches on the tickets.
    """
    monte_carlo = []  # Initialize an empty list named monte_carlo
    for i in range(n_simulaci):  # Loop through the range of the number of simulations
        monte_carlo.append(simulace_eventu(pocet_zapasu_na_tiket, pocet_tiketu))  # Append the event to monte_carlo
    return monte_carlo  # Return the value of monte_carlo

def evaluate_simulation():
    """
    This function evaluates the results of a Monte Carlo simulation.

    It first generates a Monte Carlo simulation by calling the function simulace_monte_carlo().
    Then, for each event in the simulation, it calculates the success of each ticket in the event.
    If the success of a ticket equals the number of matches on the ticket, it appends 1 to the event result, otherwise it appends 0.
    Finally, it appends the event result to the overall result.

    Returns:
        list: A list of lists of integers representing the success of each ticket in each event of the simulation.
    """
    result = []  # Initialize an empty list named result
    monte_carlo = simulace_monte_carlo()  # Generate a Monte Carlo simulation

    for event in monte_carlo:  # Loop through each event in the simulation
        print(event)  # Print the event
        print(" ")  # Print a space for readability

    for event in monte_carlo:  # Loop through each event in the simulation
        event_result = []  # Initialize an empty list named event_result
        for ticket in event:  # Loop through each ticket in the event
            uspech_na_tiket = 0  # Initialize a variable for accumulation
            for zapas in ticket:  # Loop through each match in the ticket
                uspech_na_tiket += zapas  # Accumulate the success of the match
            if uspech_na_tiket == pocet_zapasu_na_tiket:  # If the success of the ticket equals the number of matches on the ticket
                event_result.append(1)  # Append 1 to the event result
            else:  # If the success of the ticket does not equal the number of matches on the ticket
                event_result.append(0)  # Append 0 to the event result

        result.append(event_result)  # Append the event result to the overall result
    return result  # Return the overall result

def vyhodnoceni():
    simulation = evaluate_simulation()
    pocet_uspechnych_eventu = 0
    for event in simulation:
        pocet_uspechnych_tiketu = 0
        for ticket in event:
            pocet_uspechnych_tiketu += ticket
        if pocet_uspechnych_tiketu >= minimalni_pocet_spravnych_tiketu:
            pocet_uspechnych_eventu += 1
    print(f"Event uspesny, uzivatel zvitezil: {pocet_uspechnych_eventu}")
    procento_uspescnyh_eventu = pocet_uspechnych_eventu / n_simulaci

    return procento_uspescnyh_eventu






# Streamlit uživatelské rozhraní
st.title('Rozdělení po tiketech - simulace')
st.subheader('uživatel musí tefit minimálně x tiketů')
st.subheader('Kontrolní výpočet pomocí monte carlo simulace')

n_simulaci = st.number_input('Počet simulací', min_value=1, value=10000)
kurz = st.number_input('Kurz', min_value=1, value=2)
pocet_tiketu = st.number_input('Počet tiketů', min_value=1, value=4)
pocet_zapasu_na_tiket = st.number_input('Počet zápasů na tiket', min_value=1, value=3)
minimalni_pocet_spravnych_tiketu = st.number_input('Minimální počet správně tipnutých tiketů', min_value=1, value=2)

# #Určeno k developmentu, dočasné variables
# n_simulaci = 10
# kurz = 2
# pocet_tiketu = 2
# pocet_zapasu_na_tiket = 1
# minimalni_pocet_spravnych_tiketu = 2


if st.button('Vypočítat pravděpodobnost'):
    vyhodnoceni = vyhodnoceni()
    st.write(f'Pravděpodobnost:  {vyhodnoceni():.4%}')


