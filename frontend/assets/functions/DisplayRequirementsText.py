

from frontend.assets.functions.DetectRequiredPrograms import detect_required_programs

def disableBtns(self):
    '''
    This is used to disable the buttons
    :param self:
    :return:
    '''

    self.registerBtn.setEnabled(False)
    self.registerBtn.setStyleSheet("QPushButton { background-color: rgba(239, 152, 72, 0.1); border-image: none; color: rgba(0,0,0,0.4); }")
    self.loginBtn.setEnabled(False)
    self.loginBtn.setStyleSheet("QPushButton { background-color: rgba(239, 152, 72, 0.1); border-image: none; color: rgba(0,0,0,0.4); }")


def display_success_error_label(self):
    '''
    This is used to display a specific label based on certain criteas
    :param self:
    :return:
    '''

    check_for_required_programs = detect_required_programs(self)

    # Error label(s)
    if check_for_required_programs == "SSMS was not found":
        disableBtns(self)

        self.requirementsLabel.setText("Error: SSMS was not found.")

        #self.sSMSNotDetectedLabel.show()

        # self.sSMSNotDetectedLabel.setMaximumHeight(50)
        # self.sSMSNotDetectedLabel.setMinimumHeight(50)

    if check_for_required_programs == "ODBC was not found":
        disableBtns(self)

        self.requirementsLabel.setText("Error: ODBC was not found.")

        #self.oDBCNotDetectedLabel.show()
        # self.oDBCNotDetectedLabel.setMaximumHeight(50)
        # self.oDBCNotDetectedLabel.setMinimumHeight(50)

    if check_for_required_programs == "Both programs were not found":
        disableBtns(self)

        self.requirementsLabel.setText("Error: Both programs were not found.")

        #self.bothNotDetectedLabel.show()
        # self.bothNotDetectedLabel.setMaximumHeight(50)
        # self.bothNotDetectedLabel.setMinimumHeight(50)

    if check_for_required_programs == "Only SSMS and Drivers were found, not database and tables.":
        disableBtns(self)

        self.requirementsLabel.setText("Error: Only SSMS and Drivers were found, not database and/or tables.")

        #self.onlySSMSDriversFoundLabel.show()
        # self.onlySSMSDriversFoundLabel.setMaximumHeight(50)
        # self.onlySSMSDriversFoundLabel.setMinimumHeight(50)

    # Success label
    if check_for_required_programs == "All requirements were found":

        self.requirementsLabel.setText("Success! All requirements were found.")

        #self.bothDetectedLabel.show()
        # self.bothDetectedLabel.setMaximumHeight(50)
        # self.bothDetectedLabel.setMinimumHeight(50)