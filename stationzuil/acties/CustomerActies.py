import datetime

from stationzuil.util import StationsManager


def voerGegevensInGebruiker():
    randomStation = StationsManager.RandomStation()
    tijd = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

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