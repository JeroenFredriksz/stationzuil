import psycopg2

connection = psycopg2.connect("dbname=stationzuil user=postgres password=postgres port=5433")

cursor = connection.cursor


