# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'userlogin.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from userregister import Ui_registerWindow
import sqlite3

class Ui_loginWindow(object):
        def setupUi(self, loginWindow):
                loginWindow.setObjectName("loginWindow")
                loginWindow.setWindowModality(QtCore.Qt.NonModal)
                loginWindow.setEnabled(True)
                loginWindow.resize(669, 346)
                loginWindow.setMinimumSize(QtCore.QSize(390, 303))
                loginWindow.setAutoFillBackground(False)
                loginWindow.setStyleSheet("font: 12pt \"MS UI Gothic\";\n"
"selection-color: rgb(124, 255, 234);\n"
"background-color: rgb(16, 88, 204);")
                loginWindow.setAnimated(True)
                loginWindow.setDocumentMode(False)
                loginWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
                self.centralwidget = QtWidgets.QWidget(loginWindow)
                self.centralwidget.setAutoFillBackground(False)
                self.centralwidget.setStyleSheet("")
                self.centralwidget.setObjectName("centralwidget")
                self.loginButton = QtWidgets.QPushButton(self.centralwidget)
                self.loginButton.setGeometry(QtCore.QRect(80, 210, 93, 28))
                self.loginButton.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.loginButton.setObjectName("loginButton")
                ################
                self.loginButton.clicked.connect(self.login)
                ################
                self.closeButton = QtWidgets.QPushButton(self.centralwidget)
                self.closeButton.setGeometry(QtCore.QRect(150, 250, 93, 28))
                self.closeButton.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
                self.closeButton.setObjectName("closeButton")
                self.userLabel = QtWidgets.QLabel(self.centralwidget)
                self.userLabel.setGeometry(QtCore.QRect(80, 110, 101, 16))
                self.userLabel.setStyleSheet("color: rgb(255, 255, 255);")
                self.userLabel.setObjectName("userLabel")
                self.passLabel = QtWidgets.QLabel(self.centralwidget)
                self.passLabel.setGeometry(QtCore.QRect(80, 160, 101, 16))
                self.passLabel.setStyleSheet("color: rgb(255, 255, 255);")
                self.passLabel.setObjectName("passLabel")
                self.userLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.userLineEdit.setGeometry(QtCore.QRect(170, 110, 161, 22))
                self.userLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.userLineEdit.setInputMask("")
                self.userLineEdit.setText("")
                self.userLineEdit.setObjectName("userLineEdit")
                self.passLineEdit = QtWidgets.QLineEdit(self.centralwidget)
                self.passLineEdit.setGeometry(QtCore.QRect(170, 160, 161, 22))
                self.passLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.passLineEdit.setObjectName("passLineEdit")
            ##########
                self.passLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            ##########
                
                self.pushButton = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton.setGeometry(QtCore.QRect(220, 210, 93, 28))
                self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
                self.pushButton.setObjectName("pushButton")
            #########
                self.pushButton.clicked.connect(self.reg)
            #########
                self.userLabel_2 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_2.setGeometry(QtCore.QRect(170, 30, 311, 21))
                self.userLabel_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_2.setObjectName("userLabel_2")
                self.userLabel_3 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_3.setGeometry(QtCore.QRect(400, 70, 91, 21))
                self.userLabel_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_3.setObjectName("userLabel_3")
                self.userLabel_4 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_4.setGeometry(QtCore.QRect(400, 100, 401, 21))
                self.userLabel_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_4.setObjectName("userLabel_4")
                self.userLabel_5 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_5.setGeometry(QtCore.QRect(400, 130, 401, 21))
                self.userLabel_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_5.setObjectName("userLabel_5")
                self.userLabel_6 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_6.setGeometry(QtCore.QRect(400, 160, 401, 21))
                self.userLabel_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_6.setObjectName("userLabel_6")
                self.userLabel_7 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_7.setGeometry(QtCore.QRect(400, 190, 401, 21))
                self.userLabel_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_7.setObjectName("userLabel_7")
                self.userLabel_8 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_8.setGeometry(QtCore.QRect(400, 220, 401, 21))
                self.userLabel_8.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_8.setObjectName("userLabel_8")
                self.userLabel_9 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_9.setGeometry(QtCore.QRect(400, 250, 401, 21))
                self.userLabel_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_9.setObjectName("userLabel_9")
                self.userLabel_10 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_10.setGeometry(QtCore.QRect(400, 280, 401, 21))
                self.userLabel_10.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_10.setObjectName("userLabel_10")
                self.userLabel_11 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_11.setGeometry(QtCore.QRect(170, 0, 311, 21))
                self.userLabel_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS UI Gothic\";")
                self.userLabel_11.setObjectName("userLabel_11")
                self.userLabel_12 = QtWidgets.QLabel(self.centralwidget)
                self.userLabel_12.setGeometry(QtCore.QRect(160, 70, 101, 16))
                self.userLabel_12.setStyleSheet("color: rgb(255, 255, 255);")
                self.userLabel_12.setObjectName("userLabel_12")
                loginWindow.setCentralWidget(self.centralwidget)
                self.menubar = QtWidgets.QMenuBar(loginWindow)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 669, 26))
                self.menubar.setObjectName("menubar")
                loginWindow.setMenuBar(self.menubar)
                self.statusbar = QtWidgets.QStatusBar(loginWindow)
                self.statusbar.setObjectName("statusbar")
                loginWindow.setStatusBar(self.statusbar)

                self.retranslateUi(loginWindow)
                ################
                self.closeButton.clicked.connect(loginWindow.close)
                ################
                QtCore.QMetaObject.connectSlotsByName(loginWindow)

        def login(self):
                username = self.userLineEdit.text()
                password = self.passLineEdit.text()
                
                con = sqlite3.connect("userlogin.db")
                cur = con.cursor()
         #  res = con.execute('SELECT * FROM admin WHERE username = ? AND password = ?',(username,password))
                cur.execute('SELECT * FROM admin WHERE username = ? AND password = ?',(username,password))
                data = cur.fetchone()
                con.commit()
         #  if(len(res.fetchall()) > 0) 
                if data != None:
                       import main.py
                else:
                        QMessageBox.information(loginWindow,"no user ","invalid user or pass" ,QMessageBox.Ok)
                con.close()
                
        def reg(self):
                self.registerWindow = QtWidgets.QMainWindow()
                self.ui = Ui_registerWindow()
                self.ui.setupUi(self.registerWindow)
                self.registerWindow.show()
                    
        def retranslateUi(self, loginWindow):
                _translate = QtCore.QCoreApplication.translate
                loginWindow.setWindowTitle(_translate("loginWindow", "User Login"))
                self.loginButton.setText(_translate("loginWindow", "Login"))
                self.closeButton.setText(_translate("loginWindow", "Close"))
                self.userLabel.setText(_translate("loginWindow", "Username:"))
                self.passLabel.setText(_translate("loginWindow", "Password:"))
                self.pushButton.setText(_translate("loginWindow", "Register"))
                self.userLabel_2.setText(_translate("loginWindow", "COE125 - C1 - 1Q1920 Group 3 & 4 "))
                self.userLabel_3.setText(_translate("loginWindow", "Members:"))
                self.userLabel_4.setText(_translate("loginWindow", "Christian Benedict Gaba"))
                self.userLabel_5.setText(_translate("loginWindow", "Jerome Nel Ganitnit"))
                self.userLabel_6.setText(_translate("loginWindow", "Bien Carlo Halili"))
                self.userLabel_7.setText(_translate("loginWindow", "Carmelo John Ilag"))
                self.userLabel_8.setText(_translate("loginWindow", "Khayam Khan"))
                self.userLabel_9.setText(_translate("loginWindow", "Bjarne Magturo"))
                self.userLabel_10.setText(_translate("loginWindow", "Gian Perez"))
                self.userLabel_11.setText(_translate("loginWindow", "American Sign Language Translator"))
                self.userLabel_12.setText(_translate("loginWindow", "Login"))

         

if __name__ == "__main__":
        print ("Everything Passed!")
        import sys
        app = QtWidgets.QApplication(sys.argv)
        loginWindow = QtWidgets.QMainWindow()
        ui = Ui_loginWindow()
        ui.setupUi(loginWindow)
        loginWindow.show()
        sys.exit(app.exec_())
