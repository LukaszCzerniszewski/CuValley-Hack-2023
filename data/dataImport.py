import pathlib
import getpass
import oracledb
import pandas
import time
from datetime import datetime
import re
from datetime import datetime
import json
from urllib import request

import openpyxl
import pandas
import pandas as pd
import requests as requests
#pip install openpyxl
import re

class FileWork():
    hydroTestFile = 'hydro+2021+2022.xlsx'
    metoTestFile = 'meteo - sample.xlsx'
    metoCsvFile = 'pobraneDane.csv'
    #  Wczytanie testowych danych Hydro przekazanych w excelu
    def loadHydroAsJson (self):
        excel_data_df = pandas.read_excel(self.hydroTestFile,
                                          sheet_name='hydro',
                                          skiprows=[0, 1],
                                          usecols=[0,1,2],
                                          names=['Data','151160060','150180060'])
        return (excel_data_df.to_json(orient='records'))

    #Wczytanie testowych danych Meto przekazanych w excelu
    def loadMetoAsJson (self):
        excel_data_df = pandas.read_excel(
            self.metoTestFile,
            sheet_name='dane',
            skiprows=[0],
            usecols=[0,1,3,5,7,9,11,13,15],
            names=['Data','250160410', '251170270', '250160610',
                   '250160030','250160070','250170050','251160230',
                   '251160170']
        )
        return (excel_data_df.to_json(orient='records'))

    #Funckja do ladowania nowych danych hydro pobranych jako csv ze strony
    def loadDataFromPageCsv(self):
        columns = ['kod_stacji', 'rok', 'miesiac', 'dzien', 'opad[mm]']
        df = pandas.read_csv(self.metoCsvFile, header=1,
                             usecols=[0,2,3,4,5],
                              names=columns,
                              skiprows=0,
                             encoding= 'unicode_escape')

        #ujednolicenie do daty przekazanego przez KGHM
        df["Data"] = df['dzien'].astype(str) +"-"+ df["miesiac"].astype(str)+"-"+ df["rok"].astype(str)
        df = df.drop(['dzien', "miesiac", "rok"], axis=1)

        #zmiana do stringa
        df["kod_stacji"] = df["kod_stacji"].astype(str)
        df["opad[mm]"] = df["opad[mm]"] .astype(str)

        return df.to_json(orient='records')

    #Funckcja przyjmuje na wejsciu jsona i liste kodw_stacji
    # Zwaracana jest lista z elementami tylko z numerami kod_stacji znajdujcymi sie na liscie
    def extractFromJson(self, json, list):

        df = pandas.read_json(json, orient='records')
        df["kod_stacji"] = df["kod_stacji"].astype(str)
        list = [str(x) for x in list]


        df = df[df["kod_stacji"].isin(list)]
        df.to_json('data.json', orient='records')
        print(df)


        return df

    def responseToMeteo(self):
        stacjeeeeeee = [250160410,
                        251170270,
                        250160610,
                        250160030,
                        250160070,
                        250170050,
                        251160230,
                        251160170,
                        249180550,
                        250160590,
                        250170110,
                        250160260,
                        250170290,
                        250170390,
                        250170330,
                        250170760,
                        251170150,
                        249180280,
                        250170340,
                        251160290,
                        250160220,
                        251170320,
                        250150110,
                        250160620,
                        251160310,
                        350160520,
                        250170730,
                        250170750,
                        250180190,
                        250160450,
                        250160520,
                        351160415,
                        351160418,
                        250160470,
                        250180230,
                        250160170,
                        251160190,
                        250160120,
                        250180330,
                        251170420,
                        250160630,
                        250160650,
                        251170140,
                        250160540,
                        251170290,
                        250170230,
                        251160220,
                        251170130,
                        250160510,
                        350170530,
                        251160110,
                        250160320,
                        251170430,
                        250170250,
                        250170220,
                        250160490,
                        251160150,
                        250170530,
                        250170120,
                        250160090,
                        350180540,
                        250170540,
                        251180230,
                        251160140,
                        250160480,
                        251170090,
                        250180030,
                        250160560,
                        250170090,
                        250180380,
                        250160840,
                        250160130,
                        251150360,
                        250160360,
                        251170210,
                        251150280,
                        250160270,
                        351160424,
                        250160530,
                        250170280,
                        251160370,
                        249180130,
                        249180290,
                        250160350,
                        250180510,
                        251160080]

        lo = [16.7442,
              17.5447,
              16.8908,
              16.0986,
              16.9900,
              17.4667,
              16.7264,
              16.6131,
              18.6092,
              16.6333,
              17.0172,
              16.6242,
              17.0842,
              17.7947,
              17.3872,
              17.6233,
              17.4614,
              18.9403,
              17.4381,
              16.1836,
              16.3492,
              17.3564,
              15.9358,
              16.8842,
              16.7481,
              16.6142,
              17.4761,
              17.6122,
              18.6233,
              16.2219,
              16.8850,
              16.2078,
              16.5347,
              16.2939,
              18.1528,
              16.4286,
              16.2169,
              16.1958,
              18.6153,
              17.1597,
              16.7731,
              16.6708,
              17.2772,
              16.5408,
              17.7158,
              17.3531,
              16.9306,
              17.6653,
              16.7347,
              17.9689,
              16.4642,
              16.6358,
              17.9156,
              17.1664,
              17.0167,
              16.5183,
              16.0561,
              17.5744,
              17.1683,
              16.5431,
              18.1908,
              17.7614,
              18.1556,
              16.2572,
              16.3794,
              17.1797,
              18.3639,
              16.8661,
              17.0661,
              18.1697,
              16.5525,
              16.2411,
              15.9028,
              16.7928,
              17.0681,
              15.7475,
              16.4392,
              16.9000,
              16.3942,
              17.7953,
              16.7225, 18.3759, 18.5338, 16.3946, 18.3242, 16.0450]

        la = [50.5092,
              51.1189,
              50.2547,
              50.9250,
              50.8822,
              50.8692,
              51.2619,
              51.4483,
              49.7750,
              50.2497,
              50.7586,
              50.7433,
              50.4114,
              50.1819,
              50.3022,
              50.6517,
              51.4661,
              49.5853,
              50.2881,
              51.0633,
              50.7186,
              51.0436,
              50.9089,
              50.2272,
              51.0331,
              50.4369,
              50.6458,
              50.4750,
              50.5692,
              50.4381,
              50.3453,
              51.1925,
              51.8356,
              50.4050,
              50.4850,
              50.7639,
              51.4119,
              50.8036,
              50.3419,
              51.0864,
              50.2183,
              50.1533,
              51.5111,
              50.3014,
              51.0658,
              50.4647,
              51.2894,
              51.5775,
              50.3567,
              50.6269,
              51.6319,
              50.6442,
              51.4344,
              50.4722,
              50.4700,
              50.4253,
              51.5006,
              50.3025,
              50.6867,
              50.8539,
              50.0611,
              50.3108,
              51.0561,
              51.5081,
              50.4100,
              51.6942,
              50.9047,
              50.3025,
              50.7922,
              50.2628,
              50.4306,
              50.8067,
              51.0131,
              50.5753,
              51.3228,
              51.0906,
              50.7028,
              51.1033,
              50.3300,
              50.4422,
              51.156, 49.4454, 49.3350, 50.3434, 50.0555, 51.3933]

        # stacje_ids = ['250160410', '251170270', '250160610', '250160030', '250160070', '250170050', '251160230', '251160170', '249180130', '249180550', '250160590', '250170110', '250160260', '250170290', '251160080', '250170390', '250170330', '250170760', '251170150', '249180280', '249180290', '250170340', '251160290', '250160220', '251170320', '250150110', '250160620', '251160310', '350160520', '250170730', '250170750', '250180190', '250160450', '250160520', '351160415', '351160418', '250160470', '250180230', '250160170', '251160190', '250160120', '250180330', '251170420', '250160630', '250160650', '251170140', '250160540', '251170290', '250170230', '251160220', '251170130', '250160510', '350170530', '251160110', '250160320', '251170430', '250170250', '250170220', '250160490', '251160150', '250170530', '250170120', '250160090', '350180540', '250170540', '251180230', '251160140', '250180510', '250160480', '251170090', '250160350', '250180030', '250160560', '250170090', '250180380', '250160840', '250160130', '251150360', '250160360', '251170210', '251150280', '250160270', '351160424', '250160530', '250170280', '251160370']



        # values = re.findall(r'\(([^)]+)\)', string)
        # print(values)
        url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{}%2C{}?unitGroup=metric&elements=datetime%2Cprecip&include=days&key=E9AEF3HPXVNG34298XYBEANPQ&contentType=json'
        filename = 'responses2/resp{}.json'

        for i in range(1, 87):
            n_file = filename.format(i)
            new_str = url.format(la[i - 1], lo[i - 1])
            response = requests.get(new_str)
            if response.status_code == 200:
                with open(n_file, 'w') as file:
                    json.dump(response.json(), file)
            else:
                print('failed')


