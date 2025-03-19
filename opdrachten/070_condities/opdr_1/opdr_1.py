# Opdracht 1 condities
# Naam student:
# Groep:

# Maak een lege lijst
getallen = []

# Vul de lijst met getallen van 1 t/m 10
for i in range(1, 11):
    getallen.append(i)

# Maak een nieuwe lijst met getallen die groter zijn dan 4
groter_dan_vier = [nummer for nummer in getallen if nummer > 4]

# Print de lijst van getallen groter dan 4
print(groter_dan_vier)
