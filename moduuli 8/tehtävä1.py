import mysql.connector

yhteys = mysql.connector.connect(
    host ="localhost",
    database = "lentokentat",
    user ="kayttaja",
    password ="salasana"
    )
icao = input("Anna lentoaseman icao-koodi:")

sql ="SELECT name, municipilaty FROM airport WHERE ident = %s"

kursori =yhteys.cursor()
kursori.execute(sql, (icao,))

tulos = kursori.fetchone()

if tulos:
    print("lentokenttä:", tulos[0])
    print("sijaintikunta:", tulos[1])
else:
    print("Lentokentää ei löytynyt.")
    kursori.close()
    yhteys.close()