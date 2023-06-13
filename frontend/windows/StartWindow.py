'''

    This is the Start Window

'''

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from backend.database.classes.Connection import db_connection

from frontend.assets.variables.arrays import active_connections
from frontend.assets.qrcs import light_bg, dark_bg, settings_icon, light_mode_icon, dark_mode_icon, start_window_bg
from frontend.assets.functions.ShadowText import *
from frontend.assets.functions.DisplayRequirementsText import display_success_error_label

import sys, pyodbc, atexit


class StartWindow(QMainWindow):


    def __init__(self):
        super(StartWindow, self).__init__()

        uic.loadUi("frontend/ui/StartWindow.ui", self)
        self.setWindowFlag(Qt.FramelessWindowHint)

        # Define widgets
        # EX: self.testWidget = self.findChild(QLineEdit, "startWindow_TestLE")
        self.lightModeToggler = self.findChild(QLabel, "StartWindow_LightModeToggler")
        self.darkModeToggler = self.findChild(QLabel, "StartWindow_DarkModeToggler")
        self.textLayout = self.findChild(QVBoxLayout, "StartWindow_TextLayout")
        self.mainHeadingLabel = self.findChild(QLabel, "StartWindow_MainHeadingLabel")
        self.mainTextLabel = self.findChild(QLabel, "StartWindow_MainTextLabel")
        self.requirementsLabel = self.findChild(QLabel, "StartWindow_RequirementsLabel")
        self.registerBtn = self.findChild(QPushButton, "StartWindow_RegisterBtn")
        self.loginBtn = self.findChild(QPushButton, "StartWindow_LoginBtn")
        self.exitBtn = self.findChild(QPushButton, "StartWindow_ExitBtn")
        self.topFrame = self.findChild(QFrame, "StartWindow_TopFrame")
        self.bottomFrame = self.findChild(QFrame, "StartWindow_BottomFrame")

        headingShadow = QGraphicsDropShadowEffect()
        applyBlur(headingShadow, 15)
        changeShadowColor(headingShadow, QColor(38, 38, 38))
        positionShadow(headingShadow, 0, 2)

        textShadow = QGraphicsDropShadowEffect()
        applyBlur(textShadow, 15)
        changeShadowColor(textShadow, QColor(38, 38, 38))
        positionShadow(textShadow, 0, 2)

        registerShadow = QGraphicsDropShadowEffect()
        applyBlur(registerShadow, 15)
        changeShadowColor(registerShadow, QColor(97, 69, 50))
        positionShadow(registerShadow, 0, 2)

        loginShadow = QGraphicsDropShadowEffect()
        applyBlur(loginShadow, 15)
        changeShadowColor(loginShadow, QColor(97, 69, 50))
        positionShadow(loginShadow, 0, 2)

        exitShadow = QGraphicsDropShadowEffect()
        applyBlur(exitShadow, 15)
        changeShadowColor(exitShadow, QColor(97, 69, 50))
        positionShadow(exitShadow, 0, 2)

        requirementsShadow = QGraphicsDropShadowEffect()
        applyBlur(requirementsShadow, 15)
        changeShadowColor(requirementsShadow, QColor(38, 38, 38))
        positionShadow(requirementsShadow, 0, 2)

        self.mainHeadingLabel.setGraphicsEffect(headingShadow)
        self.mainTextLabel.setGraphicsEffect(textShadow)
        self.requirementsLabel.setGraphicsEffect(requirementsShadow)
        self.registerBtn.setGraphicsEffect(registerShadow)
        self.loginBtn.setGraphicsEffect(loginShadow)
        self.exitBtn.setGraphicsEffect(exitShadow)

        # Define functions
        # EX: def doSomething():
        #       print("Test")

        def toggleLightMode():
            '''
            This is used to change the border-image of the
            MainWindow to the light-mode-bg
            :return:
            '''

            self.topFrame.setStyleSheet("QFrame {border-image: url('frontend/assets/imgs/light-mode-bg.png')}")
            self.bottomFrame.setStyleSheet("QFrame {border-image: url('frontend/assets/imgs/light-mode-bg.png')}")

            self.lightModeToggler.setFixedWidth(0)
            self.darkModeToggler.setFixedWidth(45)


        def toggleDarkMode():
            '''
            This is used to change the border-image of the
            MainWindow to the dark-mode-bg
            :return:
            '''

            self.topFrame.setStyleSheet("QFrame {border-image: url('frontend/assets/imgs/dark-mode-bg.png')}")
            self.bottomFrame.setStyleSheet("QFrame {border-image: url('frontend/assets/imgs/dark-mode-bg.png')}")

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
        self.exitBtn.clicked.connect(exitApp)

        # Displaying result of program detection
        display_success_error_label(self)

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