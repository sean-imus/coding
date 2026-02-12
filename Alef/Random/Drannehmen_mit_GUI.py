import tkinter

# Klasse für das Klassenbuch
class Klassenbuch:
    def __init__(self, gesamt_schueler):
        self.gesamt_schueler = gesamt_schueler

    def berechne_index(self, zahl2):
        return zahl2 % self.gesamt_schueler + 1

# Funktion zum Berechnen und Anzeigen des Ergebnisses
def berechne_index():
    anzahl_schueler = int(eingabe_anzahl_schueler.get())
    zahl = int(eingabe_zahl.get())
    kb = Klassenbuch(anzahl_schueler)
    ergebnis_label["text"] = kb.berechne_index(zahl)

# GUI-Fenster initialisieren
fenster = tkinter.Tk()

# Eingabefelder
tkinter.Label(fenster, text="Anzahl der Schüler").pack()
eingabe_anzahl_schueler = tkinter.Entry(fenster)
eingabe_anzahl_schueler.pack()

tkinter.Label(fenster, text="Zahl zwischen 1.000 & 10.000").pack()
eingabe_zahl = tkinter.Entry(fenster)
eingabe_zahl.pack()

# Button zum Berechnen
tkinter.Button(fenster, text="Index berechnen", command=berechne_index).pack()

# Label für das Ergebnis
ergebnis_label = tkinter.Label(fenster, text="")
ergebnis_label.pack()

# GUI starten
fenster.mainloop()
