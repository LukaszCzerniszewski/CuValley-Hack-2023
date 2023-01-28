import getpass
import oracledb

connection = oracledb.connect(
    user="admin",
    password='7KZYc!TrQQR*8onxTx4Z',
    dsn="objectnotfound_high",
    config_dir="/opt/oracle/config")

print("Successfully connected to Oracle Database")

cur = connection.cursor()

# # wyszukanie naszych tabel w bazie
# cur.execute("SELECT owner, table_name FROM all_tables")
# res = cur.fetchall()
# a = dict()
# for row in res:
#     if(str(row[0])=="ADMIN"):
#         a[str(row[1])] = 0
# print(list(a.keys()))


['METEO_STATION', 'WEATHER_PROGNOSE', 'STATION']
cur.execute("SELECT * FROM STATION")
res = cur.fetchall()
a = dict()
for row in res:
    print(str(row))


cur.close()
connection.close()


