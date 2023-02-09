from PyQt5.QtCore import Qt, QTime, QDateTime
from PyQt5.QtWidgets import QTableWidgetItem
from database import DataBase
import sys

from PyQt5 import QtWidgets
from PyQt5 import uic, QtCore, QtGui
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QGraphicsScene
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox

import logging
logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = DataBase()
        self.ui = uic.loadUi("forms/main.ui", self)
        # self.exitButton.setIcon(QIcon('icons/logout.png'))

        self.page = self.ui.stackedWidget_main
        self.page_id = [0]  # индексы доступных страничек после авторизации для сотрудника
        self.now_page = 0
        # self.page.setCurrentIndex(self.page_id[self.now_page])

        self.ui.nextButton.clicked.connect(self.next_page)
        self.ui.nextButton.setToolTip("Следующая страница")

        self.ui.backButton.clicked.connect(self.back_page)
        self.ui.backButton.setToolTip("Предыдущая страница")

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.setToolTip("Завершить текущую сессию")

        # self.ui.infoButton.setToolTip("Автор: Шепелёв Сергей, ИСП-41-19")

        # Кнопки монипуляции данных таблицы Employees

        self.ui.add_emloyee.clicked.connect(self.new_employee)
        self.ui.delete_emloyee.clicked.connect(self.delete_employee)
        self.ui.save_emloyee.clicked.connect(self.save_employee)

        # Кнопки монипуляции данных таблицы Positions

        self.ui.add_pos.clicked.connect(self.new_positions)
        self.ui.delete_pos.clicked.connect(self.delete_position)
        self.ui.save_pos.clicked.connect(self.save_position)

        # Кнопки монипуляции данных таблицы Readers

        self.ui.emp_add.clicked.connect(self.new_readers)
        self.ui.emp_delete.clicked.connect(self.delete_reader)
        self.ui.emp_save.clicked.connect(self.save_reader)

        # Кнопки монипуляции данных таблицы Books

        self.ui.add_dep.clicked.connect(self.new_books)
        self.ui.delete_dep.clicked.connect(self.delete_book)
        self.ui.save_dep.clicked.connect(self.save_book)

        # Кнопки монипуляции данных таблицы Publishers

        self.ui.pushButton_2.clicked.connect(self.new_publishers)
        self.ui.pushButton_3.clicked.connect(self.delete_publisher)
        self.ui.pushButton.clicked.connect(self.save_publisher)

        # Кнопки монипуляции данных таблицы Issues

        self.ui.issues_add.clicked.connect(self.new_issues)
        self.ui.issues_delete.clicked.connect(self.delete_issue)
        self.ui.issues_save.clicked.connect(self.save_issue)

        self.positions_combobox.addItems(self.db.create_combobox_positions())
        self.readers_combobox.addItems(self.db.create_combobox_readers())
        self.books_combobox.addItems(self.db.create_combobox_books())
        self.publishers_combobox.addItems(self.db.create_combobox_publishers())
        self.employee_combobox.addItems(self.db.create_combobox_employees())

        self.updateTableEmployees()
        self.updateTablePositions()
        self.updateTableBooks()
        self.updateTableReaders()
        self.updateTablePublishers()
        self.updateTableIssues()

        logging.log(logging.INFO, 'Приложение запущено.')

    def exit(self):
        self.now_page = 0
        self.page.setCurrentIndex(self.page_id[self.now_page])
        self.hide()
        logging.log(logging.INFO, 'Завершение сессии.')
        self.open_auth()

    def next_page(self):
        if self.now_page != len(self.page_id) - 1:
            self.now_page += 1
            self.page.setCurrentIndex(self.page_id[self.now_page])
            logging.log(logging.INFO, 'Следующая страница.')

    def back_page(self):
        if self.now_page != 0:
            self.now_page -= 1
            self.page.setCurrentIndex(self.page_id[self.now_page])
            logging.log(logging.INFO, 'Предыдущая страница.')

    def open_auth(self):
        dialog = DialogAuth(self)
        dialog.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('icons/books.png'))
        dialog.show()
        dialog.exec_()
        logging.log(logging.INFO, 'Начало сессии.')

    #########################

    def updateTableEmployees(self):
        self.table_employees.clear()
        rec = self.db.get_from_employees()
        self.ui.table_employees.setColumnCount(10)
        self.ui.table_employees.setRowCount(len(rec))
        self.ui.table_employees.setHorizontalHeaderLabels(
            ['ID', 'ФИО', 'Дата рождения', 'Адрес', 'Паспорт', 'Телефон', 'Логин', 'Пароль', 'Уровень доступа', 'ID должности'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_employees.setItem(i, x, item)

    def updateTablePositions(self):
        self.table_positions.clear()
        rec = self.db.get_from_positions()
        self.ui.table_positions.setColumnCount(3)
        self.ui.table_positions.setRowCount(len(rec))
        self.ui.table_positions.setHorizontalHeaderLabels(
            ['ID', 'Наименование', 'Оклад(₽)'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_positions.setItem(i, x, item)

    def updateTableReaders(self):
        self.table_readers.clear()
        rec = self.db.get_from_readers()
        self.ui.table_readers.setColumnCount(5)
        self.ui.table_readers.setRowCount(len(rec))
        self.ui.table_readers.setHorizontalHeaderLabels(
            ['ID', 'ФИО', 'Дата рождения', 'Адрес проживания', 'Телефон'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_readers.setItem(i, x, item)

    def updateTableBooks(self):
        self.table_books.clear()
        rec = self.db.get_from_books()
        self.ui.table_books.setColumnCount(5)
        self.ui.table_books.setRowCount(len(rec))
        self.ui.table_books.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Автор/Авторы', 'Год издания', 'Издатель'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_books.setItem(i, x, item)

    def updateTablePublishers(self):
        self.table_publishers.clear()
        rec = self.db.get_from_publishers()
        self.ui.table_publishers.setColumnCount(5)
        self.ui.table_publishers.setRowCount(len(rec))
        self.ui.table_publishers.setHorizontalHeaderLabels(
            ['ID', 'Наименование', 'Адрес', 'Телефон', 'Сайт'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_publishers.setItem(i, x, item)

    def updateTableIssues(self):
        self.table_issues.clear()
        rec = self.db.get_from_issues()
        self.ui.table_issues.setColumnCount(6)
        self.ui.table_issues.setRowCount(len(rec))
        self.ui.table_issues.setHorizontalHeaderLabels(
            ['ID', 'Дата выдачи', 'Статус', 'Читатель', 'Книга', 'Сотрудник'])

        for i, exposition in enumerate(rec):
            for x, field in enumerate(exposition):
                item = QTableWidgetItem()
                item.setText(str(field))
                if x == 0:
                    item.setFlags(Qt.ItemIsEnabled)
                self.ui.table_issues.setItem(i, x, item)

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

    def getFromTableBooks(self):
        rows = self.table_books.rowCount()
        cols = self.table_books.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_books.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableReaders(self):
        rows = self.table_readers.rowCount()
        cols = self.table_readers.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_readers.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTablePublishers(self):
        rows = self.table_publishers.rowCount()
        cols = self.table_publishers.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_publishers.item(row, col).text())
            data.append(tmp)
        return data

    def getFromTableIssues(self):
        rows = self.table_issues.rowCount()
        cols = self.table_issues.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                tmp.append(self.table_issues.item(row, col).text())
            data.append(tmp)
        return data

    def new_employee(self):
        employees_fio = self.ui.employees_fio.text()
        employees_date = self.ui.employees_date.text()
        employees_address = self.ui.employees_address.text()
        employees_passport = self.ui.employees_passport.text()
        employees_phone = self.ui.employees_phone.text()
        login = self.ui.login.text()
        password = self.ui.password.text()
        access = self.ui.access.text()
        self.ui.label_9.setToolTip("0 - для библиотекаря, 1 - для сотрудника отдела кадров, 2 - для остальных должностей")
        positions_combobox = self.ui.positions_combobox.currentText()
        positions_combobox = positions_combobox.split(' ')[0]

        self.db.add_in_employees(employees_fio, employees_date, employees_address, employees_passport, employees_phone, login, password, access, positions_combobox)
        self.update_combobox_employees()
        self.updateTableEmployees()
        logging.log(logging.INFO, 'Запись добавлена.')

    def new_positions(self):
        add_pos_name = self.ui.add_pos_name.text()
        add_pos_salary = self.ui.add_pos_salary.text()

        self.db.add_in_positions(add_pos_name, add_pos_salary)
        self.update_combobox_positions()
        self.updateTablePositions()
        logging.log(logging.INFO, 'Запись добавлена.')

    def new_readers(self):
        add_fio_reader = self.ui.add_fio_reader.text()
        add_date_birth_reader = self.ui.add_date_birth_reader.text()
        add_address_reader = self.ui.add_address_reader.text()
        add_phone_reader = self.ui.add_phone_reader.text()

        self.db.add_in_readers(add_fio_reader, add_date_birth_reader, add_address_reader, add_phone_reader)
        self.update_combobox_readers()
        self.updateTableReaders()
        logging.log(logging.INFO, 'Запись добавлена.')

    def new_publishers(self):
        lineEdit_2 = self.ui.lineEdit_2.text()
        lineEdit_3 = self.ui.lineEdit_3.text()
        lineEdit_4 = self.ui.lineEdit_4.text()
        lineEdit_5 = self.ui.lineEdit_5.text()

        self.db.add_in_publishers(lineEdit_2, lineEdit_3, lineEdit_4, lineEdit_5)
        self.update_combobox_publishers()
        self.updateTablePublishers()
        logging.log(logging.INFO, 'Запись добавлена.')

    def new_books(self):
        dep_name_line = self.ui.dep_name_line.text()
        percent_line = self.ui.percent_line.text()
        dateEdit = self.ui.dateEdit.text()
        publishers_combobox = self.ui.publishers_combobox.currentText()
        publishers_combobox = publishers_combobox.split(' ')[0]

        self.db.add_in_books(dep_name_line, percent_line, dateEdit, publishers_combobox)
        self.update_combobox_books()
        self.updateTableBooks()
        logging.log(logging.INFO, 'Запись добавлена.')

    def new_issues(self):
        issues_date = self.ui.issues_date.text()
        issues_status = self.ui.issues_status.text()

        readers_combobox = self.ui.readers_combobox.currentText()
        readers_combobox = readers_combobox.split(' ')[0]

        books_combobox = self.ui.books_combobox.currentText()
        books_combobox = books_combobox.split(' ')[0]

        employee_combobox = self.ui.employee_combobox.currentText()
        employee_combobox = employee_combobox.split(' ')[0]

        self.db.add_in_issues(issues_date, issues_status, readers_combobox, books_combobox, employee_combobox)
        self.updateTableIssues()
        logging.log(logging.INFO, 'Запись добавлена.')

    def update_combobox_positions(self):
        self.positions_combobox.clear()
        self.positions_combobox.addItems(self.db.create_combobox_positions())
        logging.log(logging.INFO, 'Виджет ComboBox обновлён.')

    def update_combobox_books(self):
        self.books_combobox.clear()
        self.books_combobox.addItems(self.db.create_combobox_books())
        logging.log(logging.INFO, 'Виджет ComboBox обновлён.')

    def update_combobox_readers(self):
        self.readers_combobox.clear()
        self.readers_combobox.addItems(self.db.create_combobox_readers())
        logging.log(logging.INFO, 'Виджет ComboBox обновлён.')

    def update_combobox_employees(self):
        self.employee_combobox.clear()
        self.employee_combobox.addItems(self.db.create_combobox_employees())
        logging.log(logging.INFO, 'Виджет ComboBox обновлён.')

    def update_combobox_publishers(self):
        self.publishers_combobox.clear()
        self.publishers_combobox.addItems(self.db.create_combobox_publishers())
        logging.log(logging.INFO, 'Виджет ComboBox обновлён.')

    def delete_employee(self):
        SelectedRow = self.table_employees.currentRow()
        rowcount = self.table_employees.rowCount()
        colcount = self.table_employees.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_employees.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_employees.model().index(-1, -1)
            self.table_employees.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def delete_position(self):
        SelectedRow = self.table_positions.currentRow()
        rowcount = self.table_positions.rowCount()
        colcount = self.table_positions.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_positions.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_positions.model().index(-1, -1)
            self.table_positions.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def delete_book(self):
        SelectedRow = self.table_books.currentRow()
        rowcount = self.table_books.rowCount()
        colcount = self.table_books.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_books.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_books.model().index(-1, -1)
            self.table_books.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def delete_reader(self):
        SelectedRow = self.table_readers.currentRow()
        rowcount = self.table_readers.rowCount()
        colcount = self.table_readers.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_readers.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_readers.model().index(-1, -1)
            self.table_readers.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def delete_publisher(self):
        SelectedRow = self.table_publishers.currentRow()
        rowcount = self.table_publishers.rowCount()
        colcount = self.table_publishers.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_publishers.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_publishers.model().index(-1, -1)
            self.table_publishers.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def delete_issue(self):
        SelectedRow = self.table_issues.currentRow()
        rowcount = self.table_issues.rowCount()
        colcount = self.table_issues.columnCount()

        if rowcount == 0:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("В таблице нет данных!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        elif SelectedRow == -1:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Выберите поле для удаления!")
            msg.setWindowTitle("Ошибка")
            logging.log(logging.INFO, 'Ошибка!')
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()

        else:
            for col in range(1, colcount):
                self.table_issues.setItem(SelectedRow, col, QTableWidgetItem(''))
            ix = self.table_issues.model().index(-1, -1)
            self.table_issues.setCurrentIndex(ix)
            logging.log(logging.INFO, 'Запись удалена.')

    def save_employee(self):
        data = self.getFromTableEmployees()
        for string in data:
            if string[1] != '':
                self.db.update_employees(int(string[0]), string[1], string[2], string[3], string[4], string[5], string[6], string[7], int(string[8]), int(string[9]))
            else:
                self.db.delete_from_employees(int(string[0]))
        self.update_combobox_employees()
        self.updateTableEmployees()
        logging.log(logging.INFO, 'Данные успешно записаны.')

    def save_position(self):
        data = self.getFromTablePositions()
        for string in data:
            if string[1] != '':
                self.db.update_positions(int(string[0]), string[1], int(string[2]))
            else:
                self.db.delete_from_positions(int(string[0]))
        self.update_combobox_positions()
        self.updateTablePositions()
        logging.log(logging.INFO, 'Данные успешно записаны.')

    def save_book(self):
        data = self.getFromTableBooks()
        for string in data:
            if string[1] != '':
                self.db.update_books(int(string[0]), string[1], string[2], string[3], string[4])
            else:
                self.db.delete_from_books(int(string[0]))
        self.update_combobox_books()
        self.updateTableBooks()
        logging.log(logging.INFO, 'Данные успешно записаны.')

    def save_reader(self):
        data = self.getFromTableReaders()
        for string in data:
            if string[1] != '':
                self.db.update_readers(int(string[0]), string[1], string[2], string[3], string[4])
            else:
                self.db.delete_from_readers(int(string[0]))
        self.update_combobox_readers()
        self.updateTableReaders()
        logging.log(logging.INFO, 'Данные успешно записаны.')

    def save_publisher(self):
        data = self.getFromTablePublishers()
        for string in data:
            if string[1] != '':
                self.db.update_publishers(int(string[0]), string[1], string[2], string[3], string[4])
            else:
                self.db.delete_from_publishers(int(string[0]))
        self.update_combobox_publishers()
        self.updateTablePublishers()
        logging.log(logging.INFO, 'Данные успешно записаны.')

    def save_issue(self):
        data = self.getFromTableIssues()
        for string in data:
            if string[1] != '':
                self.db.update_issues(int(string[0]), string[1], string[2], int(string[3]), int(string[4]), int(string[5]))
            else:
                self.db.delete_from_issues(int(string[0]))
        self.updateTableIssues()
        logging.log(logging.INFO, 'Данные успешно записаны.')


class DialogAuth(QDialog):
    def __init__(self, parent=None):
        super(DialogAuth, self).__init__(parent)
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowIcon(QIcon('icons/reading-book.png'))
        self.scene = QGraphicsScene(0, 0, 300, 80)
        self.ui.btn_enter.clicked.connect(self.enter)
        self.ui.btn_enter.setToolTip("Войти в учётную запись")
        self.btn_hide_password.setIcon(QIcon('icons/eye_close.png'))
        self.ui.btn_hide_password.clicked.connect(self.vis_pas)
        self.ui.btn_hide_password.setToolTip("Показать пароль")

        self.db = DataBase()

        self.next_try = 0
        self.vis_p = False

    def vis_pas(self):
        ed = self.ui.edit_password
        if self.vis_p:
            self.vis_p = False
            self.btn_hide_password.setIcon(QIcon('icons/eye_close.png'))
            self.ui.btn_hide_password.setToolTip("Показать пароль")
            ed.setEchoMode(QtWidgets.QLineEdit.Password)

        else:
            self.vis_p = True
            self.btn_hide_password.setIcon(QIcon('icons/eye.png'))
            self.ui.btn_hide_password.setToolTip("Скрыть пароль")
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

        if auth_log == 'admin' and auth_pas == 'admin':
            self.parent().page_id = [0, 1, 2, 3, 4, 5]
            self.parent().show()
            self.close()
        
        if auth_log == '' or auth_pas == '':
            self.mes_box('Заполните все поля!')
            logging.log(logging.INFO, 'Ошибка!')
        else:
            self.parent().id, password, access = self.parent().db.get_pas(auth_log)
            if password != auth_pas:
                self.mes_box('Неверный логин или пароль')
                logging.log(logging.INFO, 'Ошибка!')
            elif password == auth_pas:
                if access == 0:
                    self.parent().page_id = [0, 2, 4, 5]
                    self.parent().show()
                    self.close()
                elif access == 1:
                    self.parent().page_id = [1, 3]
                    self.parent().show()
                    self.close()
                elif access == 2:
                    self.mes_box('Отказано в доступе')
                    logging.log(logging.INFO, 'Ошибка!')


class Builder:
    def __init__(self):
        self.qapp = QApplication(sys.argv)
        self.window = MainWindow()
        self.auth()

    def auth(self):
        self.window.open_auth()
        self.qapp.exec()
        logging.log(logging.INFO, 'Приложение завершила свою работу.')


if __name__ == '__main__':
    B = Builder()
