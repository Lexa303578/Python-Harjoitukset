import mysql.connector
yhteys = mysql.connector.connect(
    host="localhost",
    database="lentokentät",
    user="käyttäjä",
    password ="salasana"
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