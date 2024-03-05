from math import comb

# Parametry
n = 10  # počet pokusů (zápasů)
k = 7   # minimální počet úspěchů
p = 1/2 # pravděpodobnost úspěchu pro jeden pokus

# Výpočet pravděpodobnosti
pravdepodobnost = sum([comb(n, x) * (p ** x) * ((1 - p) ** (n - x)) for x in range(k, n+1)])

print("-----------------------------")
print(f"Pravděbodobnost: {pravdepodobnost:.3%}")
print("-----------------------------")
print(f"Pravděpodobnost ve 2 kolech: {(pravdepodobnost)**2:.4%}")
print("-----------------------------")
print(f"Pravděpodobnost ve 3 kolech: {(pravdepodobnost)**3:.4%}")
print("-----------------------------")
print(f"Pravděpodobnost ve 4 kolech: {(pravdepodobnost)**4:.4%}")
print("-----------------------------")