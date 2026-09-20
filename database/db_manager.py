import sqlite3
from config.settings import DATABASE_PATH

def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    return connection

def create_database():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS containers (
            container_id TEXT PRIMARY KEY,
            status TEXT,
            location TEXT,
            container_type TEXT
        )
    """)

    connection.commit()
    connection.close()

def insert_sample_data(container_id,status,location,container_type):
    connetion = get_connection()
    cursor = connetion.cursor()
    cursor.execute(""" INSERT INTO containers(container_id,status,location,container_type)
    VALUES(?,?,?,?)""",(container_id,status,location,container_type))
    connetion.commit()
    rows = cursor.rowcount
    connetion.close()
    return rows

def get_all_containers():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("select * from containers")
    result = cursor.fetchall()
    connection.close()
    return result

def get_one_container(container_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("select * from containers where container_id = ?",(container_id,))
    result = cursor.fetchone()
    connection.close()
    return result

def update_container(container_id,status):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("update containers set status = ? where container_id = ?",(status,container_id,))
    connection.commit()
    connection.close()

def delete_container(container_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE from containers where container_id = ?",(container_id,))
    connection.commit()
    connection.close()
    
                   

                   