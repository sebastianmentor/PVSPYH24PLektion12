class Kapitel:
    def __init__(self, namn):
        self.namn = namn

class Bok:
    def __init__(self, titel):
        self.titel = titel
        self.kapitel = []

    def lagg_till_kapitel(self, namn):
        nytt_kapitel = Kapitel(namn)
        self.kapitel.append(nytt_kapitel)

# Skapa objekt
bok1 = Bok("Lär dig Python")
bok1.lagg_till_kapitel("Introduktion")
bok1.lagg_till_kapitel("Grunder")

print(f"Boken '{bok1.titel}' har kapitel: {[kapitel.namn for kapitel in bok1.kapitel]}")



class Motor:
    def __init__(self, typ):
        self.typ = typ

class Bil:
    def __init__(self, modell):
        self.modell = modell
        self.motor = Motor("V8")

    def visa_info(self):
        print(f"{self.modell} har en {self.motor.typ}-motor.")

# Skapa bil
bil = Bil("Mustang")
bil.visa_info()
