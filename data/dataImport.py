import pandas


#Wczytanie testowych danych Hydro przekazanych w excelu
def loadHydroAsJson ():
    excel_data_df = pandas.read_excel('hydro - sample.xlsx',
                                      sheet_name='hydro',
                                      skiprows=[0, 1],
                                      usecols=[0,1,2],
                                      names=['Data','151160060','150180060'])
    return (excel_data_df.to_json(orient='records'))

#Wczytanie testowych danych Meto przekazanych w excelu
def loadMetoAsJson ():
    excel_data_df = pandas.read_excel(
        'meteo - sample.xlsx',
        sheet_name='dane',
        skiprows=[0],
        usecols=[0,1,3,5,7,9,11,13,15],
        names=['Data','250160410', '251170270', '250160610',
               '250160030','250160070','250170050','251160230',
               '251160170']
    )
    return (excel_data_df.to_json(orient='records'))

#Funckja do ladowania nowych danych hydro pobranych jako csv ze strony
def loadDataFromPageCsv():
    columns = ['kod_stacji', 'rok', 'miesiac', 'dzien', 'opad[mm]']
    df = pandas.read_csv('pobraneDane.csv', header=1,
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
def extractFromJson(json, list):

    df = pandas.read_json(json, orient='records')
    df["kod_stacji"] = df["kod_stacji"].astype(str)
    list = [str(x) for x in list]


    df = df[df["kod_stacji"].isin(list)]
    df.to_json('data.json', orient='records')
    print(df)


    return df


print(loadMetoAsJson ())
print(loadHydroAsJson())
print(extractFromJson(loadDataFromPageCsv(),[250160410, '251170270', '250160610',
               '250160030','250160070','250170050','251160230',
               '251160170']))