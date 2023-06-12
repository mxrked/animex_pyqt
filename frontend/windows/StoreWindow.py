'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QCursor

from backend.database.classes.Connection import db_connection

from frontend.assets.variables.arrays import active_connections


import sys, pyodbc, atexit



class StoreWindow(QMainWindow):


    def __init__(self):
        super(StoreWindow, self).__init__()

        uic.loadUi("frontend/ui/StoreWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")


        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''

            atexit.register(cleanup_connections) # Making the function run ALWAYS when exiting

            #closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets

        # Displaying result of program detection

        # Show the app
        self.show()


    def closeEvent(self, event):
        '''
        This is used to close the window on the red X
        :param event:
        :return:
        '''

        atexit.register(cleanup_connections)
        sys.exit()


def cleanup_connections():
    '''
    This is used to close all connections
    :return:
    '''

    for connection in active_connections:
        connection.close()


# initializing app
app = QApplication(sys.argv)
UIWindow = StoreWindow()
app.exec_()