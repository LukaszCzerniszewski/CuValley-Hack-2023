import pandas



def loadHydroAsJson ():
    excel_data_df = pandas.read_excel('hydro - sample.xlsx',
                                      sheet_name='hydro',
                                      skiprows=[0, 1],
                                      usecols=[0,1,2],
                                      names=['Data','151160060','150180060'])

    return (excel_data_df.to_json(orient='records'))

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

print(loadMetoAsJson ())
print(loadHydroAsJson())