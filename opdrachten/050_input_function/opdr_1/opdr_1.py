# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

import math

# Vraag de gebruiker om de lengtes van de rechthoekszijden
zijde_1 = float(input("Geef de lengte van de eerste zijde:4 "))  # Vraag de eerste zijde
zijde_2 = float(input("Geef de lengte van de tweede zijde:3 "))  # Vraag de tweede zijde

# Bereken de lengte van de schuine zijde met de stelling van Pythagoras
schuine_zijde = math.sqrt(zijde_1**2 + zijde_2**2)

# Print de lengte van de schuine zijde
print(f"De lengte van de schuine zijde is: {schuine_zijde}")