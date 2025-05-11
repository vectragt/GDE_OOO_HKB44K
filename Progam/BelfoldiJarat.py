# Belföldi járatokra vonatkozó osztály, amelyek olcsóbbak és rövidebbek.
from Jarat import Jarat
from datetime import datetime

class BelfoldiJarat(Jarat):
    def __init__(self, jaratszam: str, indulas: datetime, celallomas: str, alap_ar: float):
        super().__init__(jaratszam, indulas, celallomas, alap_ar)


    def jegy_ar_szamitas(self):
        return self.alap_ar

