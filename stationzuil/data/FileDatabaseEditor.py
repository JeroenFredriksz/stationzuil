
path = "C:/Users/Jeroen/PycharmProjects/stationzuil5/stationzuil/data/database.csv"

def inputDatabase(bericht, datumTijd, naam, station):
    database = open(path, "a")

    database.write(f"{bericht}/{datumTijd}/{naam}/{station}\n")

    database.close()
    # return true voor feedback of dit gelukt is of niet
    return True


def readDatabase():
    database = open(path, "r")

    fileLines = database.readlines()
    database.close()

    return fileLines


def clear():
    database = open(path, "r+")
    database.truncate()

    database.close()

