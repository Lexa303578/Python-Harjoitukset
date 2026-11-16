from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
app.json.sort_keys = False      
app.json.ensure_ascii = False    


def hae_yhteys():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="Leosaa07",
        autocommit=True,
    )


@app.route("/kenttä/<icao>")
def kentta(icao):
    icao = icao.upper()
    yhteys = None

    try:
        yhteys = hae_yhteys()
        kursori = yhteys.cursor()
        kursori.execute(
            "SELECT ident, name, municipality FROM airport WHERE ident = %s",
            (icao,),
        )
        rivi = kursori.fetchone()
    except mysql.connector.Error:
        return jsonify({"virhe": "Tietokantayhteys epäonnistui."}), 500
    finally:
        if yhteys is not None and yhteys.is_connected():
            yhteys.close()

    if rivi is None:
        return jsonify({"virhe": "Lentokenttää ei löytynyt."}), 404

    return jsonify({"ICAO": rivi[0], "Name": rivi[1], "Municipality": rivi[2]})


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)