'''

    This is used to store some functions that is used for displaying data from the database

'''


from backend.database.classes.Connection import db_connection
from backend.database.queries import *

def display_all_users(self):
    '''
    This is used to display all the current users to the console
    :param self: self
    :return:
    '''

    connection = db_connection
    cursor = connection.cursor()

    try:

        cursor.execute(get_all_users)
        entries = cursor.fetchall()
        connection.commit()

        print("All Current Users:")
        for entry in entries:
            print(entry)

    except Exception as e:
        print("Error retrieving indexes. Might be that there are no indexes.")


