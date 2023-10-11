import pymysql
usuario = 'gitpod'
pwd = 'postgres'
host = 'localhost'
puerto = 3306 # El puerto por defecto de MySQL es 3306


# Inicia la conexión con el servidor
conexion = pymysql.connect(
    host=host,
    user=usuario,
    password=pwd,
    port=puerto  
)