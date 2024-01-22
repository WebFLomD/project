# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Александр\Desktop\Cyber_Club\UI\exit.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExitWindow(object):
        
##### ОКНО ВХОД В СИСТЕМУ ###############################

    def openLoginWindow(self):
        from start import MainWindow
        self.ui = MainWindow()
        self.ui.show()
    
##### ОКНО ГЛАВНОЕ #######################################

    def openMainWindow(self):
        from main_staff import Ui_StaffMainWindow
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_StaffMainWindow()
        self.ui.setupUi(self.window1)
        self.window1.show()
        
##########################################################
        
    def setupUi(self, ExitWindow):
        ExitWindow.setObjectName("ExitWindow")
        ExitWindow.resize(900, 450)
        ExitWindow.setMinimumSize(QtCore.QSize(900, 450))
        ExitWindow.setMaximumSize(QtCore.QSize(900, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/img/LOGO_icon_4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExitWindow.setWindowIcon(icon)
        ExitWindow.setStyleSheet("background-color: #2D2D2D;")
        self.centralwidget = QtWidgets.QWidget(ExitWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setStyleSheet("background-color: rgb(166, 49, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.title = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(25)
        self.title.setFont(font)
        self.title.setStyleSheet("color: #ffffff;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 1000))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.text = QtWidgets.QFrame(self.frame_2)
        self.text.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.text.setFrameShadow(QtWidgets.QFrame.Raised)
        self.text.setObjectName("text")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.text)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.text)
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #ffffff;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.text)
        self.btn_exit = QtWidgets.QFrame(self.frame_2)
        self.btn_exit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_exit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.btn_exit)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
######### ВЫЙТИ ########################################################

        # КНОПКА ВЫЙТИ - Находим эту строчку
        self.btn_yes = QtWidgets.QPushButton(self.btn_exit)
        
        # Добаляемя
        # ПРИ НАЖАТИ ОТКРЫВАЕТ ОКНО ВХОД
        self.btn_yes.clicked.connect(self.openLoginWindow)
        
        # ЗАКРЫВАЕТ ТЕКУЩЕЕ ОКНО
        self.btn_yes.clicked.connect(ExitWindow.close)
        
##########################################################################

        self.btn_yes.setMaximumSize(QtCore.QSize(200, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.btn_yes.setFont(font)
        self.btn_yes.setStyleSheet("QPushButton{\n"
"background-color: rgb(224, 65, 61);\n"
"color: #fff;\n"
"border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(204, 5, 0);\n"
"}")
        self.btn_yes.setObjectName("btn_yes")
        self.horizontalLayout_2.addWidget(self.btn_yes)
        
######### ОТМЕНА ########################################################

        # КНОПКА ОТМЕНА - Находим эту строчку
        self.btn_no = QtWidgets.QPushButton(self.btn_exit)
        
        # Добавляем
        # ПРИ НАЖАТИ ОТКРЫВАЕТ ГЛАВНОЕ ОКНО
        self.btn_no.clicked.connect(self.openMainWindow)
        
        # ЗАКРЫВАЕТ ТЕКУЩЕЕ ОКНО
        self.btn_no.clicked.connect(ExitWindow.close)
        
##########################################################################

        self.btn_no.setMaximumSize(QtCore.QSize(200, 55))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(18)
        self.btn_no.setFont(font)
        self.btn_no.setStyleSheet("QPushButton{\n"
"background-color: rgb(224, 65, 61);\n"
"color: #fff;\n"
"border-radius: 14px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(204, 5, 0);\n"
"}")
        self.btn_no.setObjectName("btn_no")
        self.horizontalLayout_2.addWidget(self.btn_no)
        self.verticalLayout_2.addWidget(self.btn_exit)
        self.verticalLayout.addWidget(self.frame_2)
        ExitWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExitWindow)
        QtCore.QMetaObject.connectSlotsByName(ExitWindow)

    def retranslateUi(self, ExitWindow):
        _translate = QtCore.QCoreApplication.translate
        ExitWindow.setWindowTitle(_translate("ExitWindow", "Выход"))
        self.title.setText(_translate("ExitWindow", "Выйти с аккаунта"))
        self.label.setText(_translate("ExitWindow", "Вы точно хотите закончить смену?"))
        self.btn_yes.setText(_translate("ExitWindow", "Выйти"))
        self.btn_no.setText(_translate("ExitWindow", "Отмена"))
        
import icon_and_logo_py.Logo_rc # Подключение Лого
