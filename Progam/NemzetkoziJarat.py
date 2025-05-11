# Nemzetközi járatokra vonatkozó osztály, magasabb jegyárakkal.
from Jarat import Jarat
from datetime import datetime

class NemzetkoziJarat(Jarat):
    def __init__(self, jaratszam: str, indulas: datetime, celallomas: str, alap_ar: float):
        super().__init__(jaratszam, indulas, celallomas, alap_ar)
        self.extra = 10000  # Vámkezelés

    def jegy_ar_szamitas(self):
        return self.alap_ar + self.extra