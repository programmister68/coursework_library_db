from PyQt5.QtCore import Qt, QTime, QDateTime
from PyQt5.QtWidgets import QTableWidgetItem
from database import Database
import logging
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

import datetime


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("forms/main.ui", self)
        self.exitButton.setIcon(QIcon('icons/power-off.png'))
        self.page = self.ui.stackedWidget_main
        self.page_id = [0]  # индексы доступных страничек после авторизации для сотрудника
        self.now_page = 0
        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.db = Database()

        self.ui.nextButton.clicked.connect(self.next_page)
        self.ui.backButton.clicked.connect(self.back_page)
        self.ui.exitButton.clicked.connect(self.exit)

        self.ui.add_dep.clicked.connect(self.new_deposit)
        self.ui.delete_dep.clicked.connect(self.delete_deposit)
        self.ui.save_dep.clicked.connect(self.save_deposit)

        self.ui.emp_add.clicked.connect(self.new_employee)
        self.ui.emp_delete.clicked.connect(self.delete_employee)
        self.ui.emp_save.clicked.connect(self.save_employee)

        self.ui.add_pos.clicked.connect(self.new_position)
        self.ui.delete_pos.clicked.connect(self.delete_position)
        self.ui.save_pos.clicked.connect(self.save_position)

        self.ui.depositor_add.clicked.connect(self.new_depositor)
        self.ui.depositor_delete.clicked.connect(self.delete_depositors)
        self.ui.depositor_save.clicked.connect(self.save_depositors)

        self.ui.curr_add.clicked.connect(self.new_currency)
        self.ui.curr_delete.clicked.connect(self.delete_currency)
        self.ui.curr_save.clicked.connect(self.save_currency)

        self.updateTableCurrencies()
        self.updateTablePositions()
        self.updateTableEmployees()
        self.updateTableDepositors()
        self.updateTableDeposits()

    def exit(self):
        self.now_page = 0
        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.hide()
        self.open_auth()

    def next_page(self):
        if self.now_page != len(self.page_id) - 1:
            self.now_page += 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def back_page(self):
        if self.now_page != 0:
            self.now_page -= 1
            self.page.setCurrentIndex(self.page_id[self.now_page])

    def open_auth(self):
        dialog = DialogAuth(self)
        dialog.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('icons/debit-card.png'))
        dialog.show()
        dialog.exec_()

