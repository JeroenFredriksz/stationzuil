import DatabaseEditor


def modereerBerichten():
    moderatorNaam = input("Wat is uw naam?\n"
                          ": ")
    moderatorEmail = input("Wat is uw email?\n"
                           ": ")

    lines = DatabaseEditor.readDatabase()

    for line in lines:
        splittedLines = line.split("/")
        naam = splittedLines[0]
        datum = splittedLines[1]
        bericht = splittedLines[2]
        station = splittedLines[3].strip()

        print(f"Het huidige bericht om te keuren is:\n"
              f'"{bericht}"\n'
              f'geschreven door {naam} op {datum} op station {station}\n\n'
              f'"wilt u dit bericht goedkeuren? antwoord "Ja" of "Nee"')

        # while loop zodat als moderator geen ja of nee opgeeft, het programma niet doorgaat met een ongeldig antwoord
        while True:
            keuring = input(": ").lower()
            if keuring == "ja" or keuring == "nee":
                break
            else:
                print('Dit is geen geldige invoer! Voer in "Ja" of "Nee"')
#             zo nee, gaat het terug naar vragen om keuring input


modereerBerichten()
