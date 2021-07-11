##pymysql library
import pymysql
##inporting time library
import time

from PyQt5 import QtCore, QtGui, QtWidgets
##for message box
from PyQt5.QtWidgets import QMessageBox

##database connection
db=pymysql.connect(host="localhost",user="root",password="medbeds@123",database="Medbeds")
cur=db.cursor()


##function for error message
def error():
        msg=QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Wrong Input!")
        msg.exec_()

##function for displaying the live status
def live_status(dept,hosp,time,date):
    if(hosp=='ruby' or hosp=='Ruby' or hosp=='RUBY'):
        extract="select * from ruby_dummy"
        cur.execute(extract)
    elif(hosp=='amri' or hosp=='Amri' or hosp=='AMRI'):
        extract="select * from amri_dummy"
        cur.execute(extract)
    else:
        error()
        exit()

    #flag for indicating record found
    f=0         

    for i in cur:
        if(i[0]==dept and i[1]==date and i[2]==time):
            beds_occ=i[3]
            beds_vac=i[4]
            print(beds_occ,beds_vac)
            f=f+1
            print(f)
        
        elif(f==0):
            beds_occ='NA'
            beds_vac='NA'

    return beds_occ,beds_vac
            

    

class Ui_OtherWindow(object):
    def setupUi(self, OtherWindow):

        OtherWindow.setObjectName("OtherWindow")
        OtherWindow.resize(499, 592)
        OtherWindow.setStyleSheet("background-color: qconicalgradient(cx:1, cy:0, angle:0, stop:0 rgba(35, 40, 3, 255), stop:0.16 rgba(136, 106, 22, 255), stop:0.225 rgba(166, 140, 41, 255), stop:0.285 rgba(204, 181, 74, 255), stop:0.345 rgba(235, 219, 102, 255), stop:0.415 rgba(245, 236, 112, 255), stop:0.52 rgba(209, 190, 76, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.635 rgba(168, 142, 42, 255), stop:0.695 rgba(202, 174, 68, 255), stop:0.75 rgba(218, 202, 86, 255), stop:0.815 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255), stop:1 rgba(35, 40, 3, 255));")
        self.centralwidget = QtWidgets.QWidget(OtherWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(37, 49, 57);")
        self.label_5.setObjectName("label_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 380, 121, 21))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_9.setObjectName("label_9")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(300, 420, 161, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_7.setGeometry(QtCore.QRect(50, 420, 161, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(270, 110, 201, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 160, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(37, 49, 57);")
        self.label_6.setObjectName("label_6")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 160, 201, 31))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(37, 49, 57);")
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(270, 210, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgb(37, 49, 57);")
        self.label_10.setObjectName("label_10")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 250, 201, 31))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(70, 380, 121, 21))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(270, 250, 201, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 441, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 330, 441, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 300, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 480, 131, 23))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_8.setGeometry(QtCore.QRect(50, 510, 411, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textBrowser_8.setObjectName("textBrowser_8")

        OtherWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 499, 21))
        self.menubar.setObjectName("menubar")
        OtherWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow)
        self.statusbar.setObjectName("statusbar")
        OtherWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OtherWindow)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow)


        ##function for accepting the line edit values
        def input_values():
            d_name=self.lineEdit.text()
            h_name=self.lineEdit_2.text()            
            curr_time=self.lineEdit_3.text()
            curr_date=self.lineEdit_4.text()


            print(d_name,h_name,curr_date,curr_time)

            occ_beds,vac_beds = live_status(d_name,h_name,curr_time,curr_date)
            print(occ_beds,vac_beds)
            ##clearing pre-exixting values in text browser
            self.textBrowser_6.clear()
            self.textBrowser_7.clear()            
            ##displaying the values in textbrowser
            self.textBrowser_6.append(str(occ_beds))
            self.textBrowser_7.append(str(vac_beds))

        ##function for displaying the token
        def token_num():
            token= time.time()
            self.textBrowser_8.clear()
            self.textBrowser_8.append("Note down the token for reference in hospital. It will be invalid after 24 Hrs")
            self.textBrowser_8.append(str(token))


        ##accepting the values on button click
        self.pushButton.clicked.connect(input_values)  

        ##generating token
        self.pushButton_2.clicked.connect(token_num)



    def retranslateUi(self, OtherWindow):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow.setWindowTitle(_translate("OtherWindow", "MainWindow"))
        self.label_5.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Department Name :-</span></p></body></html>"))
        self.label_9.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Occupied Beds</span></p></body></html>"))
        self.label_6.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Hospital Name:-</span></p></body></html>"))
        self.label_7.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Time(HH:MMAM/PM):-</span></p></body></html>"))
        self.label_10.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Date(MM/DD/YYYY):-</span></p></body></html>"))
        self.label_11.setText(_translate("OtherWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600; color:#ffffff;\">Vacant Beds</span></p></body></html>"))
        self.label.setText(_translate("OtherWindow", "PLEASE ENTER THE FOLLOWING DETAILS:-"))
        self.pushButton.setText(_translate("OtherWindow", "SEARCH"))
        self.pushButton_2.setText(_translate("OtherWindow", "BOOK AND GET TOKEN"))        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow()
    ui.setupUi(OtherWindow)
    OtherWindow.show()
    sys.exit(app.exec_())
