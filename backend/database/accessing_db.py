'''

    This is used to store functions for connecting/disconnecting from the database

'''

import pyodbc

connect = None # This is used to pass the close function on the connection if there isnt one

def closeConnectionToDB(self):
    '''
    This is used to close the connect to the database
    :return:
    '''

    # This is used to pass the close function on the connection if there isnt one
    global connect

    try:

        # This is used to pass the close function on the connection if there isnt one
        if connect is not None:
            connect.close()

            connect = None

            print("Connection closed.")

    except pyodbc.Error as e:
        pass

