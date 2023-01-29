import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import getpass
import oracledb
import pathlib
import datetime
import collections
from sklearn.metrics import mean_absolute_error
from keras.models import Sequential
from keras.layers import Dense
import keras as tf
from keras import backend as K

# Connecting to db to fetch data
path = pathlib.Path('C:\\Users\\48664\\Desktop\\WAT\\Magister\\Semestr 1\\Mum2')

connection = oracledb.connect(
    user='ADMIN',
    password='7KZYc!TrQQR*8onxTx4Z',
    dsn='objectnotfound_high',
    config_dir=path)

print("Successfully connected to Oracle Database", flush=True)
cursor = connection.cursor()


def time_to_int(dateobj):
    total = int(dateobj.strftime('%S'))
    total += int(dateobj.strftime('%M')) * 60
    total += int(dateobj.strftime('%H')) * 60 * 60
    total += (int(dateobj.strftime('%j')) - 1) * 60 * 60 * 24
    total += (int(dateobj.strftime('%Y')) - 1970) * 60 * 60 * 24 * 365
    return total

# Water level
water_level_query = """
    SELECT 
        STATIONCODE,
        DDATE,
        WATERSTATE
    FROM STATION
"""
water_levels_raw = np.asarray(cursor.execute(water_level_query).fetchall())
water_meter_stations = list(set(water_levels_raw[:, 0]))
water_levels = {}
for water_level in water_levels_raw:
    stationId, ddate, w_lvl = water_level
    if water_levels.get(stationId) is None:
        water_levels[stationId] = {}
    water_levels[stationId][time_to_int(ddate)] = w_lvl/500

# Get meteo
meteo_station_query = """
    SELECT 
        STATIONCODE,
        DDATE,
        DAILYRAINFALLTOTAL
    FROM Meteo_station
"""
meteo_stations_raw = np.asarray(cursor.execute(meteo_station_query).fetchall())
meteo_stations = list(set(meteo_stations_raw[:, 0]))
print(sorted(meteo_stations))
meteo_station_rain = {}
for meteo_station in meteo_stations_raw:
    stationId, ddate, rain_lvl = meteo_station
    if meteo_station_rain.get(stationId) is None:
        meteo_station_rain[stationId] = {}
    meteo_station_rain[stationId][time_to_int(ddate)] = rain_lvl/100

# 1319241600
# Creating training set for 151160060
training_set = []
etiquetes = []
water_level_151160060 = water_levels.get(150180060)
first_day = sorted(list(water_level_151160060.keys()))[0]
curr_day_water_level = water_level_151160060.get(first_day)

last_day = sorted(list(water_level_151160060.keys()))[-1]
print(last_day)
# print(meteo_stations.sort())
while first_day + 86400 <= last_day:
    value_for_training_set = []
    # Adding water level of Odra in day x
    value_for_training_set.append(curr_day_water_level)
    for key in sorted(meteo_stations):
        value_for_training_set.append(meteo_station_rain[key].get(first_day))
    if None not in value_for_training_set:
        training_set.append(value_for_training_set)
        etiquetes.append(water_level_151160060.get(first_day + 86400))
    first_day += 86400

df = pd.DataFrame(value_for_training_set)
filepath = 'my_excel_file.xlsx'

df.to_excel(filepath, index=False)


X_train, X_test, y_train, y_test = train_test_split(training_set, etiquetes, test_size=0.2)
X_train = K.cast_to_floatx(X_train)
X_test = K.cast_to_floatx(X_test)
y_train = K.cast_to_floatx(y_train)
y_test = K.cast_to_floatx(y_test)


# X_test = tf.convert_to_tensor(X_test, dtype=tf.float32)
# y_train = tf.convert_to_tensor(y_train, dtype=tf.float32)
# y_test = tf.convert_to_tensor(y_test, dtype=tf.float32)
# K.cast_to_floatx(X_train)
#  np.asarray(X_train)
# X_test = np.asarray(X_test)
# y_train = np.asarray(y_train)
# y_test = np.asarray(y_test)


model = Sequential()
model.add(Dense(64, input_dim=87, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mean_squared_error', optimizer='adam')

model.fit(X_train, y_train, epochs=300, batch_size=32)

# scores = model.evaluate(X_test, y_test)
# print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# y_pred = model.predict(X_test)
# print(y_pred)
# for i in range(0, len(y_pred)):
#     print(y_pred[i], "-->", y_test[i])

model.save("model_150180060.h5")
