# Opdracht 3 input functie
# Naam student:
# Groep:

# Startlijst met pizza's
pizzas = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Stap 1: Sorteer de lijst alfabetisch
pizzas.sort()
print(pizzas)  # Output: ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi']

# Stap 2: Voeg een pizza naar keuze toe
pizzas.append('Pepperoni')
print(pizzas)  # Output: ['calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi', 'Pepperoni']

# Stap 3: Verwijder de minst lekkere pizza
pizzas.remove('olivio')
print(pizzas)  # Output: ['calzone', 'margharita', 'quattro stagioni', 'verdi', 'Pepperoni']

# Stap 4: Print de eerste 3 pizza's
print(pizzas[:3])  # Output: ['calzone', 'margharita', 'quattro stagioni']

# Stap 5: Print de middelste pizza
midden_index = len(pizzas) // 2
print([pizzas[midden_index]])  # Output: ['quattro stagioni']

# Stap 6: Print de laatste 3 pizza's
print(pizzas[-3:])  # Output: ['quattro stagioni', 'verdi', 'Pepperoni']