# A járatok foglalásához szükséges osztály, amely egy utazásra szóló jegy foglalását tárolja.

from Jarat import Jarat
from datetime import datetime

class JegyFoglalas:
    sorszam = 1
    def __init__(self, jarat: Jarat, utas_neve: str, foglalas_datuma: datetime):
        self.jarat = jarat
        self.utas_neve = utas_neve
        self.foglalas_datuma = foglalas_datuma
        self.foglalas_ara = jarat.jegy_ar_szamitas()
        self.foglalas_szam = f"{JegyFoglalas.sorszam}"  # sorszám
        JegyFoglalas.sorszam += 1
    def __str__(self):
        return (f"Foglalás {self.foglalas_szam} - Utas: {self.utas_neve} | Járat: {self.jarat} | Foglalás dátuma: {self.foglalas_datuma.strftime('%Y-%m-%d %H:%M')} | Ár: {self.foglalas_ara} Ft")
