def inputDatabase(bericht, datumTijd, naam, station):
    database = open("database.csv", "a")

    database.write(f"{bericht}/{datumTijd}/{naam}/{station}\n")

    database.close()
    # return true voor feedback of dit gelukt is of niet
    return True
