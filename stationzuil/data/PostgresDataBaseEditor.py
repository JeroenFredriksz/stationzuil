import datetime

import psycopg2

connection = psycopg2.connect("dbname=stationzuil user=postgres password=postgres port=5433")
cursor = connection.cursor()


def inputGekeurdBericht(goedgekeurd, auteur, bericht, creeerdatum, moderatorNaam, stationnaam):
    berichtInputString = f"INSERT INTO gekeurdBericht (naammoderator, bericht, creeerdatum, keurdatum, goedgekeurd, auteur, stationnaam) VALUES ('{moderatorNaam}', '{bericht}', '{creeerdatum}', '{creeerdatum}', '{goedgekeurd}', '{auteur}', '{stationnaam}')"

    cursor.execute(berichtInputString)
    connection.commit()

def getLaatste5Berichten():
    selectString = f'SELECT * FROM gekeurdbericht ORDER BY keurdatum DESC LIMIT 5;'
    cursor.execute(selectString)
    return cursor.fetchall()

def getFaciliteitenStationService(stationnaam):
    select = f"SELECT * from station_service where station_city = '{stationnaam}'"
    cursor.execute(select)
    return cursor.fetchall()
