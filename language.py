# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont, QIcon
from sys import argv

class LanguageBox(QtWidgets.QDialog):
    def __init__(self, windowTitle, parent=None):
        super(LanguageBox, self).__init__(parent)
        self.windowTitle = windowTitle
        self.setFixedSize(290, 178)
        self.language_es_img = QtWidgets.QLabel(self)
        self.language_es_img.setGeometry(QtCore.QRect(10, 40, 120, 80))
        self.language_es_img.setObjectName("language_es_img")
        self.language_es_img.setPixmap(QPixmap("language_es.png"))
        self.language_label = QtWidgets.QLabel(self)
        self.language_label.setGeometry(QtCore.QRect(30, 10, 231, 21))
        font = QFont()
        font.setFamily("Miriam Libre")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.language_label.setFont(font)
        self.language_label.setObjectName("language_label")
        self.language_ch_img = QtWidgets.QLabel(self)
        self.language_ch_img.setGeometry(QtCore.QRect(160, 40, 120, 80))
        self.language_ch_img.setObjectName("language_ch_img")
        self.language_ch_img.setPixmap(QPixmap("language_ch.png"))
        self.language_es = QtWidgets.QRadioButton(self)
        self.language_es.setGeometry(QtCore.QRect(60, 130, 16, 17))
        self.language_es.setText("")
        self.language_es.setObjectName("language_es")
        self.language_ch = QtWidgets.QRadioButton(self)
        self.language_ch.setGeometry(QtCore.QRect(215, 130, 31, 17))
        self.language_ch.setText("")
        self.language_ch.setObjectName("language_ch")
        self.language_button = QtWidgets.QPushButton(self)
        self.language_button.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.language_button.setObjectName("language_button")
        self.language_button.clicked.connect(self.start_app)
        self.language_ch.click()
        self.language = "ch"

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, languageBox):
        _translate = QtCore.QCoreApplication.translate
        languageBox.setWindowTitle(_translate("languageBox", self.windowTitle))
        self.language_label.setText(_translate("languageBox", "language / lenguaje / 语言"))
        self.language_button.setText(_translate("languageBox", "Ok"))

    def start_app(self):
        if self.language_es.isChecked():
            self.language = "es"
        else:
            self.language = "ch"
        self.accept()
