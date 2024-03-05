import random

n = 10  # počet pokusů (zápasů na jeden ticket)
k = 7   # minimální počet úspěchů

lower_bound = 1
upper_bound = 2
n_simulaci = 100000 # Počet simulací

zobrazit_data = False # Zobrazit data

def random_ticket():
    """
    Reprezentuje ticket n zápasů uživatele.
    Generuje náhodné čísla mezi dolní a horní hranicí (včetně).

    Tato funkce je určena pro simulaci náhodného výsledku zápasu.
    Výsledek zápasu je reprezentován číslem: 1 pro výhru domácího týmu,
    2 pro remízu a 3 pro výhru hostujícího týmu.

    Výstup:
    Seznam náhodně vygenerovaných celých čísel mezi dolní a horní hranicí (včetně).

    """
    ticket = []
    for pokus in range(n):
        pokus = random.randint(lower_bound, upper_bound)
        ticket.append(pokus)
    return ticket

def generate_multiple_tickets():
    """
    Vytvoří list x ticketů reprezentující uživatele.

    Výstup:
    Seznam náhodných výsledků n zápasů pro n_simulaci uživatelů.
    """
    multiple_tickets = []
    for i in range(n_simulaci):
        multiple_tickets.append(random_ticket())
    return multiple_tickets

def calculate_successes(multiple_tickets):
    """
    Spočítá počet úspěchů pro každý ticket.

    Výstup:
    Seznam počtu úspěchů pro každý ticket.
    """
    successes = []
    for ticket in multiple_tickets:
        success = ticket.count(1)
        successes.append(success)
    return successes


def calculate ():
    multiple_tickets = generate_multiple_tickets()
    successes = calculate_successes(multiple_tickets)
    total_n_tickets = len(successes) #Počet ticketů
    winning_tickets = [ticket for ticket in successes if ticket >= k] #Počet ticketů s úspěchem

    if zobrazit_data:
        print(f"multiple_tickets: {multiple_tickets}")
        print(f"successes: {successes}")

    print("-----------------------------")
    print(f"celkový počet ticketů: {total_n_tickets}")
    print("-----------------------------")
    print(f"Počet výherních ticketů: {len(winning_tickets)}")
    print("-----------------------------")
    print(f"Pravděpodobnost výhry: {len(winning_tickets)/total_n_tickets:.2%}")
    print("-----------------------------")
    print(f"Pravděpodobnost ve 2 kolech: {(len(winning_tickets)/total_n_tickets)**2:.3%}")
    print("-----------------------------")
    print(f"Pravděpodobnost ve 3 kolech: {(len(winning_tickets)/total_n_tickets)**3:.4%}")
    print("-----------------------------")
    print(f"Pravděpodobnost ve 4 kolech: {(len(winning_tickets)/total_n_tickets)**4:.4%}")



calculate()


