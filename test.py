import sys
from unittest import TestCase

from PyQt5 import QtCore
from PyQt5.QtCore import QDate, QItemSelectionModel
from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication

from database import DataBase
from gui import MainWindow


class TestAddData(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.db = DataBase()
        self.window = MainWindow()

    def test_add_a_position_lib(self):
        btn_add = self.window.ui.add_pos  # Объявление кнопки

        self.window.ui.add_pos_name.setText("Библиотекарь")
        self.window.ui.add_pos_salary.setValue(10000)

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_a_position_otd(self):
        btn_add = self.window.ui.add_pos  # Объявление кнопки

        self.window.ui.add_pos_name.setText("Сотрудник отдела кадров")
        self.window.ui.add_pos_salary.setValue(10000)

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_employee_lib(self):
        btn_add = self.window.ui.add_emloyee  # Объявление кнопки

        self.window.ui.employees_fio.setText("Максим")
        self.window.ui.employees_date.setDate(QDate.fromString("24.01.2003"))
        self.window.ui.employees_address.setText("test")
        self.window.ui.employees_passport.setText("5456789098")
        self.window.ui.employees_phone.setText("9296781708")
        self.window.ui.login.setText("test")
        self.window.ui.password.setText("test")
        self.window.ui.access.setValue(1)
        self.window.ui.positions_combobox.addItems(self.db.create_combobox_positions())

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_employee_otd(self):
        btn_add = self.window.ui.add_emloyee  # Объявление кнопки

        self.window.ui.employees_fio.setText("Александр")
        self.window.ui.employees_date.setDate(QDate.fromString("04.01.2003"))
        self.window.ui.employees_address.setText("test")
        self.window.ui.employees_passport.setText("9856789098")
        self.window.ui.employees_phone.setText("9296971708")
        self.window.ui.login.setText("test2")
        self.window.ui.password.setText("test2")
        self.window.ui.access.setValue(0)
        self.window.ui.positions_combobox.addItems(self.db.create_combobox_positions())

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_a_publisher(self):
        btn_add = self.window.ui.pushButton_2  # Объявление кнопки

        self.window.ui.lineEdit_2.setText("Издательство")
        self.window.ui.lineEdit_3.setText("test_test")
        self.window.ui.lineEdit_4.setText("9296971708")
        self.window.ui.lineEdit_5.setText("test.ru")

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_book(self):
        btn_add = self.window.ui.add_dep  # Объявление кнопки

        self.window.ui.dep_name_line.setText("Война и Мир")
        self.window.ui.percent_line.setText("Л.Толстой")
        self.window.ui.dateEdit.setDate(QDate.fromString("2000"))
        self.window.ui.publishers_combobox.addItems(self.db.create_combobox_publishers())

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_a_reader(self):
        btn_add = self.window.ui.emp_add  # Объявление кнопки

        self.window.ui.add_fio_reader.setText("Пётр")
        self.window.ui.add_date_birth_reader.setDate(QDate.fromString("01.01.2022"))
        self.window.ui.add_address_reader.setText("test_test")
        self.window.ui.add_phone_reader.setText("9296971708")

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)

    def test_add_issue(self):
        btn_add = self.window.ui.issues_add  # Объявление кнопки

        self.window.ui.issues_date.setDate(QDate.fromString("01.01.2022"))
        self.window.ui.issues_status.setText("01.01.2023")
        self.window.ui.readers_combobox.addItems(self.db.create_combobox_readers())
        self.window.ui.books_combobox.addItems(self.db.create_combobox_books())
        self.window.ui.employee_combobox.addItems(self.db.create_combobox_employees())

        QTest.mouseClick(btn_add, QtCore.Qt.MouseButton.LeftButton)
        self.db.delete_from_issues(1)
        self.db.delete_from_books(1)
        self.db.delete_from_readers(1)
        self.db.delete_from_employees(1)
        self.db.delete_from_positions(1)
        self.db.delete_from_publishers(1)


class TestDeleteAndSave(TestCase):
    def setUp(self):
        self.qapp = QApplication(sys.argv)
        self.db = DataBase()
        self.window = MainWindow()

    def test_add_save_position(self):
        self.db.add_in_positions("name", 20000)
        QTest.mouseClick(self.window.ui.save_pos, QtCore.Qt.MouseButton.LeftButton)

    def test_add_save_publisher(self):
        self.db.add_in_publishers("name", "address", "phone", "site")
        QTest.mouseClick(self.window.ui.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test_add_save_employee(self):
        self.db.add_in_employees("name", "date", "address", "passport", "phone", "test1", "test1", 0, 1)
        QTest.mouseClick(self.window.ui.save_emloyee, QtCore.Qt.MouseButton.LeftButton)

    def test_add_save_book(self):
        self.db.add_in_books("name", "author", "date", 1)
        QTest.mouseClick(self.window.ui.save_dep, QtCore.Qt.MouseButton.LeftButton)

    def test_add_save_reader(self):
        self.db.add_in_readers("name", "date", "address", "phone")
        QTest.mouseClick(self.window.ui.emp_save, QtCore.Qt.MouseButton.LeftButton)

    def test_add_save_issue(self):
        self.db.add_in_issues("date", "status", 1, 1, 1)
        QTest.mouseClick(self.window.ui.issues_save, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_a_issue(self):
        rowcount = self.window.table_issues.rowCount()
        self.window.table_issues.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.issues_delete
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.issues_save, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_book(self):
        rowcount = self.window.table_books.rowCount()
        self.window.table_books.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.delete_dep
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.save_dep, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_employee(self):
        rowcount = self.window.table_employees.rowCount()
        self.window.table_employees.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.delete_emloyee
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.save_emloyee, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_position(self):
        rowcount = self.window.table_positions.rowCount()
        self.window.table_positions.setCurrentCell(rowcount - 1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.delete_pos
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.save_pos, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_publisher(self):
        rowcount = self.window.table_publishers.rowCount()
        self.window.table_publishers.setCurrentCell(rowcount - 1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.pushButton_3
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.pushButton, QtCore.Qt.MouseButton.LeftButton)

    def test_delete_reader(self):
        rowcount = self.window.table_readers.rowCount()
        self.window.table_readers.setCurrentCell(rowcount-1, 1, QItemSelectionModel.SelectionFlag.Select)

        btn_del = self.window.ui.emp_delete
        QTest.mouseClick(btn_del, QtCore.Qt.MouseButton.LeftButton)
        QTest.mouseClick(self.window.ui.emp_save, QtCore.Qt.MouseButton.LeftButton)


