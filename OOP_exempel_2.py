import math

# Basklass för alla fordon
class Fordon:
    def __init__(self, märke, modell, år):
        self.märke = märke
        self.modell = modell
        self.år = år

    def starta(self):
        print(f"{self.märke} {self.modell} startar.")

    def stanna(self):
        print(f"{self.märke} {self.modell} stannar.")

    def info(self):
        print(f"Fordon: {self.märke} {self.modell}, Årsmodell: {self.år}")

# Subklass för bilar
class Bil(Fordon):
    def __init__(self, märke, modell, år, antal_dörrar):
        super().__init__(märke, modell, år)  # Använder basklassens konstruktor
        self.antal_dörrar = antal_dörrar

    def info(self):
        super().info()  # Anropar basklassens info-metod
        print(f"Detta är en bil med {self.antal_dörrar} dörrar.")

    def tuta(self):
        print(f"{self.märke} {self.modell} tutar: Tuuut tuut!")

# Subklass för motorcyklar
class Motorcykel(Fordon):
    def __init__(self, märke, modell, år, typ_av_mc):
        super().__init__(märke, modell, år)  # Använder basklassens konstruktor
        self.typ_av_mc = typ_av_mc

    def info(self):
        super().info()  # Anropar basklassens info-metod
        print(f"Detta är en motorcykel av typen {self.typ_av_mc}.")

    def göra_hjulning(self):
        print(f"{self.märke} {self.modell} gör en hjulning!")

class TrikeBike(Bil, Motorcykel): # Dumt!!!
    def info(self):
        super().info()

# Subklass för elbilar, en specialisering av Bil
class Elbil(Bil):
    def __init__(self, märke, modell, år, antal_dörrar, batterikapacitet):
        super().__init__(märke, modell, år, antal_dörrar)  # Använder Bil-konstruktorn
        self.batterikapacitet = batterikapacitet  # Nytt attribut för batterikapacitet

    def info(self):
        super().info()  # Anropar Bil-klassens info-metod
        print(f"Detta är en elbil med en batterikapacitet på {self.batterikapacitet} kWh.")

    def ladda_batteri(self):
        print(f"{self.märke} {self.modell} laddar sitt batteri.")

# Exempel på användning av systemet

# Skapa en bil och en motorcykel
bil = Bil("Volvo", "XC60", 2021, 5)
motorcykel = Motorcykel("Harley-Davidson", "Street 750", 2020, "Cruiser")
elbil = Elbil("Tesla", "Model S", 2023, 4, 100)

# Använd metoderna
bil.starta()            # Volvo XC60 startar.
bil.tuta()              # Volvo XC60 tutar: Tuuut tuut!
bil.info()              # Volvo XC60 info, antal dörrar osv.

motorcykel.starta()      # Harley-Davidson Street 750 startar.
motorcykel.göra_hjulning() # Harley-Davidson Street 750 gör en hjulning!
motorcykel.info()        # Harley-Davidson Street 750 info, typ av motorcykel.

elbil.starta()           # Tesla Model S startar.
elbil.ladda_batteri()    # Tesla Model S laddar sitt batteri.
elbil.info()             # Tesla Model S info, batterikapacitet osv.

trik = TrikeBike
trik.info()