#######################################################
    def updateTableCurrencies(self):
        self.table_currencies.clear()
        rec = self.db.selectCurrencies()
        self.ui.table_currencies.setColumnCount(3)
        self.ui.table_currencies.setRowCount(len(rec))
        self.ui.table_currencies.setHorizontalHeaderLabels(
            ['ID', 'Наименование', 'Обменный курс'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_currencies.setItem(i, x, item)

    def updateTablePositions(self):
        self.table_positions.clear()
        rec = self.db.selectPositions()
        self.ui.table_positions.setColumnCount(5)
        self.ui.table_positions.setRowCount(len(rec))
        self.ui.table_positions.setHorizontalHeaderLabels(
            ['ID', 'Наименование', 'Зарплата', 'Обязанности', 'Требования'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_positions.setItem(i, x, item)

    def updateTableDepositors(self):
        self.table_depositors.clear()
        rec = self.db.selectDepositors()
        self.ui.table_depositors.setColumnCount(10)
        self.ui.table_depositors.setRowCount(len(rec))
        self.ui.table_depositors.setHorizontalHeaderLabels(
            ['ID', 'ФИО', 'Телефон', 'Паспортные данные', 'Сумма вклада', 'Сумма возврата', 'Дата открытия вклада', 'Дата возврата', 'Статус возврата', 'Код сотрудника'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_depositors.setItem(i, x, item)

    def updateTableEmployees(self):
        self.table_employees.clear()
        rec = self.db.selectEmployees()
        self.ui.table_employees.setColumnCount(8)
        self.ui.table_employees.setRowCount(len(rec))
        self.ui.table_employees.setHorizontalHeaderLabels(
            ['ID', 'ФИО', 'Логин', 'Пароль', 'Роль', 'Телефон', 'Паспортные данные', 'Код Должности'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_employees.setItem(i, x, item)

    def updateTableDeposits(self):
        self.table_deposit.clear()
        rec = self.db.selectDeposits()
        self.ui.table_deposit.setColumnCount(5)
        self.ui.table_deposit.setRowCount(len(rec))
        self.ui.table_deposit.setHorizontalHeaderLabels(
            ['ID', 'Наименование', 'Процент', 'Код Валюты', 'Код Вкладчика'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_deposit.setItem(i, x, item)

    def getFromTableDeposits(self):
        rows = self.table_deposit.rowCount()
        cols = self.table_deposit.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_deposit.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableEmployees(self):
        rows = self.table_employees.rowCount()
        cols = self.table_employees.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_employees.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTablePositions(self):
        rows = self.table_positions.rowCount()
        cols = self.table_positions.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_positions.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableCurrencies(self):
        rows = self.table_currencies.rowCount()
        cols = self.table_currencies.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_currencies.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableDepositors(self):
        rows = self.table_depositors.rowCount()
        cols = self.table_depositors.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_depositors.item(row, col).text())
            data.append(tmp)
        return data

    def new_currency(self):
        curr_name = self.ui.curr_name.text()
        curr_ex_rate = float(self.ui.curr_ex_rate.text())

        self.db.insertCurrencies(curr_name, curr_ex_rate)
        self.updateTableCurrencies()

    def new_deposit(self):
        dep_name = self.ui.dep_name_line.text()
        percent_rate = float(self.ui.percent_line.text())
        curr_id = int(self.ui.id_curr_line.text())
        depositor_id = int(self.ui.id_depositor_line.text())

        self.db.insertDeposits(dep_name, percent_rate, curr_id, depositor_id)
        self.updateTableDeposits()

    def new_employee(self):
        emp_name = self.ui.add_fio_employee.text()
        login = self.ui.add_login.text()
        password = self.ui.add_password.text()
        role = self.ui.add_role.text()
        emp_phone = self.ui.add_phone_employee.text()
        emp_passport = self.ui.add_passport_employee.text()
        positions_id = self.ui.add_position.text()

        self.db.insertEmployees(emp_name, login, password, role, emp_phone, emp_passport, positions_id)
        self.updateTableEmployees()

    def new_position(self):
        pos_name = self.ui.pos_name.text()
        pos_salary = int(self.ui.pos_salary.text())
        pos_res = self.ui.pos_res.text()
        pos_req = self.ui.pos_req.text()

        self.db.insertPositions(pos_name, pos_salary, pos_res, pos_req)
        self.updateTablePositions()

    def new_depositor(self):
        depositor_fio = self.ui.depositor_fio.text()
        depositor_phone = self.ui.depositor_phone.text()
        depositor_passport = self.ui.depositor_passport.text()
        dep_sum = int(self.ui.dep_sum.text())
        refund_sum = int(self.ui.refund_sum.text())
        data_dep = self.ui.date_dep.dateTime().toString("yyyy-MM-dd")
        data_ref = self.ui.date_ref.dateTime().toString("yyyy-MM-dd")
        dep_status = self.ui.dep_status.text()
        id_emp_dep = int(self.id_emp_dep.text())

        self.db.insertDepositors(depositor_fio, depositor_phone, depositor_passport, dep_sum, refund_sum, data_dep, data_ref, dep_status, id_emp_dep)
        self.updateTableDepositors()

    def delete_currency(self):
        SelectedRow = self.table_currencies.currentRow()
        rowcount = self.table_currencies.rowCount()
        colcount = self.table_currencies.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_currencies.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_currencies.model().index(-1, -1)
            self.table_currencies.setCurrentIndex(ix)

    def delete_deposit(self):
        SelectedRow = self.table_deposit.currentRow()
        rowcount = self.table_deposit.rowCount()
        colcount = self.table_deposit.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_deposit.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_deposit.model().index(-1, -1)
            self.table_deposit.setCurrentIndex(ix)

    def delete_employee(self):
        SelectedRow = self.table_employees.currentRow()
        rowcount = self.table_employees.rowCount()
        colcount = self.table_employees.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_employees.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_employees.model().index(-1, -1)
            self.table_employees.setCurrentIndex(ix)

    def delete_position(self):
        SelectedRow = self.table_positions.currentRow()
        rowcount = self.table_positions.rowCount()
        colcount = self.table_positions.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_positions.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_positions.model().index(-1, -1)
            self.table_positions.setCurrentIndex(ix)

    def save_currency(self):
        data = self.getFromTableCurrencies()
        for string in data:
            if string[1] != '':
                self.db.updateCurrencies(int(string[0]), string[1], float(string[2]))
            else:
                self.db.deleteCurrencies(int(string[0]))
        self.updateTableCurrencies()

    def delete_depositors(self):
        SelectedRow = self.table_depositors.currentRow()
        rowcount = self.table_depositors.rowCount()
        colcount = self.table_depositors.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_depositors.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_depositors.model().index(-1, -1)
            self.table_depositors.setCurrentIndex(ix)

    def save_deposit(self):
        data = self.getFromTableDeposits()
        for string in data:
            if string[1] != '':
                self.db.updateDeposits(int(string[0]), string[1], float(string[2]), int(string[3]), int(string[4]))
            else:
                self.db.deleteDeposits(int(string[0]))
        self.updateTableDeposits()

    def save_employee(self):
        data = self.getFromTableEmployees()
        for string in data:
            if string[1] != '':
                self.db.updateEmployees(int(string[0]), string[1], string[2], string[3], string[4], string[5], string[6], int(string[7]))
            else:
                self.db.deleteEmployees(int(string[0]))
        self.updateTableEmployees()

    def save_position(self):
        data = self.getFromTablePositions()
        for string in data:
            if string[1] != '':
                self.db.updatePositions(int(string[0]), string[1], int(string[2]), string[3], string[4])
            else:
                self.db.deletePositions(int(string[0]))
        self.updateTablePositions()

    def save_depositors(self):
        data = self.getFromTableDepositors()
        for string in data:
            if string[1] != '':
                self.db.updateDepositors(int(string[0]), string[1], string[2], string[3], int(string[4]), int(string[5]), string[6], string[7], string[8], int(string[9]))
            else:
                self.db.deleteDepositors(int(string[0]))
        self.updateTableDepositors()


class DialogAuth(QDialog):
    def __init__(self, parent=None):
        super(DialogAuth, self).__init__(parent)
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowIcon(QIcon('icons/authentication.png'))
        self.scene = QGraphicsScene(0, 0, 300, 80)
        self.ui.btn_enter.clicked.connect(self.enter)
        self.btn_hide_password.setIcon(QIcon('icons/eye_close.png'))
        self.ui.btn_hide_password.clicked.connect(self.vis_pas)

        self.db = Database()

        self.next_try = 0
        self.vis_p = False

    def vis_pas(self):
        ed = self.ui.edit_password
        if self.vis_p:
            self.vis_p = False
            self.btn_hide_password.setIcon(QIcon('icons/eye_close.png'))
            ed.setEchoMode(QtWidgets.QLineEdit.Password)

        else:
            self.vis_p = True
            self.btn_hide_password.setIcon(QIcon('icons/eye.png'))
            ed.setEchoMode(QtWidgets.QLineEdit.Normal)

    def mes_box(self, text):
        self.messagebox = QMessageBox(self)
        self.messagebox.setWindowTitle("Ошибка")
        self.messagebox.setText(text)
        self.messagebox.setStandardButtons(QMessageBox.Ok)
        self.messagebox.show()

    def enter(self):
        auth_log = self.ui.edit_login.text()
        auth_pas = self.ui.edit_password.text()

        if auth_log == '' or auth_pas == '':
            self.mes_box('Заполните все поля!')
        else:
            self.parent().id, password, role = self.parent().db.get_pas(auth_log)
            if password != auth_pas:
                self.mes_box('Неправильно введены данные.')
            elif password == auth_pas:
                if role == '1':
                    self.parent().page_id = [0, 1, 2, 4]
                elif role == '2':
                    self.parent().page_id = [0, 3, 5]
                self.parent().show()
                self.close()


class Builder:
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()


if __name__ == '__main__':
    B = Builder()
