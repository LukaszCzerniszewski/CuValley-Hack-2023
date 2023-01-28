import oracledb
import json
from datetime import datetime
from flask import Flask, jsonify, make_response, redirect, request, url_for, abort
app = Flask(__name__)

from flask import send_from_directory

api_key = "c9f53a7a0657ed8769098ad48074709cbd0bf0ad83e41e67164a9316605b86b0bdd81f0b16fd8b1a4a3dc7c0194f9bcb50cc29c16bfd73ef42c07e81b35026ef"

connection = oracledb.connect(
    user="admin",
    password='7KZYc!TrQQR*8onxTx4Z',
    dsn="objectnotfound_high",
    config_dir="/opt/oracle/config")
cur = connection.cursor()

@app.route('/<path:path>')
def send_report(path):
    return send_from_directory('front', path)

@app.route('/')
def hello_world():
    return send_from_directory('front', 'index.html')

@app.route('/api')
def api_test_call():
    if not request.headers.has_key('kkey_y') or request.headers['kkey_y'] != api_key:
        abort(404)
    cur.execute("SELECT * FROM METEO_STATION")
    res = cur.fetchall()
    a = []
    for row in res:
        r = list(row)
        r[2] = datetime.timestamp(row[2])
        a.append(r)

    response = make_response(
                jsonify(
                    a
                ),
                200,
            )
    response.headers["Content-Type"] = "application/json"
    return response
    
@app.route('/api/get_rainfall', methods=['POST'])
def get_rainfall():
    if not request.headers.has_key('kkey_y') or request.headers['kkey_y'] != api_key:
        abort(404)
    data = request.get_json()
    station_code = data['STATIONCODE']
    date = data['DDATE']
    query = f"SELECT DAILYRAINFALLTOTAL FROM METEO_STATION WHERE STATIONCODE = '{station_code}' AND DDATE = '{date}'"
    cur.execute(query)
    result = cur.fetchone()
    cur.close()
    if result:
        daily_rainfall_total = result[0]
        return jsonify(daily_rainfall_total)
    else:
        return jsonify("No data found for the provided station code and date"), 404

@app.route('/api/get_waterstate', methods=['POST'])
def get_rainfall():
    if not request.headers.has_key('kkey_y') or request.headers['kkey_y'] != api_key:
        abort(404)
    data = request.get_json()
    station_code = data['STATIONCODE']
    date = data['DDATE']
    query = f"SELECT DAILYRAINFALLTOTAL FROM METEO_STATION WHERE STATIONCODE = '{station_code}' AND DDATE = '{date}'"
    cur.execute(query)
    result = cur.fetchone()
    cur.close()
    if result:
        daily_rainfall_total = result[0]
        return jsonify(daily_rainfall_total)
    else:
        return jsonify("No data found for the provided station code and date"), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
