# (absztrakt osztály):** Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).

from abc import ABC, abstractmethod
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam: str, indulas: datetime, celallomas: str, alap_ar: float):
        self.jaratszam = jaratszam
        self.indulas = indulas
        self.celallomas = celallomas
        self.alap_ar = alap_ar

    @abstractmethod
    def jegy_ar_szamitas(self) -> float:
        pass

    def __str__(self):
        return f"{self.jaratszam}: {self.indulas.strftime('%Y-%m-%d %H:%M')} - {self.celallomas}"