class DataBaseWork():
    password = '7KZYc!TrQQR*8onxTx4Z'
    userName = 'ADMIN'
    cursor = None


    def __init__(self):
        print("Yea")
        self.dbConnect()

    def dbConnect(self):
        path = pathlib.Path('C:\\Program Files\\Oracle\\instantclient_21_8\\network\\admin')
        connection = oracledb.connect(
            user=self.userName,
            password=self.password,
            dsn="objectnotfound_high",
            config_dir=path)
        print("Successfully connected to Oracle Database", flush=True)
        self.cursor = connection.cursor()

    def pushHydroToBase(self, json):
        json = pandas.read_json(json, orient='records')
        f = open("demofile2.txt", "a")



        for index, row in json.iterrows():
            #x = datetime.strptime(str(row.Data), '%d-%m-%Y')

            x = pandas.to_datetime(row.Data, unit='ms')
            print(x)

            #x = datetime.fromtimestamp(int(row.Data))
            date = x.strftime("%y/%m/%d")

            query1 = "INSERT INTO station ( DDate, waterstate, stationcode ) VALUES ('" + str(date) + "'," + str(row[1]) + ",151160060);"
           # query2 = "INSERT INTO station ( DDate, waterstate, stationcode ) VALUES ('" + str(date) + "'," + str(row[2]) + ",150180060);"
            f.write(query1)
            f.write('\n')
           # f.write(query2)
           # f.write('\n')
            # self.cursor.execute(query1)
            # self.cursor.execute(query2)
        f.close()

    def pushCsvMeteoFileToBase(self):
        file1 = open('meteo_fixed.csv', 'r', encoding="utf-8")
        lines = file1.readlines()

        count = 0
        l = lines[0].split(";")
        ready = []
        for ll in l:
            ll = re.sub(r'^.*\(', '', ll)
            ll = ll.replace(")", "")
            ready.append(ll)

        # pominiecie stacji i headerow
        for line in lines[2:]:
            l = line.split(";")
            ddate = l[0]
            # kazde 2 kolejne sa do poszczegolnej stacji
            for i in range(1, len(l), 2):
                a = l[i]
                if a == '':
                    a = str(0)
                query = "INSERT INTO meteo_station (STATIONCODE, DDATE, DAILYRAINFALLTOTAL) VALUES (" + ready[
                    i] + ",TO_DATE('" + ddate + "', 'dd/mm/yyyy')," + a + ")"
                self.cursor.execute(query)

    def pushMeteoToBase(self):
        # wyciąganie danych z pliku json - prognozy oraz robienie z tego inserta do bazy:
        stacje = [250160410,
                  251170270,
                  250160610,
                  250160030,
                  250160070,
                  250170050,
                  251160230,
                  251160170,
                  249180550,
                  250160590,
                  250170110,
                  250160260,
                  250170290,
                  250170390,
                  250170330,
                  250170760,
                  251170150,
                  249180280,
                  250170340,
                  251160290,
                  250160220,
                  251170320,
                  250150110,
                  250160620,
                  251160310,
                  350160520,
                  250170730,
                  250170750,
                  250180190,
                  250160450,
                  250160520,
                  351160415,
                  351160418,
                  250160470,
                  250180230,
                  250160170,
                  251160190,
                  250160120,
                  250180330,
                  251170420,
                  250160630,
                  250160650,
                  251170140,
                  250160540,
                  251170290,
                  250170230,
                  251160220,
                  251170130,
                  250160510,
                  350170530,
                  251160110,
                  250160320,
                  251170430,
                  250170250,
                  250170220,
                  250160490,
                  251160150,
                  250170530,
                  250170120,
                  250160090,
                  350180540,
                  250170540,
                  251180230,
                  251160140,
                  250160480,
                  251170090,
                  250180030,
                  250160560,
                  250170090,
                  250180380,
                  250160840,
                  250160130,
                  251150360,
                  250160360,
                  251170210,
                  251150280,
                  250160270,
                  351160424,
                  250160530,
                  250170280,
                  251160370,
                  249180130,
                  249180290,
                  250160350,
                  250180510,
                  251160080]

        file = 'respv4/resp{}.json'

        for i in range(1, 6):
            new_file = file.format(i)
            with open(new_file, 'r') as json_file:
                data = json.load(json_file)
            for day in data['days']:
                print(
                    f"INSERT INTO WEATHER_PROGNOSE (PREDICTEDDATE, PREDICTEDDAILYRAINFALLTOTAL, METEO_STATION_ID) VALUES('{day['datetime']}', {day['precip']}, {stacje[i - 1]});")









fileWork = FileWork()
db = DataBaseWork()
db.pushHydroToBase(fileWork.loadHydroAsJson())
#print(fileWork.loadHydroAsJson())
#print(fileWork.extractFromJson(fileWork.loadDataFromPageCsv(),[250160410, '251170270', '250160610','250160030','250160070','250170050','251160230','251160170']))




