# Opdracht 3 input functie
# Naam student:
# Groep:

# Vraag de gebruiker om een lijst met minimaal 5 objecten, gescheiden door komma's
items = input("Amsterdam, Zwolle, Dronten, Haarlem, Zaanstad")

# Zet de invoer om in een lijst en verwijder eventuele spaties rondom de items
lijst = [item.strip() for item in items.split(",")]

# Sorteer de lijst alfabetisch en draai de volgorde om
lijst.sort(reverse=True)

# Print de gesorteerde lijst
print(lijst)

