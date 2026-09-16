import mysql.connector
yhteys = mysql.connector.connect(
    host="localhost",
    database="flight_game",
    user="root",
    password ="Leosaa07"
)
maakoodi = input("Anna maakoodi:")
sql ="""
SELECT type,COUNT(*)
FROM airport
WHERE iso_country = %s
GROUP BY type
"""
kursori = yhteys.cursor()
kursori.execute(sql,(maakoodi,))

tulokset = kursori.fetchall()

for tyyppi, maara in tulokset:
    print(tyyppi, maara)

kursori.close()
yhteys.close()