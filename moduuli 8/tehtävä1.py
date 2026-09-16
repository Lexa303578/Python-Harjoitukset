import mysql.connector

yhteys = mysql.connector.connect(
    host ="localhost",
    database = "flight_game",
    user ="root",
    password ="Leosaa07"
    )
icao = input("Anna lentoaseman icao-koodi:")

sql ="SELECT name FROM airport WHERE ident = %s"

kursori =yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print("lentokenttä:", tulos[0])
    print("sijaintikunta:", tulos[0])
else:
    print("Lentokentää ei löytynyt.")
    kursori.close()
    yhteys.close()