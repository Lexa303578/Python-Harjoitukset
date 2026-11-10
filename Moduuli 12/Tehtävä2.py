import requests

api_key = "bc157ff242d8107e5b5c7765b351d00c"
paikkakunta = input("Anna paikkakunnan nimi:")
url = "https://api.openweathermap.org/data/2.5/weather"

parametrit = {
    "q": paikkakunta,
    "appid": api_key,
    "units": "metric",
    "lang": "fi"
}

vastaus = requests.get(url,params=parametrit)
data = vastaus.json()

if vastaus.status_code == 200:
    säätila = data["weather"][0]["description"]
    lämpötila = data["main"]["temp"]

    print("Säätila:", säätila)
    print("Lämpötila", lämpötila,"astetta")

else:
    print("Säätilojen hakeminen epäonnistui")
    
    