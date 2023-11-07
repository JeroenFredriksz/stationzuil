import random

stations = ["Arnhem", "Almere", "Amersfoort"]


def RandomStation():
    randomindex = random.randint(0, len(stations) - 1)

    return stations[randomindex]


def isin(station):
    try:
        stations.index(station)
        return True
    except:
        return False
