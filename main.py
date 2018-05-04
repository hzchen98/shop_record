# 日期： 2018年4月14日
# 软件名： 店面记录 1.0

# -*- coding: utf-8 -*-

from login import *
from language import *
from app import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from sys import argv, exit
import sys
from os import path
import MySQLdb

def main():
    host = "localhost"
    user = "root"
    windowTitle = "店面记录 1.0"
    app = QApplication(argv)
    app.setStyle("fusion")
    app.setWindowIcon(QIcon("icon.png"))
    language = LanguageBox(windowTitle)
    if language.exec_() == QDialog.Accepted:
        login = Login(language.language, host, user, windowTitle)
        if login.exec_() == QtWidgets.QDialog.Accepted: 
            try:
                window = App(login.password, language.language, login.db, windowTitle)
                window.show()
                exit(app.exec_())
            except Exception as e:
                print(e)
                login.db.close()
            else:
                window.db.close()
            finally:
                pass

if __name__ == '__main__':
    main()
