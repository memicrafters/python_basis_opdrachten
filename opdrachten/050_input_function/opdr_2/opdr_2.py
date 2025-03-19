# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Paul", "Kees", "Marie", "Hilda"]
gasten.insert(0, "Michel")  # Voeg jezelf toe aan het begin
print(gasten)  # Verwachte output: ["Michel", "Paul", "Kees", "Marie", "Hilda"]

# Stap 2: Marie belt af
gasten.remove("Marie")
print(gasten)  # Verwachte output: ["Michel", "Paul", "Kees", "Hilda"]

# Stap 3: George wil naast Kees zitten
index_kees = gasten.index("Kees")  # Zoek de index van Kees
gasten.insert(index_kees + 1, "George")  # Voeg George toe naast Kees
print(gasten)  # Verwachte output: ["Michel", "Paul", "Kees", "George", "Hilda"]