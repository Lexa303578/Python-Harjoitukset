import mysql.connector
from geopy.distance import geodesic
yhteys=mysql.connector.connect(
    host="localhost",
    database ="lentokentat",
    user = "käyttäjä",
    password ="salasana"
)
icao1=input("Anna ensimmäisen lentokentän ICAO-koodi:")
icao2=input("Anna toisen lentokentän ICAO-koodi:")

sql ="""
SELECT latitude_deg, longitude_deg
FROM airport
WHERE ident =%s
"""
kursori =yhteys.corsor()

kursori.execute(sql,(icao1,))
kentta1=kursori.fetchone()

kursori.execute(sql,(icao2,))
kentta2=kursori.fetchone()

if kentta1 and kentta2:
    koordinaatit1 = (kentta1[0], kentta1[1])
    koordinaatit2 =(kentta2[0],kentta2[1])

    etäisyys = geodesic(koordinaatit1, koordinaatit2).kilometers
    print(f"Lentekenttie vlinen etäysyys on {etäisyys:.1f} kilometriä.")
else:
    print("Jompaakumpaa lentokentää ei löytynyt.")
    kursori.close()
    yhteys.close()