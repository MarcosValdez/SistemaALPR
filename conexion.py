from mysql import connector

try:
    connection = connector.connect(
        user = 'root', 
        password = 'root',
        host = 'localhost',
        port = '3306',
        database = 'alpr'
    )

    if connection.is_connected():
        print("Conexion exitosa")
        info_serve = connection.get_server_info()
        print(info_serve)

except Exception as ex:
    print(ex)