# Opdracht 4 condities
# Naam student:
# Groep:

toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = ['olijven', 'kaas', 'salami', 'pepperoni', 'ansjovis']

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

for topping, prijs in toppings:
    if keuze.lower() == topping.lower():  # Zorg ervoor dat de hoofdletters geen invloed hebben
        print(f"U heeft {topping} besteld. Dat kost {prijs}")
        break
else:
    print("Deze topping is niet beschikbaar. Kies een van de beschikbare toppings.")