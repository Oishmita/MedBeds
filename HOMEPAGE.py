##pymysql library
import pymysql

from PyQt5 import QtCore, QtGui, QtWidgets
from DETAILSPAGE import *

##database connection
db=pymysql.connect(host="localhost",user="root",password="medbeds@123",database="Medbeds")
cur=db.cursor() 

class Ui_MainWindow(object):

    ##function to open the detailspage
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui=Ui_OtherWindow()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(573, 477)
        MainWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 491, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 151, 51))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(220, 120, 311, 211))
        self.textBrowser.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 380, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 190, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("border-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")

        ##for connecting to the other window on button click
        self.pushButton.clicked.connect(self.openWindow)

        ##function for displaying the different departments of different hospitals
        def display_list():
            query1="select distinct Department from amri_dummy"
            cur.execute(query1)
            self.textBrowser.append("AMRI Hospital\n")
            for i in cur:
                ##to display the hospital details in textbrowser
                self.textBrowser.append(i[0])

            query2="select distinct Department from ruby_dummy"
            cur.execute(query2)
            self.textBrowser.append("Ruby Hospital\n")
            for i in cur:
                ##to display the hospital details in textbrowser
                self.textBrowser.append(i[0])

            db.close()
            

        ##for displaying data in the browser as the button is clicked
        self.pushButton_2.clicked.connect(display_list)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 573, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; color:#000000;\">Welcome to MedBeds</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Hospital Details:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "BOOK A BED"))
        self.pushButton_2.setText(_translate("MainWindow", "CHECK HOSPITALS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
