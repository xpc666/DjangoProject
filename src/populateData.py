import mysql.connector
import sqlite3
from sqlite3 import Error

def retrieveMySQLdata(table, query):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='petclinic',
                                             user='dbadmin',
                                             password='12345')

        # my_sql_select = """select id, first_name, last_name, address, city, telephone from petclinic.Owners"""

        cursor = connection.cursor()
        cursor.execute(query)
        records = cursor.fetchall()
        print("Total number of rows in table", table, cursor.rowcount)

    except mysql.connector.Error as e:
        print("Error reading data from MySQL table", e)
    finally:
        if connection.is_connected():
            connection.close()
            cursor.close()
            print("MySQL connection is closed")

    return records


def insertDataToSqlite(table, insert_sql, records):
    try:
        sqliteConnection = sqlite3.connect('db.sqlite3')
        cursor = sqliteConnection.cursor()
        if table == 'petclinic_pets':
            for row in records:
                data_tuple = (row[0], row[1], row[2], row[3], row[4])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_pets table ")
        elif table == 'petclinic_specialties':
            for row in records:
                data_tuple = (row[0], row[1])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_specialties table ")
        elif table == 'petclinic_types':
            for row in records:
                data_tuple = (row[0], row[1])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_types table ")
        elif table == 'petclinic_vets':
            for row in records:
                data_tuple = (row[0], row[1], row[2])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_vets table ")
        elif table == 'petclinic_vetspecialties':
            for row in records:
                data_tuple = (row[0], row[1])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_vetspecialties table ")
        elif table == 'petclinic_visits':
            for row in records:
                data_tuple = (row[0], row[1], row[2], row[3])
                cursor.execute(insert_sql, data_tuple)
                sqliteConnection.commit()
            print("Record inserted successfully into sqlite3.db petclinic_visits table ")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

def etlFromMySqlToSqlite(query_dict):
    for key, value in query_dict.items():
        records = retrieveMySQLdata(key, value[0])
        insertDataToSqlite(key, value[1], records)


print("retrieving data and display:")
query_dict = {'petclinic_pets': ['SELECT id, name, birth_date, type_id, owner_id FROM petclinic.pets', 'insert into petclinic_pets (id, name, birth_date, type_id, owner_id) values (?, ?, ?, ?, ?)'],
              'petclinic_specialties': ['SELECT id, name FROM petclinic.specialties', 'insert into petclinic_specialties (id, name) values (?, ?)'],
              'petclinic_types': ['SELECT id, name FROM petclinic.types', 'insert into petclinic_types (id, name) values (?, ?)'],
              'petclinic_vets': ['SELECT id, first_name, last_name FROM petclinic.vets', 'insert into petclinic_vets (id, first_name, last_name) values (?, ?, ?)'],
              'petclinic_vetspecialties': ['SELECT vet_id, specialty_id FROM petclinic.vet_specialties', 'insert into petclinic_vetspecialties (vet_id, specialty_id) values (?, ?)'],
              'petclinic_visits': ['SELECT id, pet_id, visit_date, description FROM petclinic.visits', 'insert into petclinic_visits (id, pet_id, visit_date, description) values (?, ?, ?, ?)']}
etlFromMySqlToSqlite(query_dict)
print("ETL from MySQL to Sqlite3 Completed!")


# def insertDataToSqlite():
#     records = retrieveMySQLdata()
#     print("\nPrinting each row")
#     for row in records:
#         print("Id = ", row[0], )
#         print("first_name = ", row[1])
#         print("last_name  = ", row[2])
#         print("city  = ", row[4], "\n")
#
#     sqlite3_insert_query = """INSERT INTO petclinic_owners
#                             (id, first_name, last_name, address, city, telephone)
#                             VALUES
#                             (?, ?, ?, ?, ?, ?) """
#     try:
#         sqliteConnection = sqlite3.connect('db.sqlite3')
#         cursor = sqliteConnection.cursor()
#         print("Successfully Connected to SQLite")
#
#         for row in records:
#             data_tuple = (row[0], row[1], row[2], row[3], row[4], row[5])
#             cursor.execute(sqlite3_insert_query, data_tuple)
#             sqliteConnection.commit()
#         print("Record inserted successfully into sqlite3.db Owner table ")
#         cursor.close()
#
#     except sqlite3.Error as error:
#         print("Failed to insert data into sqlite table", error)
#     finally:
#         if sqliteConnection:
#             sqliteConnection.close()
#             print("The SQLite connection is closed")
