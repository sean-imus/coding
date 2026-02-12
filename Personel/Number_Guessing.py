import random

random_num = random.randint(0, 100)

while True:

    num = int(input("Wähle eine Zahl zwischen 0 und 100: "))

    if num > random_num:
        print("Zu hoch, versuche es erneut!")

    elif num == random_num:
        print("\nGenau richtig!")
        break

    else:
        print("Zu niedrig, versuche es erneut!")
