# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QDate
from datetime import date
from window import *

class App(QMainWindow, MainWindow):
    def __init__(self, pas, language, db, windowTitle):
        super(App, self).__init__()
        self.windowTitle = windowTitle
        self.db = db
        self.cursor = self.db.cursor()
        self.cursor.execute("set SQL_SAFE_UPDATES = 0;")
        self.db.commit()
        self.language = language
        self.setupUi_main()

    def setupUi_main(self):
        self.setupUi(self)
        self.debt_add_name_input.setFocus()
        self.debt_add_search_func()
        self.debt_search_search_func()
        self.check_in_search_search_func()
        self.person_search_search_func()

        # Messageboxs
        # Correct messagebox
        self.correct_msgBox = QMessageBox()
        self.correct_msgBox.setWindowTitle(self.windowTitle)
        self.correct_msgBox.addButton(QMessageBox.Ok)
        self.correct_msgBox.setIconPixmap(QPixmap("tick.png"))

        # Comfirm messagebox
        self.comfirm_msgBox = QMessageBox()
        self.comfirm_msgBox.setIcon(QMessageBox.Question)
        self.comfirm_msgBox.setWindowTitle(self.windowTitle)
        self.comfirm_msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        
        # Delete debt messagebox
        self.delete_msgBox = QMessageBox()
        self.delete_msgBox.setIcon(QMessageBox.Question)
        self.delete_msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Check in quantity
        self.check_in_Quantity_msgBox = QMessageBox()
        self.check_in_Quantity_msgBox.setIcon(QMessageBox.Question)
        self.check_in_Quantity_msgBox.setWindowTitle(self.windowTitle)
        self.check_in_Quantity_msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Check in day exist 
        self.check_in_exist_msgBox = QMessageBox()
        self.check_in_exist_msgBox.setIcon(QMessageBox.Question)
        self.check_in_exist_msgBox.setWindowTitle(self.windowTitle)
        self.check_in_exist_msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        # Person exist
        self.person_add_exist_msgBox = QMessageBox()
        self.person_add_exist_msgBox.setIcon(QMessageBox.Critical)
        self.person_add_exist_msgBox.setWindowTitle(self.windowTitle)

        # Person add input is empty
        self.person_add_empty_msgBox = QMessageBox()
        self.person_add_empty_msgBox.setIcon(QMessageBox.Critical)
        self.person_add_empty_msgBox.setWindowTitle(self.windowTitle)

        # Functions
        # debt_add_search_func()
        self.debt_add_search_button.clicked.connect(self.debt_add_search_func)
        self.debt_add_name_input.returnPressed.connect(self.debt_add_search_func)
        self.debt_add_number_input.returnPressed.connect(self.debt_add_search_func)
        
        # debt_add_add_func()
        self.debt_add_add_button.clicked.connect(self.debt_add_add_func)
        self.debt_add_thing_input.returnPressed.connect(self.debt_add_add_func)

        # debt_search_search_func()
        self.debt_search_search_button.clicked.connect(self.debt_search_search_func)
        self.debt_search_name_input.returnPressed.connect(self.debt_search_search_func)
        self.debt_search_number_input.returnPressed.connect(self.debt_search_search_func)
        self.debt_search_description_input.returnPressed.connect(self.debt_search_search_func)

        # debt_search_delete_func()
        self.debt_search_delete_button.clicked.connect(self.debt_search_delete_func)

        # check_in_add_add_func()
        self.check_in_add_add_button.clicked.connect(self.check_in_add_add_func)

        # check_in_search_search_func()
        self.check_in_search_search_button.clicked.connect(self.check_in_search_search_func)

        # person_add_add_func()
        self.person_add_add_button.clicked.connect(self.person_add_add_func)
        self.person_add_name_input.returnPressed.connect(self.person_add_add_func)
        self.person_add_description_input.returnPressed.connect(self.person_add_add_func)

        # person_search_search_func()
        self.person_search_search_button.clicked.connect(self.person_search_search_func)
        self.person_search_name_input.returnPressed.connect(self.person_search_search_func)
        self.person_search_number_input.returnPressed.connect(self.person_search_search_func)
        self.person_search_description_input.returnPressed.connect(self.person_search_search_func)

        # person_search_cliked_func()
        self.person_search_table.itemDoubleClicked.connect(self.person_search_cliked_func)

        self.retranslateUi_main()

    def debt_add_search_func(self):
        name = self.debt_add_name_input.text().strip()
        number = self.debt_add_number_input.text().strip()
        things = self.debt_add_thing_input.text().strip()
        if not self.check_input(self.debt_add_name_input) and not self.check_input(self.debt_add_number_input):
            command = "select id, nombre, descripcion from persona;"
        else:
            command = "select id, nombre, descripcion from persona where id like '%"+number+"%' and nombre like '%"+name+"%';"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        if self.check_result(result, self.debt_add_table):
            self.debt_add_table.setCurrentCell(0,0)

    def debt_add_add_func(self):
        command = "insert into deuda(id_persona, cuantia, productos, fecha_endeudado) values(%s, %s, '%s', date(now()));"
        number, name, description = [i .text() for i in self.debt_add_table.selectedItems()]
        quantity = self.debt_add_quantity_input.value()
        products = self.debt_add_thing_input.text() 
        self.comfirm_msgBox.setText(self.comfirm_msgBox_text % (name, description, quantity, products))
        result = self.comfirm_msgBox.exec_()
        if result == QMessageBox.Yes:
            self.cursor.execute(command % (number, quantity, products))
            self.db.commit()
            self.debt_add_name_input.clear()
            self.debt_add_number_input.clear()
            self.debt_add_thing_input.clear()
            self.debt_add_quantity_input.setValue(0)
            self.debt_add_search_func()
            self.person_search_search_func()
            self.debt_search_search_func()

    def debt_search_search_func(self):
        begin_date = str(self.debt_search_begin_date.date().toString("yyyy-MM-dd"))
        end_date = str(self.debt_search_end_date.date().toString("yyyy-MM-dd"))
        name = self.debt_search_name_input.text().strip()
        number = self.debt_search_number_input.text().strip()
        description = self.debt_search_description_input.text().strip()
        command = "select id, nombre, fecha_endeudado, cuantia, productos from persona left join deuda on deuda.id_persona = persona.id where nombre like '%"+name+"%' and id_persona like '%"+number+"%' and descripcion like '%"+description+"%' and fecha_endeudado >= date('"+begin_date+"') and fecha_endeudado <= date('"+end_date+"') and fecha_pagado is Null;"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        if self.check_result(result, self.debt_search_table):
            self.debt_search_table.setCurrentCell(0, 0)
    
    def debt_search_delete_func(self):
        number, name, debt_date, quantity, products = [i.text().strip() for i in self.debt_search_table.selectedItems()]
        self.cursor.execute("select descripcion from persona where id = %s" % number)
        description = self.cursor.fetchall()
        command = "update deuda set fecha_pagado = date(now()) where id_persona = "+number+" and cuantia >= "+quantity+" and cuantia < "+str(float(quantity)+0.01)+" and fecha_endeudado = date('"+debt_date+"') and productos like '%"+products+"%';"
        self.delete_msgBox.setText(self.delete_msgBox_text % (name,description[0][0],quantity,products,debt_date))
        result = self.delete_msgBox.exec_()
        if result == QMessageBox.Yes:
            self.cursor.execute(command)
            self.db.commit()
            self.debt_search_name_input.clear()
            self.debt_search_number_input.clear()
            self.debt_search_description_input.clear()
            self.debt_search_begin_date.setDate(QDate(QDate(2017, 1, 1)))
            self.debt_search_end_date.setDate(QDate.currentDate())
            self.debt_search_search_func()
            self.person_search_search_func()

    def check_in_add_add_func(self):
        date = str(self.check_in_add_date.date().toString("yyyy-MM-dd"))
        command = "insert into facturacion(fecha, cuantia) values(date('%s'), %s)"
        self.cursor.execute("select count(fecha) from facturacion where fecha = date('%s');" % (date))
        is_exist = False
        quantity = False
        continu = True
        if self.check_in_add_quantity.value() < 200:
            quantity = True
            askBox = self.check_in_Quantity_msgBox.exec_()
            if askBox == QMessageBox.Yes:
                quantity = False
            else:
                continu = False
        if self.cursor.fetchone()[0] > 0 and continu:
            is_exist = True
            existBox = self.check_in_exist_msgBox.exec_()
            if existBox == QMessageBox.Yes:
                is_exist = False
                command = "update facturacion set fecha = date('%s'), cuantia = %f where fecha = date('"+date+"')"
        if not is_exist and not quantity:
            self.cursor.execute(command % (date, float(self.check_in_add_quantity.value())))
            self.db.commit()
            QMessageBox.information(self, self.windowTitle, "Ok！")
            self.check_in_search_search_func()

    def check_in_search_search_func(self):
        command = "select fecha, cuantia from facturacion where fecha >= '%s' and fecha <= '%s'"
        self.cursor.execute(command % (self.check_in_search_begin_date.date().toString("yyyy-MM-dd"), self.check_in_search_end_date.date().toString("yyyy-MM-dd")))
        result = self.cursor.fetchall()
        self.show_table(self.check_in_search_table, result)

    # Agregar persona
    def person_add_add_func(self):
        name, description = self.person_add_name_input, self.person_add_description_input
        command = "insert into persona(nombre, descripcion) values (%s, %s)"
        if self.check_input((name, description)):
            self.cursor.execute("select id from persona where nombre = '%s' and descripcion = '%s'" % (name.text(), description.text()))
            result = self.cursor.fetchone()
            if result != None:
                self.person_add_exist_msgBox.exec_()
            else:
                self.cursor.execute(command, (name.text(), description.text()))
                self.db.commit()
                self.correct_msgBox.exec_()
                self.person_add_description_input.clear()
                self.person_add_name_input.clear()
        else:
            self.person_add_empty_msgBox.exec_()

    def person_search_search_func(self):
        name = self.person_search_name_input.text().strip()
        number = self.person_search_number_input.text().strip()
        description = self.person_search_description_input.text().strip()
        if not self.check_input(self.person_search_number_input) and not self.check_input(self.person_search_description_input) and not self.check_input(self.person_search_name_input):
            command = "select id, nombre, sum(cuantia), descripcion from persona left join deuda on deuda.id_persona = persona.id and fecha_pagado is Null group by id;"
        else:
            command = "select id, nombre, sum(cuantia), descripcion from persona left join deuda on deuda.id_persona = persona.id where nombre like '%"+name+"%' and id like '%"+number+"%' and descripcion like '%"+description+"%' and fecha_pagado is Null group by id;"
        self.cursor.execute(command)
        result = self.cursor.fetchall()
        if self.check_result(result, self.person_search_table):
            self.person_search_table.setCurrentCell(0, 0)
     
    def person_search_cliked_func(self):
        number, name, quantity, description = [i.text() for i in self.person_search_table.selectedItems()]
        if quantity != "":
            command = "select id, nombre, fecha_endeudado, cuantia, productos from persona left join deuda on deuda.id_persona = persona.id where nombre like '%"+name+"%' and id_persona like '%"+number+"%' and descripcion like '%"+description+"%' and fecha_endeudado >= date('2017-01-01') and fecha_endeudado <= date(now()) and fecha_pagado is Null;"
            self.cursor.execute(command)
            result = self.cursor.fetchall()
            self.show_table(self.debt_search_table, result)
            self.section.setCurrentIndex(0)

    # Chequea si es vacio el resultado  
    def check_result(self, result, table):
        if len(result) < 1:
            table.setRowCount(0)
            return False
        else:
            self.show_table(table, result)
            return True

    # Chequea si está vacío el input
    def check_input(self, items):
        if not isinstance(items, tuple):
            if items.text() != "":
                pass
            else:
                return False
        else:
            for i in items:
                if i.text() != "":
                    pass
                else:
                    return False
        return True
        
    # Mostrar en tabla
    def show_table(self, table, items):
        end = False
        check_in_table = False
        table.setRowCount(0)
        total = 0.0
        for i in range(0,len(items)):
            table.insertRow(i)
            for j in range(0,len(items[0])):
                try:
                    if items[i][j] == None:
                        table.setItem(i, j, QTableWidgetItem(""))
                    elif isinstance(items[i][j], date):
                        table.setItem(i, j, QTableWidgetItem("%s" % items[i][j]))
                    elif not str(items[i][j]).isalpha() and not str(items[i][j]).isnumeric():
                        try:
                            table.setItem(i, j, QTableWidgetItem("%.2f" % items[i][j]))
                        except TypeError:
                            table.setItem(i, j, QTableWidgetItem(str(items[i][j])))
                    else:
                        table.setItem(i, j, QTableWidgetItem(str(items[i][j])))
                except Exception as er:
                    end = True
                    print(er)
                    break
            if table.objectName() == "check_in_search_table":
                total += float(items[i][1])
                check_in_table = True
        if check_in_table:
            self.check_in_search_total_input.setEnabled(True)
            self.check_in_search_total_input.setText(str(total))
            self.check_in_search_total_input.setEnabled(False)

    def retranslateUi_main(self):
        if self.language == "es":
            self.correct_msgBox.setText("Creación exitoso!")
            self.comfirm_msgBox_text = "Comfirmación de deuda: \n Nombre: %s \n Descripción: %s \n Cuantía: %s \n Productos: %s"
            self.delete_msgBox_text = "Comfirmación de eliminación: \n Nombre: %s \n Descripción: %s \n Cuantía: %s \n Productos: %s \n Fecha endeudado: %s"
            self.check_in_Quantity_msgBox.setText("Tan poco?")
            self.check_in_exist_msgBox.setText("Ya existe el día, ¿desea reemplazarlo?")
            self.person_add_empty_msgBox.setText("Para crear una persona se necesita\nintroducir todos los campos!")
            self.person_add_exist_msgBox.setText("Ya existe el usuario!")
        else:
            self.correct_msgBox.setText("创建成功！")
            self.comfirm_msgBox_text = "确定添加欠款: \n 客户名: %s \n 客户介绍: %s \n 欠款数目: %s \n 欠款物品: %s"
            self.delete_msgBox_text = "确定删除欠款: \n 客户名: %s \n 客户介绍: %s \n 欠款数目: %s \n 欠款物品: %s \n 欠款日期: %s"
            self.check_in_Quantity_msgBox.setText("这么少?")
            self.check_in_exist_msgBox.setText("此日期已存在, 需要覆盖吗?")
            self.person_add_empty_msgBox.setText("创建人物, 需要填写任何一项信息。")
            self.person_add_exist_msgBox.setText("此人物已存在！")
