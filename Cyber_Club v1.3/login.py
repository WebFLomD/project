# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Александр\Desktop\test\Cyber_Club\UI\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginWindow(object):

    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(400, 565)
        LoginWindow.setMinimumSize(QtCore.QSize(400, 565))
        LoginWindow.setMaximumSize(QtCore.QSize(400, 565))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/LOGO_icon_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LoginWindow.setWindowIcon(icon)
        LoginWindow.setStyleSheet("background-color: #151819;")
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo_club = QtWidgets.QLabel(self.frame)
        self.logo_club.setMinimumSize(QtCore.QSize(200, 125))
        self.logo_club.setMaximumSize(QtCore.QSize(200, 125))
        self.logo_club.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo_club.setStyleSheet("background-image: url(:/newPrefix/LOGO/LOGO_2.3.2.png);")
        self.logo_club.setText("")
        self.logo_club.setPixmap(QtGui.QPixmap(":/newPrefix/img/LOGO_2.3.4.png"))
        self.logo_club.setScaledContents(True)
        self.logo_club.setAlignment(QtCore.Qt.AlignCenter)
        self.logo_club.setObjectName("logo_club")
        self.horizontalLayout.addWidget(self.logo_club)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.walcome = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(23)
        self.walcome.setFont(font)
        self.walcome.setStyleSheet("color: #fff;")
        self.walcome.setAlignment(QtCore.Qt.AlignCenter)
        self.walcome.setObjectName("walcome")
        self.verticalLayout_3.addWidget(self.walcome)
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 17))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: red;")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.login = QtWidgets.QLineEdit(self.frame_4)
        self.login.setMaximumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(15)
        self.login.setFont(font)
        self.login.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.login.setText("")
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 2, 0, 1, 1)
        self.text_login = QtWidgets.QLabel(self.frame_4)
        self.text_login.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.text_login.setFont(font)
        self.text_login.setStyleSheet("color: #fff;")
        self.text_login.setObjectName("text_login")
        self.gridLayout.addWidget(self.text_login, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.password = QtWidgets.QLineEdit(self.frame_6)
        self.password.setMaximumSize(QtCore.QSize(300, 45))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.password.setText("")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout_2.addWidget(self.password, 1, 0, 1, 1)
        self.text_password = QtWidgets.QLabel(self.frame_6)
        self.text_password.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(20)
        self.text_password.setFont(font)
        self.text_password.setStyleSheet("color: #fff;")
        self.text_password.setObjectName("text_password")
        self.gridLayout_2.addWidget(self.text_password, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.enter = QtWidgets.QPushButton(self.frame_5)

        self.enter.setMaximumSize(QtCore.QSize(175, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(15)
        self.enter.setFont(font)
        self.enter.setStyleSheet("QPushButton{\n"
"background-color: rgb(255, 255, 255);\n"
"color: #4E4E4E;\n"
"border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:  rgb(204, 5, 0);\n"
"color: #fff;\n"
"}")
        self.enter.setObjectName("enter")
        self.gridLayout_3.addWidget(self.enter, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Логин"))
        self.walcome.setText(_translate("LoginWindow", "Добро пожаловать!"))
        self.text_login.setText(_translate("LoginWindow", "Логин"))
        self.text_password.setText(_translate("LoginWindow", "Пароль"))
        self.enter.setText(_translate("LoginWindow", "Войти"))
        
import icon_and_logo_py.Logo_rc # Подключение Лого
