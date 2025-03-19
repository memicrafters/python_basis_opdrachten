# Opdracht 3 condities
# Naam student:
# Groep:

# Normale toegangsprijs
normale_prijs = 12.5

# Vraag de leeftijd van de bezoeker
leeftijd = int(input("Geef uw leeftijd in aantal jaar: "))  # Zorg ervoor dat je dit precies zo schrijft

# Bereken de korting en geef de bijbehorende groep en prijs
if leeftijd < 3:
    korting = 100  # Baby's krijgen 100% korting
    groep = "baby"
elif 3 <= leeftijd <= 18:
    korting = 50  # Kinderen krijgen 50% korting
    groep = "kinderen"
elif 19 <= leeftijd <= 64:
    korting = 0  # Volwassenen krijgen geen korting
    groep = "volwassenen"
else:
    korting = 30  # Ouderen krijgen 30% korting
    groep = "ouderen"

# Bereken de uiteindelijke prijs na de korting
te_betalen = normale_prijs * (1 - korting / 100)

# Print het resultaat
print(f"U behoort tot de groep {groep}")
print(f"U krijgt {korting}% korting")
print(f"U betaalt daarom {te_betalen}")