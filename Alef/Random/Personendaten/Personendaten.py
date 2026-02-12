# Klasse & Liste erstellen

class Personen:
    def __init__(self, vorname, nachname, alter):
        self.vorname = vorname
        self.nachname = nachname
        self.alter = alter

    def geburtstag(self):
        self.alter += 1

    def report(self):
        return f"{self.vorname} {self.nachname}, {self.alter}"

personen = []

# Funktionen
def addieren():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    alter = int(input("Alter: "))
    personen.append(Personen(vorname, nachname, alter))
    print("\nPerson erfolgreich hinzugefügt!")

def report():
    for i, p in enumerate(personen):
        print(f"\n{i+1}. {p.report()}")

def entfernen():
    report()
    if personen:
        num = int(input("Nummer: ")) - 1
        if 0 <= num < len(personen):
            personen.pop(num)
            print("\nPerson erfolgreich entfernt!")

def geburtstag():
    report()
    if personen:
        num = int(input("Nummer: ")) - 1
        if 0 <= num < len(personen):
            personen[num].geburtstag()
            print("\nPerson hatte einen erfolgreichen Geburtstag!")

# Menü
while True:
    print("\n1. Person hinzufügen" +
        "\n2. Personen anzeigen" +
        "\n3. Person entfernen" +
        "\n4. Person hatte Geburstag" +
        "\n5. Programm beenden")
    wahl = input("Wahl: ")

    if wahl == "1":
        addieren()
    elif wahl == "2":
        report()
    elif wahl == "3":
        entfernen()
    elif wahl == "4":
        geburtstag()
    elif wahl == "5":
        break
