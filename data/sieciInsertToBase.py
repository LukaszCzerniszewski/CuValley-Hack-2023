from keras.models import load_model
import getpass
import oracledb
import pathlib
import numpy as np
import datetime

def time_to_int(dateobj):
    total = int(dateobj.strftime('%S'))
    total += int(dateobj.strftime('%M')) * 60
    total += int(dateobj.strftime('%H')) * 60 * 60
    total += (int(dateobj.strftime('%j')) - 1) * 60 * 60 * 24
    total += (int(dateobj.strftime('%Y')) - 1970) * 60 * 60 * 24 * 365
    return total


path = pathlib.Path('C:\\Users\\48664\\Desktop\\WAT\\Magister\\Semestr 1\\Mum2')
stations = [249180130, 249180280, 249180290, 249180550, 250150110, 250160030, 250160070, 250160090, 250160120, 250160130, 250160170, 250160220, 250160260, 250160270, 250160320, 250160350, 250160360, 250160410, 250160450, 250160470, 250160480, 250160490, 250160510, 250160520, 250160530, 250160540, 250160560, 250160590, 250160610, 250160620, 250160630, 250160650, 250160840, 250170050, 250170090, 250170110, 250170120, 250170220, 250170230, 250170250, 250170280, 250170290, 250170330, 250170340, 250170390, 250170530, 250170540, 250170730, 250170750, 250170760, 250180030, 250180190, 250180230, 250180330, 250180380, 250180510, 251150280, 251150360, 251160080, 251160110, 251160140, 251160150, 251160170, 251160190, 251160220, 251160230, 251160290, 251160310, 251160370, 251170090, 251170130, 251170140, 251170150, 251170210, 251170270, 251170290, 251170320, 251170420, 251170430, 251180230, 350160520, 350170530, 350180540, 351160415, 351160418, 351160424]
connection = oracledb.connect(
    user='ADMIN',
    password='7KZYc!TrQQR*8onxTx4Z',
    dsn='objectnotfound_high',
    config_dir=path)

print("Successfully connected to Oracle Database", flush=True)
cursor = connection.cursor()

model = load_model("model_151160060.h5")

meteo_station_query = """
    SELECT 
        METEO_STATION_ID,
        PREDICTEDDATE,
        PREDICTEDDAILYRAINFALLTOTAL
    FROM WEATHER_PROGNOSE
"""

STATION_ID = 151160060



meteo_stations_raw = np.asarray(cursor.execute(meteo_station_query).fetchall())
meteo_station_future = {}
for meteo_station in meteo_stations_raw:
    stationId, ddate, rain_lvl = meteo_station
    if meteo_station_future.get(ddate) is None:
        meteo_station_future[ddate] = {}
    meteo_station_future[ddate][stationId] = rain_lvl/100

for date in list(meteo_station_future.keys()):
    print(date.strftime("%y/%m/%d"), type(date))
    water_level_query = f"""
        SELECT 
            WATERSTATE
        FROM STATION WHERE STATIONCODE = {STATION_ID} AND DDATE = TO_DATE('{date.strftime("%y/%m/%d")}', 'YY/MM/DD')
    """
    try:
        station_water_state = cursor.execute(water_level_query).fetchall()[0][0]/500
    except IndexError:
        station_water_state = None
    if station_water_state is not None:
        value_for_prediction = [station_water_state]
        for meteo_station_id in stations:
            value_for_prediction.append(meteo_station_future[date][meteo_station_id])
        water_level_prediction = model.predict([value_for_prediction])
        data_for_insert_to_db = {
            'ddate': (date + datetime.timedelta(days=1)),
            'waterstate': water_level_prediction[0][0] * 500,
            'stationcode': STATION_ID,
            'ispredicted': True
        }
        print(data_for_insert_to_db)
        insert_query = """
            INSERT INTO STATION (ddate, waterstate, stationcode, ispredicted)
            VALUES (:ddate, :waterstate, :stationcode, :ispredicted)
        """
        cursor.execute(insert_query, data_for_insert_to_db)
        connection.commit()
        print(data_for_insert_to_db)

print(list(meteo_station_future.keys()))
