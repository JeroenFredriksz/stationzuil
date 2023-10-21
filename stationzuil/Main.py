import DatabaseEditor
import datetime

import StationsManager


def voerGegevensInGebruiker():
    randomStation = StationsManager.RandomStation()
    tijd = datetime.datetime.now()

    while True:
        naam = input("Wat is uw naam?\n"
                     ": ")
        if(len(naam) <= 50 and len(naam) > 1):
            break

    while True:
        bericht = input("Wat voor bericht wilt u meegeven?\n"
                        "Maximaal 140 karakters.\n"
                        ": ")
        if(len(bericht) <= 140):
            break
    DatabaseEditor.inputDatabase(bericht, tijd, naam, randomStation)


voerGegevensInGebruiker()