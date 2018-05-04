# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5.QtCore import QRect, QCoreApplication
import MySQLdb

class Login(QtWidgets.QDialog):
	def __init__(self, language, host, user, windowTitle, parent=None):
		super(Login, self).__init__(parent)
		self.host = host
		self.user = user
		self.windowTitle = windowTitle
		self.setFixedSize(450, 367)
		self.language = language
		self.textBrowser = QtWidgets.QTextBrowser(self)
		self.textBrowser.setEnabled(False)
		self.textBrowser.setGeometry(QRect(90, 10, 256, 91))
		self.textBrowser.setObjectName("textBrowser")
		self.label = QtWidgets.QLabel(self)
		self.label.setGeometry(QRect(100, 170, 31, 41))
		self.label.setObjectName("label")
		self.lineEdit = QtWidgets.QLineEdit(self)
		self.lineEdit.setGeometry(QRect(140, 180, 141, 21))
		self.lineEdit.setInputMask("")
		self.lineEdit.setText("")
		self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
		self.lineEdit.setObjectName("lineEdit")
		self.lineEdit.returnPressed.connect(self.handleLogin)
		self.pushButton = QtWidgets.QPushButton(self)
		self.pushButton.setGeometry(QRect(180, 240, 75, 23))
		self.pushButton.setObjectName("pushButton")
		self.pushButton.clicked.connect(self.handleLogin)
		self.retranslateUi(self)

	def retranslateUi(self, MainWindow):
		_translate = QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", self.windowTitle))
		if self.language == "ch":
			self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
			"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
			"p, li { white-space: pre-wrap; }\n"
			"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">欢迎使用</span></p>\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">店面记录 1.0</span></p></body></html>"))
			self.label.setText(_translate("MainWindow", "密码："))
			self.pushButton.setText(_translate("MainWindow", "登陆"))
		else:
			self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
			"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
			"p, li { white-space: pre-wrap; }\n"
			"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Bienvenido a </span></p>\n"
			"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">店面记录 1.0</span></p></body></html>"))
			self.label.setText(_translate("MainWindow", "Contraseña:"))
			self.pushButton.setText(_translate("MainWindow", "Acceder"))

	def handleLogin(self):
		try:
		    self.db = MySQLdb.connect(host=self.host, user=self.user, password=self.lineEdit.text(), db="tienda", use_unicode=True, charset="utf8")
		    self.password = self.lineEdit.text()
		    self.accept()
		except Exception as er:
			if self.language == "ch":
			    QtWidgets.QMessageBox.critical(self, "错误", "密码错误 或 连接失败,\n 请重试！")
			else:
			    QtWidgets.QMessageBox.critical(self, "Error", "Contraseña erronea o conexión fallida,\n intente de nuevo！")