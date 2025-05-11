# ## Funkciók
#
# - **Jegy foglalása:** A járatokra jegyet lehet foglalni, és visszaadja a foglalás árát.
# - **Foglalás lemondása:** A felhasználó lemondhatja a meglévő foglalást.
# - **Foglalások listázása:** Az összes aktuális foglalás listázása.
#
# ## Adatvalidáció
#
# - Ellenőrzi, hogy a járat elérhető-e foglalásra, és hogy a foglalás időpontja érvényes-e.
# - Biztosítja, hogy csak létező foglalásokat lehessen lemondani.
#
# ## Felhasználói interfész
#
# - Egyszerű felhasználói interfész, amely lehetővé teszi a következő műveleteket:
#   - Jegy foglalása
#   - Foglalás lemondása
#   - Foglalások listázása
#
# ## Előkészítés
#
# A rendszer indulásakor egy légitársaság, 3 járat és 6 foglalás előre be van töltve a rendszerbe, így a felhasználó azonnal használatba veheti a rendszert.

from datetime import datetime, timedelta
from LegiTarsasag import LegiTarsasag
# from Jarat import Jarat
from BelfoldiJarat import BelfoldiJarat
from JegyFoglalas import JegyFoglalas
from NemzetkoziJarat import NemzetkoziJarat


class FoProgram:
    def __init__(self):

        self.legitarsasag = LegiTarsasag("GDE AirLines")
        self._init_adatok()

    def _init_adatok(self):
        # Kezdő adatok
        # from datetime import datetime, timedelta

        # Járatok hozzáadása
        ma = datetime.now()

        self.legitarsasag.jarat_hozzaad(BelfoldiJarat("BJ101", ma + timedelta(days=1), "Debrecen", 12050.0))
        self.legitarsasag.jarat_hozzaad(BelfoldiJarat("BJ102", ma + timedelta(days=1), "Mezőkövesd", 12050.0))
        self.legitarsasag.jarat_hozzaad(NemzetkoziJarat("NJ201", ma + timedelta(days=2), "London", 62220.0))


        # Példa foglalások
        self.foglalas_letrehozasa("BJ101", "Kiss János", ma)
        self.foglalas_letrehozasa("BJ101", "Nagy Éva", ma)
        self.foglalas_letrehozasa("BJ102", "Kovács Péter", ma)
        self.foglalas_letrehozasa("BJ102", "Tóth Anna", ma)
        self.foglalas_letrehozasa("NJ201", "Szabó Gábor", ma)
        self.foglalas_letrehozasa("NJ201", "Horváth Zsuzsa", ma)

    def foglalas_letrehozasa(self, jaratszam: str, utas_neve: str, foglalas_datuma: datetime) -> bool:
        jarat = self.legitarsasag.jarat_keres(jaratszam)

        if not jarat:
            print("Hiba: Nem létező járat!")
            return False

        if foglalas_datuma > jarat.indulas:
            print("Hiba: A foglalás dátuma nem lehet később, mint a járat indulási dátuma!")
            return False

        foglalas = JegyFoglalas(jarat, utas_neve, foglalas_datuma)
        self.legitarsasag.foglalasok.append(foglalas)
        print(f"Sikeres foglalás! Foglalási szám: {foglalas.foglalas_szam}")
        return True

    def foglalas_lemondasa(self, foglalas_szam: str) -> bool:
        for i, foglalas in enumerate(self.legitarsasag.foglalasok):
            if foglalas.foglalas_szam == foglalas_szam:
                self.legitarsasag.foglalasok.pop(i)
                print("Sikeres lemondás!")
                return True
        print("Hiba: Nem található ilyen foglalás!")
        return False

    def foglalasok_listazasa(self):
        if not self.legitarsasag.foglalasok:
            print("Nincsenek foglalások.")
            return

        print("\nÖsszes foglalás:")
        for foglalas in self.legitarsasag.foglalasok:
            print(foglalas)


    #@staticmethod
    def felhasznaloi_interfesz(self):

        while True:
            print("\nFőmenü\n")
            print("1. Járatok listázása")
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Foglalások listázása")
            print("5. Kilépés")

            valasztas = int(input("Válasszon egy menüpontot (1-5): "))

            if valasztas == 1:
                print("\nElérhető járatok:")
                for jarat in rendszer.legitarsasag.jaratok:
                    print(f"{jarat} - {jarat.jegy_ar_szamitas():.2f} Ft")

            elif valasztas == 2:
                jaratszam = input("Járatszám: ")
                utas_neve = input("Utas neve: ")
                rendszer.foglalas_letrehozasa(jaratszam, utas_neve, datetime.now())

            elif valasztas == 3:
                foglalas_szam = input("Kérem adja meg a sorszámát amit le szeretne mondani: ")
                rendszer.foglalas_lemondasa(foglalas_szam)

            elif valasztas == 4:
                rendszer.foglalasok_listazasa()

            elif valasztas == 5:
                print("Kilépés...")
                break

            else:
                print("Hibás választás!")


if __name__ == "__main__":
    JegyFoglalas.sorszam = 1
    rendszer = FoProgram()
    rendszer.felhasznaloi_interfesz()