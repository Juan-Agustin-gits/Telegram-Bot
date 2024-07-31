import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host='localhost',
        database ='ChatBot_Anto_Citas',
        user='root',
        password='Halo4agustin_'
    )

    if connection.is_connected():
        db_info = connection.get_server_info()

        print(f"{db_info}")

        cursor = connection.cursor()
        cursor.execute("SELECT DATABASE(); ")
        record = cursor.fetchone()
        print(f"connected : {record}")


except Error as e:
        print(f"Error is : {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

def Create(title, site, description, H_NH, day ):
    data = (title, site, description, H_NH, day)
    query  = "INSERT INTO Citas (lugar, descripcion, hecho, fecha, Titulo) VALUES (?, ?, ?, ?, ?);S"

    cursor.execute(query, data)
    connection.commit()
    print("data insert")

### dejar para el final     
def Delete(title, site, description, H_NH, day):
    data = (title, site, description, H_NH, day)
    
