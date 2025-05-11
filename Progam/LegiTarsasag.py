# Tartalmazza a járatokat és saját attribútumot, mint például a légitársaság neve.
# from OOO_proj.Jarat import Jarat

from Jarat import Jarat

class LegiTarsasag:
    def __init__(self, legitarsasag_neve):
        self.legitarsasag_neve = legitarsasag_neve
        self.jaratok = []
        self.foglalasok = []

    def jarat_hozzaad(self, jarat: Jarat):
        self.jaratok.append(jarat)

    def jarat_keres(self, jaratszam: str) -> Jarat:
        for jarat in self.jaratok:
            if jarat.jaratszam == jaratszam:
                return jarat
        return None


