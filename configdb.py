#libreria para la conexion a la base de datos
import pymysql

#metodo para relizar la conexion a mysql

def get_connection():
    return pymysql.connect(host='localhost', user='root', password='', db='dbbioblioteca' )