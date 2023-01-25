import pandas



def loadHydroAsJson ():
    excel_data_df = pandas.read_excel('hydro - sample.xlsx', sheet_name='hydro', skiprows=[0, 1])

    return (excel_data_df.to_json(orient='records'))

def loadMetoAsJson ():
    excel_data_df = pandas.read_excel('meteo - sample.xlsx', sheet_name='dane', skiprows=[0], usecols=[0,1,3,5,7,9,10,11,12,13,15,17])

    return (excel_data_df.to_json(orient='records'))

