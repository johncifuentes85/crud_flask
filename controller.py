#llamamos la conexion
from configdb import get_connection

#se crea una funcion para agregar usuario y pedimos los campos pueden llamarse igual a la variables de mysql o diferente
def add_user(name,email,phone,passwd):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("INSER INTO user(name,email,phone,passwd) VALUES (%s,%s,%s,%s)",(name,email,phone,passwd))
        cnn.commit()
        cnn.close()

def update_user(name,email,phone,passwd):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("UPDATE user SER name = %s, email = %s, phone = %s, passwd = %s WHERE id = %s, (name,email,phone,passwd,id) ")
        cnn.commit()
        cnn.close()
    
def delete_user(id):
    cnn = get_connection()
    with cnn.cursor() as cursor:
        cursor.execute("DELETE FROM user WHERE id = %s", (id))
        cnn.commit()
        cnn.close()

def get_user():
    cnn = get_connection()
    user = []
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone FROM user")
        user = cursor.fetchall()
        cnn.close()
        return user

def get_user_id(id):
    cnn = get_connection()
    user = None
    with cnn.cursor() as cursor:
        cursor.execute("SELECT id, name, phone, passwd FROM user WHERE id = %s", (id))
    cnn.close()
    return user

