class Bankkonto:
    def __init__(self, kontonummer) -> None:
        self.kontonummer = kontonummer
        self._saldo = 0

    def get_saldo(self):
        return self._saldo
    
    def ta_ut_pengar(self):
        print("Tar ut från saldo!")

class Sparkonto(Bankkonto):
    def __init__(self, kontonummer, sparränta) -> None:
        self.sparränta = sparränta
        super().__init__(kontonummer)
    
    def årsränta(self):
        ...

class Lönekonto(Bankkonto):
    # finns __init__() <-- ??
    def autogiro(self):
        ...

class Kreditkonto(Bankkonto):
    def __init__(self, kontonummer, kredit, ränta) -> None:
        self.kredit = kredit
        self.ränta = ränta
        super().__init__(kontonummer)

    def ta_ut_pengar(self):
        # Implementera så att vi kan ta ut upp till vår kreditgräns men inte mer!!
        print("Tar ut på kredit")


spar = Sparkonto("1234", 0.04)
lön = Lönekonto("1111") # Lönekonto.__init__("1111")
kred = Kreditkonto("3333", 10000, 0.28)

print(f"{spar.kontonummer=}")
print(f"{lön.kontonummer=}")
print(f"{kred.kontonummer=}")

print(f"{spar.get_saldo()=}")
print(f"{lön.get_saldo()=}")
print(f"{kred.get_saldo()=}")

print(f"{spar.ta_ut_pengar()=}")
print(f"{lön.ta_ut_pengar()=}")
print(f"{kred.ta_ut_pengar()=}")

