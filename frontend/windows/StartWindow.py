'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from backend.database.classes.Connection import db_connection

from frontend.assets.variables.arrays import active_connections
from frontend.assets.qrcs import light_bg, dark_bg, settings_icon, light_mode_icon, dark_mode_icon
from frontend.assets.functions.ShadowText import *

import sys, pyodbc, atexit


class StartWindow(QMainWindow):


    def __init__(self):
        super(StartWindow, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)


        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.lightModeToggler = self.findChild(QLabel, "StartWindow_LightModeToggler")
        self.darkModeToggler = self.findChild(QLabel, "StartWindow_DarkModeToggler")
        self.textLayout = self.findChild(QVBoxLayout, "StartWindow_TextLayout")
        self.mainHeadingLabel = self.findChild(QLabel, "StartWindow_MainHeadingLabel")
        self.mainTextLabel = self.findChild(QLabel, "StartWindow_MainTextLabel")

        headingShadow = QGraphicsDropShadowEffect()
        applyBlur(headingShadow, 15)
        changeShadowColor(headingShadow, QColor(38, 38, 38))
        positionShadow(headingShadow, 0, 2)

        textShadow = QGraphicsDropShadowEffect()
        applyBlur(textShadow, 15)
        changeShadowColor(textShadow, QColor(38, 38, 38))
        positionShadow(textShadow, 0, 2)

        self.mainHeadingLabel.setGraphicsEffect(headingShadow)
        self.mainTextLabel.setGraphicsEffect(textShadow)

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def toggleLightMode():
            '''
            This is used to change the border-image of the
            MainWindow to the light-mode-bg
            :return:
            '''

            self.setStyleSheet("QMainWindow {border-image: url('frontend/assets/imgs/light-mode-bg.png')}")

            self.lightModeToggler.setFixedWidth(0)
            self.darkModeToggler.setFixedWidth(45)


        def toggleDarkMode():
            '''
            This is used to change the border-image of the
            MainWindow to the dark-mode-bg
            :return:
            '''

            self.setStyleSheet("QMainWindow {border-image: url('frontend/assets/imgs/dark-mode-bg.png')}")

            self.lightModeToggler.setFixedWidth(45)
            self.darkModeToggler.setFixedWidth(0)

        def exitApp():
            '''
            This is used to close the app
            :return:
            '''

            atexit.register(cleanup_connections) # Making the function run ALWAYS when exiting

            #closeConnectionToDB(self)
            sys.exit()



        # Apply functions to/style widgets
        self.lightModeToggler.mousePressEvent = lambda event: toggleLightMode()
        self.darkModeToggler.mousePressEvent = lambda event: toggleDarkMode()

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

def main():
    app = QApplication(sys.argv)
    UIWindow = StartWindow()
    UIWindow.show()
    app.exec_()