import datetime

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
        datetime.datetime.fromtimestamp(datum)
        bericht = splittedLines[2]
        station = splittedLines[3].strip()




modereerBerichten()
