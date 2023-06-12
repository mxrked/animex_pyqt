'''

    This is used to store some queries that might be used

'''

#from backend.database.accessing_db import connectToDB
from backend.database.classes.Connection import db_connection

import pyodbc, json


# Inserters

# Getters
get_all_users = "SELECT * FROM Users"
get_all_emails = "SELECT User_Email FROM Users"
get_all_passwords = "SELECT User_Password FROM Users"

