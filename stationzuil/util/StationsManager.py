import random

from stationzuil.data import PostgresDataBaseEditor



def getAllStations():
    stationOutput = PostgresDataBaseEditor.getAlleStationNamen()
    return [item[0] for item in stationOutput]
def randomStation():
    stations = getAllStations()
    return random.choice(stations)
