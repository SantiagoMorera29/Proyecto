# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mante.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(805, 747)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_superior = QtWidgets.QFrame(self.frame)
        self.frame_superior.setMinimumSize(QtCore.QSize(0, 42))
        self.frame_superior.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"    background-color: #000000ff;\n"
"    border-radius:20px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius:20px;\n"
"}\n"
"")
        self.frame_superior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_superior.setObjectName("frame_superior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_superior)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_menu = QtWidgets.QPushButton(self.frame_superior)
        self.bt_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QtCore.QSize(38, 38))
        self.bt_menu.setObjectName("bt_menu")
        self.horizontalLayout.addWidget(self.bt_menu)
        spacerItem = QtWidgets.QSpacerItem(457, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt_minimizar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_minimizar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("extender.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_minimizar.setIcon(icon1)
        self.bt_minimizar.setIconSize(QtCore.QSize(38, 38))
        self.bt_minimizar.setObjectName("bt_minimizar")
        self.horizontalLayout.addWidget(self.bt_minimizar)
        self.bt_colapsar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_colapsar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("contraer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_colapsar.setIcon(icon2)
        self.bt_colapsar.setIconSize(QtCore.QSize(38, 38))
        self.bt_colapsar.setObjectName("bt_colapsar")
        self.horizontalLayout.addWidget(self.bt_colapsar)
        self.bt_cerrar = QtWidgets.QPushButton(self.frame_superior)
        self.bt_cerrar.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("cerrar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cerrar.setIcon(icon3)
        self.bt_cerrar.setIconSize(QtCore.QSize(38, 38))
        self.bt_cerrar.setObjectName("bt_cerrar")
        self.horizontalLayout.addWidget(self.bt_cerrar)
        self.verticalLayout_2.addWidget(self.frame_superior)
        self.frame_contenido = QtWidgets.QFrame(self.frame)
        self.frame_contenido.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_contenido.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_contenido.setObjectName("frame_contenido")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_contenido)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_menu = QtWidgets.QFrame(self.frame_contenido)
        self.frame_menu.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_menu.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(0, 206, 151);\n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:white;\n"
"    border-top-left-radius:20px;\n"
"    border-bottom-left-radius:20px;\n"
"    color: rgb(0,0,0);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bt_database = QtWidgets.QPushButton(self.frame_menu)
        self.bt_database.setMinimumSize(QtCore.QSize(0, 40))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("base de datos.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_database.setIcon(icon4)
        self.bt_database.setIconSize(QtCore.QSize(30, 30))
        self.bt_database.setObjectName("bt_database")
        self.verticalLayout_3.addWidget(self.bt_database)
        self.bt_registrar = QtWidgets.QPushButton(self.frame_menu)
        self.bt_registrar.setMinimumSize(QtCore.QSize(0, 40))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("filtro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_registrar.setIcon(icon5)
        self.bt_registrar.setIconSize(QtCore.QSize(30, 30))
        self.bt_registrar.setObjectName("bt_registrar")
        self.verticalLayout_3.addWidget(self.bt_registrar)
        self.bt_actualizar = QtWidgets.QPushButton(self.frame_menu)
        self.bt_actualizar.setMinimumSize(QtCore.QSize(0, 40))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("lapiz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_actualizar.setIcon(icon6)
        self.bt_actualizar.setIconSize(QtCore.QSize(30, 30))
        self.bt_actualizar.setObjectName("bt_actualizar")
        self.verticalLayout_3.addWidget(self.bt_actualizar)
        self.bt_eliminar = QtWidgets.QPushButton(self.frame_menu)
        self.bt_eliminar.setMinimumSize(QtCore.QSize(0, 40))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_eliminar.setIcon(icon7)
        self.bt_eliminar.setIconSize(QtCore.QSize(30, 30))
        self.bt_eliminar.setObjectName("bt_eliminar")
        self.verticalLayout_3.addWidget(self.bt_eliminar)
        self.bt_program = QtWidgets.QPushButton(self.frame_menu)
        self.bt_program.setMinimumSize(QtCore.QSize(0, 40))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("descargar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_program.setIcon(icon8)
        self.bt_program.setIconSize(QtCore.QSize(30, 30))
        self.bt_program.setObjectName("bt_program")
        self.verticalLayout_3.addWidget(self.bt_program)
        self.horizontalLayout_2.addWidget(self.frame_menu)
        self.frame_paginas = QtWidgets.QFrame(self.frame_contenido)
        self.frame_paginas.setStyleSheet("QFrame{\n"
"    \n"
"    background-color: rgb(61, 61, 61);\n"
"}\n"
"QLabel{\n"
"    font: 87 14pt \"Arial Black\";\n"
"    background-color:#000000ff;\n"
"    color: rgb(0, 206, 151);\n"
"    border:0px solid #14C8DC;\n"
"}\n"
"QLineEdit{\n"
"    border:0px;\n"
"    color: rgb(255, 255, 255);\n"
"    border-bottom:2px solid  rgb(61, 61, 61);\n"
"    font: 75 14pt \"Times New Roman\";\n"
"    \n"
"}\n"
"QPushButton{\n"
"    background-color: rgb(61, 61, 61);\n"
"    border-radius:15px;\n"
"    color: rgb(255, 255, 255);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:rgb(0, 206, 151);\n"
"    border-radius:15px;\n"
"    color: rgb(0,0,0);\n"
"    font: 77 10pt \"Arial Black\";\n"
"}\n"
"\n"
"QTableWidget{\n"
"    background-color:rgb(255, 255, 255);\n"
"    color: rgb(0,0,0);\n"
"    gridline-color: rgb(0, 206, 151);\n"
"    border:0px;\n"
"    color: rgb(255, 255, 255);\n"
"    font-size: 12pt;\n"
"    color: #000000;\n"
"}\n"
"QHeaderView::section{\n"
"    background-color:rgb(0, 206, 151);\n"
"    border:1px solid rgb(0,0,0);\n"
"    font-size:12pt;\n"
"}\n"
"QTableWidgetQTableCornerButton::section{\n"
"    background-color:rgb(0,0,0);\n"
"    border:1px solid rgb(0, 206, 151);\n"
"}\n"
"")
        self.frame_paginas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_paginas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_paginas.setObjectName("frame_paginas")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_paginas)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_paginas)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_eliminar = QtWidgets.QWidget()
        self.page_eliminar.setObjectName("page_eliminar")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_eliminar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.page_eliminar)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_17 = QtWidgets.QLabel(self.page_eliminar)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_eliminar)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.horizontalLayout_10.addWidget(self.lineEdit_12)
        self.bt_pgElim_consul = QtWidgets.QPushButton(self.page_eliminar)
        self.bt_pgElim_consul.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_pgElim_consul.setObjectName("bt_pgElim_consul")
        self.horizontalLayout_10.addWidget(self.bt_pgElim_consul)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.tb_Elim = QtWidgets.QTableWidget(self.page_eliminar)
        self.tb_Elim.setObjectName("tb_Elim")
        self.tb_Elim.setColumnCount(0)
        self.tb_Elim.setRowCount(0)
        self.verticalLayout.addWidget(self.tb_Elim)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_23 = QtWidgets.QLabel(self.page_eliminar)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_6.addWidget(self.label_23)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.bt_pgElim_save = QtWidgets.QPushButton(self.page_eliminar)
        self.bt_pgElim_save.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_pgElim_save.setObjectName("bt_pgElim_save")
        self.horizontalLayout_6.addWidget(self.bt_pgElim_save)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.page_eliminar)
        self.page_actualizar = QtWidgets.QWidget()
        self.page_actualizar.setObjectName("page_actualizar")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_actualizar)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_16 = QtWidgets.QLabel(self.page_actualizar)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_15 = QtWidgets.QLabel(self.page_actualizar)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_9.addWidget(self.label_15)
        self.txb_pgAct_NOrd = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_NOrd.setObjectName("txb_pgAct_NOrd")
        self.horizontalLayout_9.addWidget(self.txb_pgAct_NOrd)
        self.bt_pgAct_consul = QtWidgets.QPushButton(self.page_actualizar)
        self.bt_pgAct_consul.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_pgAct_consul.setObjectName("bt_pgAct_consul")
        self.horizontalLayout_9.addWidget(self.bt_pgAct_consul)
        self.verticalLayout_11.addLayout(self.horizontalLayout_9)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.page_actualizar)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_9.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.page_actualizar)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_9.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.page_actualizar)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_9.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.page_actualizar)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_9.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.page_actualizar)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.horizontalLayout_7.addLayout(self.verticalLayout_9)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.txb_pgAct_plac = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_plac.setObjectName("txb_pgAct_plac")
        self.verticalLayout_10.addWidget(self.txb_pgAct_plac)
        self.txb_pgAct_fech = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_fech.setObjectName("txb_pgAct_fech")
        self.verticalLayout_10.addWidget(self.txb_pgAct_fech)
        self.txb_pgAct_km = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_km.setObjectName("txb_pgAct_km")
        self.verticalLayout_10.addWidget(self.txb_pgAct_km)
        self.txb_pgAct_trab = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_trab.setObjectName("txb_pgAct_trab")
        self.verticalLayout_10.addWidget(self.txb_pgAct_trab)
        self.txb_pgAct_rep = QtWidgets.QLineEdit(self.page_actualizar)
        self.txb_pgAct_rep.setObjectName("txb_pgAct_rep")
        self.verticalLayout_10.addWidget(self.txb_pgAct_rep)
        self.horizontalLayout_7.addLayout(self.verticalLayout_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_11.addItem(spacerItem4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_14 = QtWidgets.QLabel(self.page_actualizar)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_8.addWidget(self.label_14)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.bt_pgAct_save = QtWidgets.QPushButton(self.page_actualizar)
        self.bt_pgAct_save.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_pgAct_save.setObjectName("bt_pgAct_save")
        self.horizontalLayout_8.addWidget(self.bt_pgAct_save)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.stackedWidget.addWidget(self.page_actualizar)
        self.page_registrar = QtWidgets.QWidget()
        self.page_registrar.setObjectName("page_registrar")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_registrar)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.page_registrar)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("font: 87 16pt \"Arial Black\";")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(30)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.page_registrar)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.page_registrar)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.page_registrar)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.label_1 = QtWidgets.QLabel(self.page_registrar)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_6.addWidget(self.label_1)
        self.label_3 = QtWidgets.QLabel(self.page_registrar)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.txb_pgReg_cod = QtWidgets.QLineEdit(self.page_registrar)
        self.txb_pgReg_cod.setMinimumSize(QtCore.QSize(40, 30))
        self.txb_pgReg_cod.setObjectName("txb_pgReg_cod")
        self.verticalLayout_7.addWidget(self.txb_pgReg_cod)
        self.txb_pgReg_fech = QtWidgets.QLineEdit(self.page_registrar)
        self.txb_pgReg_fech.setMinimumSize(QtCore.QSize(40, 30))
        self.txb_pgReg_fech.setObjectName("txb_pgReg_fech")
        self.verticalLayout_7.addWidget(self.txb_pgReg_fech)
        self.txb_pgReg_km = QtWidgets.QLineEdit(self.page_registrar)
        self.txb_pgReg_km.setMinimumSize(QtCore.QSize(40, 30))
        self.txb_pgReg_km.setObjectName("txb_pgReg_km")
        self.verticalLayout_7.addWidget(self.txb_pgReg_km)
        self.txb_pgReg_trab = QtWidgets.QLineEdit(self.page_registrar)
        self.txb_pgReg_trab.setMinimumSize(QtCore.QSize(40, 30))
        self.txb_pgReg_trab.setObjectName("txb_pgReg_trab")
        self.verticalLayout_7.addWidget(self.txb_pgReg_trab)
        self.txb_pgReg_rep = QtWidgets.QLineEdit(self.page_registrar)
        self.txb_pgReg_rep.setMinimumSize(QtCore.QSize(40, 30))
        self.txb_pgReg_rep.setObjectName("txb_pgReg_rep")
        self.verticalLayout_7.addWidget(self.txb_pgReg_rep)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem8)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.page_registrar)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.bt_pgReg_save = QtWidgets.QPushButton(self.page_registrar)
        self.bt_pgReg_save.setObjectName("bt_pgReg_save")
        self.horizontalLayout_5.addWidget(self.bt_pgReg_save)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.stackedWidget.addWidget(self.page_registrar)
        self.page_program = QtWidgets.QWidget()
        self.page_program.setObjectName("page_program")
        self.stackedWidget.addWidget(self.page_program)
        self.page_base_datos = QtWidgets.QWidget()
        self.page_base_datos.setObjectName("page_base_datos")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_base_datos)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QtWidgets.QLabel(self.page_base_datos)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_5.addWidget(self.label)
        self.tabla_orden_pgBD = QtWidgets.QTableWidget(self.page_base_datos)
        self.tabla_orden_pgBD.setObjectName("tabla_orden_pgBD")
        self.tabla_orden_pgBD.setColumnCount(5)
        self.tabla_orden_pgBD.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_orden_pgBD.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_orden_pgBD.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_orden_pgBD.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_orden_pgBD.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_orden_pgBD.setHorizontalHeaderItem(4, item)
        self.verticalLayout_5.addWidget(self.tabla_orden_pgBD)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_18 = QtWidgets.QLabel(self.page_base_datos)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_3.addWidget(self.label_18)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.bt_pgBD_refrescar = QtWidgets.QPushButton(self.page_base_datos)
        self.bt_pgBD_refrescar.setMinimumSize(QtCore.QSize(120, 30))
        self.bt_pgBD_refrescar.setObjectName("bt_pgBD_refrescar")
        self.horizontalLayout_3.addWidget(self.bt_pgBD_refrescar)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.stackedWidget.addWidget(self.page_base_datos)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_paginas)
        self.verticalLayout_2.addWidget(self.frame_contenido)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 8)
        self.horizontalLayout_14.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bt_database.setText(_translate("MainWindow", "BASE DE DATOS"))
        self.bt_registrar.setText(_translate("MainWindow", "REGISTRAR"))
        self.bt_actualizar.setText(_translate("MainWindow", "ACTUALIZAR"))
        self.bt_eliminar.setText(_translate("MainWindow", "ELIMINAR"))
        self.bt_program.setText(_translate("MainWindow", "PROGRAMACIÓN"))
        self.label_4.setText(_translate("MainWindow", "Eliminar"))
        self.label_17.setText(_translate("MainWindow", "Numero de Orden"))
        self.bt_pgElim_consul.setText(_translate("MainWindow", "Consultar"))
        self.label_23.setText(_translate("MainWindow", "Eliminar Registro"))
        self.bt_pgElim_save.setText(_translate("MainWindow", "Guardar"))
        self.label_16.setText(_translate("MainWindow", "Actualizar"))
        self.label_15.setText(_translate("MainWindow", "Numero de Orden"))
        self.bt_pgAct_consul.setText(_translate("MainWindow", "CONSULTAR"))
        self.label_9.setText(_translate("MainWindow", "Placa"))
        self.label_10.setText(_translate("MainWindow", "Fecha"))
        self.label_11.setText(_translate("MainWindow", "Kilometraje"))
        self.label_12.setText(_translate("MainWindow", "Trabajo"))
        self.label_13.setText(_translate("MainWindow", "Repuestos"))
        self.label_14.setText(_translate("MainWindow", "Guardar Cambios"))
        self.bt_pgAct_save.setText(_translate("MainWindow", "Actualizar"))
        self.label_7.setText(_translate("MainWindow", "Registro de mantenimientos"))
        self.label_2.setText(_translate("MainWindow", "Codigo"))
        self.label_6.setText(_translate("MainWindow", "Fecha"))
        self.label_5.setText(_translate("MainWindow", "Kilometraje"))
        self.label_1.setText(_translate("MainWindow", "Trabajo"))
        self.label_3.setText(_translate("MainWindow", "Repuestos"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.bt_pgReg_save.setText(_translate("MainWindow", "GUARDAR"))
        self.label.setText(_translate("MainWindow", "Ordenes de Trabajo"))
        item = self.tabla_orden_pgBD.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Placa"))
        item = self.tabla_orden_pgBD.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.tabla_orden_pgBD.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Kilometraje"))
        item = self.tabla_orden_pgBD.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Trabajo"))
        item = self.tabla_orden_pgBD.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Repuesto"))
        self.label_18.setText(_translate("MainWindow", "Actualizar"))
        self.bt_pgBD_refrescar.setText(_translate("MainWindow", "REFRESCAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
