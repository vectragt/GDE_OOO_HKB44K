# (absztrakt osztály):** Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).

from abc import ABC, abstractmethod
from datetime import datetime

# (absztrakt osztály): Definiálja a járat alapvető attribútumait (járatszám, célállomás, jegyár).

from abc import ABC, abstractmethod
from datetime import datetime

class Jarat(ABC):
    def __init__(self, jaratszam: str, indulas: datetime, celallomas: str, alap_ar: float):
        self._jaratszam = jaratszam
        self._indulas = indulas
        self._celallomas = celallomas
        self._alap_ar = alap_ar

    # Járatszám getter/setter
    @property
    def jaratszam(self):
        return self._jaratszam

    @jaratszam.setter
    def jaratszam(self, value):
        if not value:
            raise ValueError("A járatszám nem lehet üres.")
        self._jaratszam = value

    # Indulás dátuma getter/setter
    @property
    def indulas(self):
        return self._indulas

    @indulas.setter
    def indulas(self, value):
        if not isinstance(value, datetime):
            raise ValueError("Az indulás csak datetime lehet.")
        self._indulas = value

    # Célállomás getter/setter
    @property
    def celallomas(self):
        return self._celallomas

    @celallomas.setter
    def celallomas(self, value):
        if not value:
            raise ValueError("A célállomás nem lehet üres.")
        self._celallomas = value

    # Alap ár getter/setter
    @property
    def alap_ar(self):
        return self._alap_ar

    @alap_ar.setter
    def alap_ar(self, value):
        if value < 0:
            raise ValueError("Az alapár nem lehet negatív.")
        self._alap_ar = value

    # Absztrakt metódus
    @abstractmethod
    def jegy_ar_szamitas(self) -> float:
        pass

    def __str__(self):
        return f"{self.jaratszam}: {self.indulas.strftime('%Y-%m-%d %H:%M')} - {self.celallomas}"
