class Hjul:
    def __init__(self, diameter):
        self.diameter = diameter

class Bil:
    def __init__(self, modell):
        self.modell = modell
        self.hjul = []

    def lagg_till_hjul(self, hjul):
        self.hjul.append(hjul)

# Skapa objekt
hjul1 = Hjul(17)
hjul2 = Hjul(17)
bil1 = Bil("Volvo")

# Lägga till hjul till bilen
bil1.lagg_till_hjul(hjul1)
bil1.lagg_till_hjul(hjul2)

print(f"{bil1.modell} har hjul med diameter: {[hjul.diameter for hjul in bil1.hjul]}")





class Spelare:
    def __init__(self, namn):
        self.namn = namn

class Team:
    def __init__(self, namn):
        self.namn = namn
        self.spelare = []

    def lägg_till_spelare(self, spelare):
        self.spelare.append(spelare)

# Skapa spelare
spelare1 = Spelare("Leo")
spelare2 = Spelare("Mia")

# Skapa team och lägg till spelare
team = Team("Tigrarna")
team.lägg_till_spelare(spelare1)
team.lägg_till_spelare(spelare2)

# Visa teamets spelare
print(f"Team {team.namn} har spelarna:")
for s in team.spelare:
    print(s.namn)


class Universitet:
    def __init__(self, namn):
        self.namn = namn
        self.fakulteter = []

    def lägg_till_fakultet(self, fakultet):
        self.fakulteter.append(fakultet)

class Fakultet:
    def __init__(self, namn):
        self.namn = namn

# Skapa instanser
universitet = Universitet("Uppsala Universitet")
fakultet1 = Fakultet("Teknisk Fakultet")
fakultet2 = Fakultet("Medicinsk Fakultet")

# Lägg till fakulteter till universitetet
universitet.lägg_till_fakultet(fakultet1)
universitet.lägg_till_fakultet(fakultet2)
