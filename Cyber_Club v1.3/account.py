# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\account.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp, Qt
from PyQt5.QtGui import QRegExpValidator, QKeySequence
from PyQt5.QtWidgets import QShortcut

# Подключение БД
import mysql.connector as mc

mydb = mc.connect(
     host="localhost",
     user="root",
     password="",
     database="club"
)
print("Успешное подключение БД - Регистрация гостя")
mycursor = mydb.cursor()


class Ui_AccountWindow(object):
    def setupUi(self, AccountWindow):
        AccountWindow.setObjectName("AccountWindow")
        AccountWindow.resize(450, 725)
        AccountWindow.setMinimumSize(QtCore.QSize(450, 725))
        AccountWindow.setMaximumSize(QtCore.QSize(450, 725))
        AccountWindow.setSizeIncrement(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/LOGO_icon_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AccountWindow.setWindowIcon(icon)
        AccountWindow.setStyleSheet("background-color: #151819;")
        self.centralwidget = QtWidgets.QWidget(AccountWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QFrame(self.centralwidget)
        self.title.setMaximumSize(QtCore.QSize(16777215, 100))
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.title)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.title)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.title)
        self.line.setMaximumSize(QtCore.QSize(400, 2))
        self.line.setStyleSheet("background-color: rgb(127, 127, 127);")
        self.line.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.title)
        self.frame_1 = QtWidgets.QFrame(self.centralwidget)
        self.frame_1.setStyleSheet("")
        self.frame_1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_1.setObjectName("frame_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.info = QtWidgets.QFrame(self.frame_1)
        self.info.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info.setObjectName("info")
        self.gridLayout = QtWidgets.QGridLayout(self.info)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setObjectName("gridLayout")

###################

        self.input_phone = QtWidgets.QLineEdit(self.info)
        self.input_phone.textChanged.connect(self.phone)

##################

        self.input_phone.setMaximumSize(QtCore.QSize(325, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.input_phone.setFont(font)
        self.input_phone.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.input_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.input_phone.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.input_phone.setObjectName("input_phone")
        self.gridLayout.addWidget(self.input_phone, 9, 0, 1, 1)
        self.text_phone = QtWidgets.QLabel(self.info)
        self.text_phone.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(17)
        self.text_phone.setFont(font)
        self.text_phone.setStyleSheet("color: #fff;")
        self.text_phone.setObjectName("text_phone")
        self.gridLayout.addWidget(self.text_phone, 8, 0, 1, 1)
        self.text_phone_2 = QtWidgets.QLabel(self.info)
        self.text_phone_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(17)
        self.text_phone_2.setFont(font)
        self.text_phone_2.setStyleSheet("color: #fff;")
        self.text_phone_2.setObjectName("text_phone_2")
        self.gridLayout.addWidget(self.text_phone_2, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.info)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: red;")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 14, 0, 1, 1)
        self.text_pass = QtWidgets.QLabel(self.info)
        self.text_pass.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(17)
        self.text_pass.setFont(font)
        self.text_pass.setStyleSheet("color: #fff;")
        self.text_pass.setObjectName("text_pass")
        self.gridLayout.addWidget(self.text_pass, 4, 0, 1, 1)

######################

        self.input_fio = QtWidgets.QLineEdit(self.info)
        self.input_fio.textChanged.connect(self.fio)

######################

        self.input_fio.setMaximumSize(QtCore.QSize(325, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.input_fio.setFont(font)
        self.input_fio.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.input_fio.setText("")
        self.input_fio.setCursorPosition(0)
        self.input_fio.setAlignment(QtCore.Qt.AlignCenter)
        self.input_fio.setObjectName("input_fio")
        self.gridLayout.addWidget(self.input_fio, 1, 0, 1, 1)
        self.text_email = QtWidgets.QLabel(self.info)
        self.text_email.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(17)
        self.text_email.setFont(font)
        self.text_email.setStyleSheet("color: #fff;")
        self.text_email.setObjectName("text_email")
        self.gridLayout.addWidget(self.text_email, 10, 0, 1, 1)

####################

        self.input_email = QtWidgets.QLineEdit(self.info)
        self.input_email.textChanged.connect(self.email)

####################

        self.input_email.setMaximumSize(QtCore.QSize(325, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.input_email.setFont(font)
        self.input_email.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.input_email.setText("")
        self.input_email.setCursorPosition(0)
        self.input_email.setAlignment(QtCore.Qt.AlignCenter)
        self.input_email.setObjectName("input_email")
        self.gridLayout.addWidget(self.input_email, 11, 0, 1, 1)
        self.text_login = QtWidgets.QLabel(self.info)
        self.text_login.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(17)
        self.text_login.setFont(font)
        self.text_login.setStyleSheet("color: #fff;")
        self.text_login.setObjectName("text_login")
        self.gridLayout.addWidget(self.text_login, 0, 0, 1, 1)

##############

        self.input_login = QtWidgets.QLineEdit(self.info)
        self.input_login.textChanged.connect(self.login)

###############

        self.input_login.setMaximumSize(QtCore.QSize(325, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.input_login.setFont(font)
        self.input_login.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.input_login.setText("")
        self.input_login.setCursorPosition(0)
        self.input_login.setAlignment(QtCore.Qt.AlignCenter)
        self.input_login.setObjectName("input_login")
        self.gridLayout.addWidget(self.input_login, 5, 0, 1, 1)

###############

        self.input_login_2 = QtWidgets.QLineEdit(self.info)
        self.input_login_2.textChanged.connect(self.data_born)

###############

        self.input_login_2.setMaximumSize(QtCore.QSize(325, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.input_login_2.setFont(font)
        self.input_login_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.input_login_2.setText("")
        self.input_login_2.setCursorPosition(0)
        self.input_login_2.setAlignment(QtCore.Qt.AlignCenter)
        self.input_login_2.setObjectName("input_login_2")
        self.gridLayout.addWidget(self.input_login_2, 3, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.info)
        self.btn = QtWidgets.QFrame(self.frame_1)
        self.btn.setMaximumSize(QtCore.QSize(16777215, 100))
        self.btn.setSizeIncrement(QtCore.QSize(0, 1000))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn.setFont(font)
        self.btn.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn.setObjectName("btn")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.btn)
        self.horizontalLayout.setObjectName("horizontalLayout")

#####################

        self.btn_add = QtWidgets.QPushButton(self.btn)
        self.btn_add.clicked.connect(self.insert_data)

#####################

        self.btn_add.setMaximumSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(15)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("QPushButton{\n"
"background-color: rgb(224, 65, 61);\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #690200;\n"
"}")
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)

###############

        self.btn_cancel = QtWidgets.QPushButton(self.btn)
        self.btn_cancel.clicked.connect(AccountWindow.close)

###############

        self.btn_cancel.setMaximumSize(QtCore.QSize(170, 50))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(15)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setStyleSheet("QPushButton{\n"
"background-color: rgb(224, 65, 61);\n"
"color: #fff;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #690200;\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout_2.addWidget(self.btn)
        self.verticalLayout.addWidget(self.frame_1)
        AccountWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AccountWindow)
        QtCore.QMetaObject.connectSlotsByName(AccountWindow)

####################### БД #################################################

    def insert_data(self):

        fio = self.input_fio.text()
        data_born = self.input_login_2.text()
        login = self.input_login.text()
        phone = self.input_phone.text()
        email = self.input_email.text()

        if len(fio) == 0:
            self.label_2.setText("Введите ФИО!")
            return
        
        if len(data_born) == 0:
            self.label_2.setText("Введите дату рождения!")
            return
        
        if len(login) == 0:
            self.label_2.setText("Введите/придумайте Логин!")
            return
        
        if len(phone) == 0:
            self.label_2.setText("Введите номер телефона!")
            return
        
        if len(email) == 0:
            self.label_2.setText("Введите Email!")
            return

        mycursor.execute(f'SELECT fio FROM `clients` WHERE (fio = "{fio}") OR (login = "{login}")')
        if mycursor.fetchone() is None:
            query = "INSERT INTO clients (fio, data_born, login, phone, email) VALUES (%s, %s, %s, %s, %s)"
            value = (fio, data_born, login, phone, email)
            mycursor.execute(query, value)
            mydb.commit()
            
            self.label_2.setText("Успешно добавлено!")
            
        else:
            self.label_2.setText("Такой аккаут уже есть!")

######## Ограничитель ###############################

# ФИО   
    def fio(self):
        reg_ex = QRegExp("[а-я А-Я]{500}")
        input_validator = QRegExpValidator(reg_ex, self.input_fio)
        self.input_fio.setValidator(input_validator)

# Дата рождения
    def data_born(self):
        reg_ex = QRegExp("[0-9.]{10}")
        input_validator = QRegExpValidator(reg_ex, self.input_login_2)
        self.input_login_2.setValidator(input_validator)

# Логин
    def login(self):
        reg_ex = QRegExp("[a-zA-Z_0-9]{25}")
        input_validator = QRegExpValidator(reg_ex, self.input_login)
        self.input_login.setValidator(input_validator)

# Телефон
    def phone(self):
        reg_ex = QRegExp("[0-9 +()-]{20}")
        input_validator = QRegExpValidator(reg_ex, self.input_phone)
        self.input_phone.setValidator(input_validator)

# Email
    def email(self):
        reg_ex = QRegExp("[a-zA-Z@._0-9]{100}")
        input_validator = QRegExpValidator(reg_ex, self.input_email)
        self.input_email.setValidator(input_validator)

######################################################


    def retranslateUi(self, AccountWindow):
        _translate = QtCore.QCoreApplication.translate
        AccountWindow.setWindowTitle(_translate("AccountWindow", "Регистрация гостя"))
        self.label.setText(_translate("AccountWindow", "Реристрация гостя"))
        self.input_phone.setPlaceholderText(_translate("AccountWindow", "+7 999 123-45-67"))
        self.text_phone.setText(_translate("AccountWindow", "Телефон"))
        self.text_phone_2.setText(_translate("AccountWindow", "Дата рождения"))
        self.text_pass.setText(_translate("AccountWindow", "Логин"))
        self.input_fio.setPlaceholderText(_translate("AccountWindow", "ФИО"))
        self.text_email.setText(_translate("AccountWindow", "Почта"))
        self.input_email.setPlaceholderText(_translate("AccountWindow", "test123@gmail.com"))
        self.text_login.setText(_translate("AccountWindow", "ФИО"))
        self.input_login.setPlaceholderText(_translate("AccountWindow", "test1234"))
        self.input_login_2.setPlaceholderText(_translate("AccountWindow", "01.01.2000"))
        self.btn_add.setText(_translate("AccountWindow", "Добавить"))
        self.btn_cancel.setText(_translate("AccountWindow", "Отмена"))
import icon_and_logo_py.Logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AccountWindow = QtWidgets.QMainWindow()
    ui = Ui_AccountWindow()
    ui.setupUi(AccountWindow)
    AccountWindow.show()
    sys.exit(app.exec_())
