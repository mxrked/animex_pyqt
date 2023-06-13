from backend.database.classes.Connection import db_connection
# from backend.database.accessing_db import connectToDB

import pyodbc
import os

# Contents from sample_code
def find_ssms_installation_location():
    '''
    This is used to detect if the user has SSMS installed on their computer
    :return: location
    '''

    possible_locations = [
        r"C:\Program Files\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"C:\Program Files (x86)\Microsoft SQL Server Management Studio 19\Common7\IDE",
        r"D:\Microsoft SQL Server Management Studio 19\Common7\IDE",
        # Add more possible locations if applicable
    ]

    # Checking all of the locations at the top to see if that path exists
    for location in possible_locations:
        if os.path.exists(location):
            return location

    return None  # SSMS not found
def locating_odbc_drivers():
    '''
    This is used to check if ODBC Drivers are installed
    :return: boolean
    '''

    driver_name = "ODBC Driver 17 for SQL Server"
    drivers = [driver for driver in pyodbc.drivers() if driver == driver_name] # Goes through all the drivers to find one that matches the driver name
    return bool(drivers)

def checking_database_and_tables(self):
    '''
    This is used to check if both the database "Animex" and tables "Users" "Anime" "Products" exist
    :return: boolean
    '''

    # This will check if the connection was successful and will
    # check if the Database was properly made
    try:
        connection = db_connection
        cursor = connection.cursor()
        print(" ")
        print(" ")
        print("------------------------------")
        print("Database 'Animex' WAS found!!")
        print("------------------------------")
        print(" ")
        print(" ")
    except Exception as e:
        print(" ")
        print(" ")
        print("---------------------------------")
        print("Database 'Animex' was NOT found..")
        print("---------------------------------")
        print(" ")
        print(" ")
        pass


    try:
        # Checking if database exists
        checkDBQuery = "SELECT COUNT(*) FROM sys.databases WHERE name = 'Animex'"
        cursor.execute(checkDBQuery)
        database_exists = cursor.fetchone()[0]

        if database_exists:
            foundDB = True
        else:
            foundDB = False
            print("Could not find Animex")
    except Exception as e:
        print("An error occurred while checking the database:", str(e))
        foundDB = False

    try:
        checkTableQuery_1 = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'Users'"
        checkTableQuery_2 = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'Anime'"
        checkTableQuery_3 = "SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = 'Products'"
        cursor.execute(checkTableQuery_1)
        table_1_exists = cursor.fetchone()[0]
        cursor.execute(checkTableQuery_2)
        table_2_exists = cursor.fetchone()[0]
        cursor.execute(checkTableQuery_3)
        table_3_exists = cursor.fetchone()[0]

        if table_1_exists and table_2_exists and table_3_exists:
            foundTable = True
        else:
            foundTable = False
    except Exception as e:
        print("An error occurred while checking the tables:", str(e))
        foundTable = False

    if foundDB and foundTable:
        return True
    else:
        return False

# Calls for checkers
detect_odbc_drivers = locating_odbc_drivers()
ssms_installation_location = find_ssms_installation_location()

# Original content
def detect_required_programs(self):
    '''
    This will check if both programs are installed and will return its respected value
    :return: bothFound
    '''

    # foundODBC = False
    # foundSSMS = False
    # bothFound = False

    detect_db_and_table = checking_database_and_tables(self) # This is used to check if both the database and table exist

    # Detect/Find SSMS
    if ssms_installation_location:
        foundSSMS = True
        print("SSMS Was Found: " + ssms_installation_location)
    else:
        foundSSMS = False

    # Detect/Find ODBC
    if detect_odbc_drivers:
        foundODBC = True
        print("Appropriate drivers detected!")
    else:
        foundODBC = False

    # Checking for database and table
    if checking_database_and_tables:
        print("Tables were found!!")

    else:
        print("Tables were NOT found..")

    # Error handling
    if foundSSMS != True:
        print("SSMS WAS NOT FOUND! Use the README.md to learn where to download SSMS to.")
        sSMSNotFound = "SSMS was not found"
        return sSMSNotFound

    if foundODBC != True:
        print("ODBC Driver 17 for SQL Server WAS NOT FOUND! Install it and re-run.")
        oDBCNotFound = "ODBC was not found"
        return oDBCNotFound

    if foundSSMS != True and foundODBC != True:
        bothNotFound = "Both programs were not found"
        return bothNotFound

    # Return if both are found
    if foundSSMS and foundODBC:
        if detect_db_and_table:
            allFound = "All requirements were found"

        else:
            allFound = "Only SSMS and Drivers were found, not database and tables."

        return allFound
