import getpass
import oracledb

#pw = getpass.getpass("Enter password: ")

# dsn = """(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1522)(host=adb.eu-frankfurt-1.oraclecloud.com))(connect_data=(service_name=g059678eb35cc6c_objectnotfound_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"""

connection = oracledb.connect(
    user="admin",
    password='7KZYc!TrQQR*8onxTx4Z',
    dsn="objectnotfound_high",
    config_dir="/opt/oracle/config")

print("Successfully connected to Oracle Database")

cursor = connection.cursor()
print(cursor)


