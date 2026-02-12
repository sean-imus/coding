import tkinter as tk

class Klassenbuch:
    def __init__(self, anzahl_schueler):
        self.anzahl_schueler = anzahl_schueler

    def schueler_wahl(self, zahl):
        return zahl % self.anzahl_schueler

anzahl = int(input("Schüler Anzahl?: "))
zahl = int(input("Zahl zwischen 1.000 und 10.000?: "))

kb = Klassenbuch(anzahl)
index = kb.schueler_wahl(zahl)

print(index)
