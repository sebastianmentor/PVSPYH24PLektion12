class Djur:
    def __init__(self, namn):
        self.namn = namn

    def prata(self):
        print(f"{self.namn} gör ett ljud.")

class Hund(Djur):  # Hund ärver från Djur
    def prata(self):
        print(f"{self.namn} skäller.")


class Katt(Djur):
    def __init__(self, namn, färg):
        super().__init__(namn)  # Anropar basklassens __init__
        self.färg = färg

    def prata(self):
        super().prata()  # Anropar basklassens prata-metod
        print(f"{self.namn} jamar.")
