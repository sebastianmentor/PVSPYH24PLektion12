class Polygon:
    def __init__(self, antal_sidor) -> None:
        self.antal_sidor = antal_sidor
        self._hemlighet1 = "Hemlighet 1"
        self.__hemlighet2 = "Hemlighet 2"

    def _get_hemlighet(self):
        return self.__hemlighet2    

class Rektangel(Polygon):
    def __init__(self, längd,höjd) -> None:
        self.längd = längd
        self.höjd = höjd        
        super().__init__(antal_sidor=4)

    def area(self):
        return self.längd * self.höjd

class Triangel(Polygon):
    def __init__(self, sida1, sida2, sida3) -> None:
        self.sida1 = sida1
        self.sida2 = sida2
        self.sida3 = sida3
        super().__init__(antal_sidor=3)

    def area(self):
        # Herons formula
        ...

class Kvadrat(Rektangel):
    def __init__(self, sidlängd) -> None:
        super().__init__(sidlängd, sidlängd)

    def get_hemlighet(self):
        return super()._get_hemlighet()



rekt1 = Rektangel(4, 6)
rekt2 = Rektangel(1, 2)
kvad1 = Kvadrat(5)

print(f"{isinstance(kvad1, Kvadrat)=}")
print(f"{isinstance(kvad1, Rektangel)=}")
print(f"{isinstance(kvad1, Polygon)=}")
print("#"*30)
print(f"{isinstance(rekt1, Kvadrat)=}")
print(f"{isinstance(rekt1, Rektangel)=}")
print(f"{isinstance(rekt1, Polygon)=}")
print("#"*30)
print(rekt1._hemlighet1)
print(rekt2._hemlighet1)
print(kvad1._hemlighet1)
print(kvad1.get_hemlighet())
