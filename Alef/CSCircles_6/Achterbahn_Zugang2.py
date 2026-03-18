# Eingabe & Auswertung Alter
age = int(input("Wie alt bist du? "))

if age >= 65:
    Grund = "Zu alt"

elif age < 16:
    Grund = "Zu jung"

else:
    korrektes_alter = "y"

# Eingabe Schwangerschaft
schwanger = input("Sind Sie schwanger? y/n ")

if (korrektes_alter == "y" and schwanger == "n"):
    print("Glückwunsch Sie haben das passende Alter und da Sie nicht schwanger sind düfen Sie mitfahren")

elif (korrektes_alter == "y" and schwanger == "y"):
    print("Sie haben zwar das richtige Alter, dürfen aber aufgrund Ihrer Schwangerschaft nicht mitfahren")

elif (korrektes_alter == "n" and schwanger == "n"):
    print("Du bist nicht schwanger und du bist zu jung für die Achterbahnfahrt")
