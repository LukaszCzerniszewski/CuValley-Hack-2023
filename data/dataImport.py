import pathlib
import getpass
import oracledb
import pandas
import time
from datetime import datetime
#pip install openpyxl
import re

class FileWork():
    hydroTestFile = 'hydro - sample.xlsx'
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
        for index, row in json.iterrows():
            x = datetime.strptime(str(row.Data), '%d-%m-%Y')
            date = x.strftime("%y/%m/%d")

            query1 = "INSERT INTO station ( DDate, waterstate, stationcode ) VALUES ('" + str(date) + "'," + str(row[1]) + ",151160060);"
            query2 = "INSERT INTO station ( DDate, waterstate, stationcode ) VALUES ('" + str(date) + "'," + str(row[2]) + ",150180060);"
            self.cursor.execute(query1)
            self.cursor.execute(query2)

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









fileWork = FileWork()
db = DataBaseWork()
#print(fileWork.loadHydroAsJson())
#print(fileWork.extractFromJson(fileWork.loadDataFromPageCsv(),[250160410, '251170270', '250160610','250160030','250160070','250170050','251160230','251160170']))




