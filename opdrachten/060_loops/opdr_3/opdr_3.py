# Opdracht 3 input functie
# Naam student:
# Groep:

# Maak een lege lijst om de resultaten op te slaan
resultaten = []

# Loop van 3 tot 81, met stappen van 3
for i in range(3, 82, 3):
    waarde = (i ** 2) / 3  # Kwadraat nemen en delen door 3
    resultaten.append(waarde)  # Voeg de waarde toe aan de lijst

# Print de lijst met de juiste opmaak
print(resultaten)