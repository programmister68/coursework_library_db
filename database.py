import sqlite3


class DataBase:
    def __init__(self, name='data.db'):
        self.db = sqlite3.connect(f"{name}")
        cur = self.db.cursor()

        """
        Блок инициализация таблиц
        """

        cur.execute("""PRAGMA foreign_keys = ON;""")  # команда, включающее каскадное обновление данных

        cur.execute("""CREATE TABLE IF NOT EXISTS Readers (
            Reader_ID INT primary key,
            Reader_Name TEXT,
            Reader_Date TEXT,
            Reader_Address TEXT,
            Reader_Phone TEXT
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Publishers (
            Publisher_ID INT primary key,
            Publisher_Name TEXT,
            Publisher_Address TEXT,
            Publisher_Phone TEXT,
            Publisher_Site TEXT
            )
       """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Books (
            Book_ID INT primary key,
            Book_Name TEXT,
            Book_Author TEXT,
            Book_Date TEXT,
            Publisher_ID INT,
            FOREIGN KEY (Publisher_ID) REFERENCES Publishers(Publisher_ID) ON DELETE SET NULL ON UPDATE CASCADE
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
            Employee_ID INT primary key,
            Employee_Name TEXT,
            Employee_Date TEXT,
            Employee_Address TEXT,
            Employee_Passport TEXT,
            Employee_Phone TEXT,
            Login TEXT,
            Password TEXT,
            Access_Level INT,
            Position_ID INT,
            FOREIGN KEY (Position_ID) REFERENCES Positions(Position_ID) ON DELETE SET NULL ON UPDATE CASCADE
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Positions (
            Position_ID INT primary key,
            Position_Name TEXT,
            Employee_Salary INT
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Issues (
            Issue_Date TEXT,
            Return_Status TEXT,
            Reader_ID INT,
            Book_ID INT,
            FOREIGN KEY (Reader_ID) REFERENCES Readers(Reader_ID) ON DELETE SET NULL ON UPDATE CASCADE,
            FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID) ON DELETE SET NULL ON UPDATE CASCADE
            )
        """)
        self.db.commit()
        cur.close()

        """
        Блок чтение данных из таблиц
        """

    def get_from_books(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Books""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_readers(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Readers""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_issues(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Issues""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_publishers(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Publishers""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_positions(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Positions""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_from_employees(self):
        cur = self.db.cursor()
        cur.execute("""SELECT * FROM Employees""")
        records = cur.fetchall()
        cur.close()
        return records

    def get_pas(self, log):
        cur = self.db.cursor()
        try:
            cur.execute(f"""SELECT Employee_ID, Password, Access_Level FROM Employees WHERE Login='{log}'""")
            rec = cur.fetchall()[0]
            cur.close()
            return rec[0], rec[1], rec[2]
        except Exception:
            cur.close()
            return '', '', ''

    """
    Блок создания комбобоксов
    """

    def create_combobox_positions(self):  # Данные для комбобокса Positions
        cur = self.db.cursor()
        cur.execute("""SELECT Position_ID, Position_Name FROM Positions""")
        records = cur.fetchall()
        l = []
        for i in records:
            l.append(str(i[0]) + ' ' + i[1])
        cur.close()
        return l

    def create_combobox_readers(self):  # Данные для комбобокса Readers
        cur = self.db.cursor()
        cur.execute("""SELECT Reader_ID, Reader_Name FROM Readers""")
        records = cur.fetchall()
        l = []
        for i in records:
            l.append(str(i[0]) + ' ' + i[1])
        cur.close()
        return l

    def create_combobox_books(self):  # Данные для комбобокса Books
        cur = self.db.cursor()
        cur.execute("""SELECT Book_ID, Book_Name FROM Books""")
        records = cur.fetchall()
        l = []
        for i in records:
            l.append(str(i[0]) + ' ' + i[1])
        cur.close()
        return l

    def create_combobox_publishers(self):  # Данные для комбобокса Publishers
        cur = self.db.cursor()
        cur.execute(f"""SELECT Publisher_ID, Publisher_Name FROM Publishers""")
        records = cur.fetchall()
        l = []
        for i in records:
            l.append(str(i[0]) + ' ' + i[1])
        cur.close()
        return l

    """
    Блок добавления данных в таблицы
    """

    def add_in_books(self, name, author, date, publisher_id):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (name, author, date, publisher_id))
        self.db.commit()
        cur.close()

    def add_in_positions(self, name, salary):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Positions VALUES (NULL, ?, ?)", (name, salary))
        self.db.commit()
        cur.close()

    def add_in_issues(self, is_date, status, reader_id, book_id):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Issues VALUES (?, ?, ?, ?)", (is_date, status, reader_id, book_id))
        self.db.commit()
        cur.close()

    def add_in_employees(self, name, date, address, passport, phone, login, password, access, position_id):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Employees VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, date, address, passport, phone, login, password, access, position_id))
        self.db.commit()
        cur.close()

    def add_in_readers(self, name, date, address, phone):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Readers VALUES (NULL, ?, ?, ?, ?)", (name, date, address, phone))
        self.db.commit()
        cur.close()

    def add_in_publishers(self, name, address, phone, site):
        cur = self.db.cursor()
        cur.execute("INSERT INTO Publishers VALUES (NULL, ?, ?, ?, ?)", (name, address, phone, site))
        self.db.commit()
        cur.close()

    """
    Блок удаления данных
    """

    def delete_from_books(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Books WHERE Book_ID={id}""")
        self.db.commit()
        cur.close()

    def delete_from_issues(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Issues WHERE Reader_ID={id}""")
        self.db.commit()
        cur.close()

    def delete_from_readers(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Readers WHERE Reader_ID={id}""")
        self.db.commit()
        cur.close()

    def delete_from_publishers(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Publishers WHERE Publisher_ID={id}""")
        self.db.commit()
        cur.close()

    def delete_from_employees(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Employees WHERE Employee_ID={id}""")
        self.db.commit()
        cur.close()

    def delete_from_positions(self, id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(f"""DELETE from Positions WHERE Position_ID={id}""")
        self.db.commit()
        cur.close()

    """
    Блок обновления данных
    """
    def update_books(self, id, name, description, date, publisher_id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Books set Book_Name="{name}", Book_Author="{description}", Book_Date="{date}", Publisher_ID={publisher_id}  WHERE Book_ID={id}""")
        self.db.commit()
        cur.close()

    def update_issues(self, id, is_date, status, reader_id, book_id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Issues set Issue_Date="{is_date}", Return_Status="{status}", Reader_ID={reader_id}, Book_ID={book_id}  WHERE Reader_ID={id}""")
        self.db.commit()
        cur.close()

    def update_positions(self, id, name, salary):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Positions set Position_Name="{name}", Employee_Salary={salary}  WHERE Position_ID={id}""")
        self.db.commit()
        cur.close()

    def update_readers(self, id, name, date, address, phone):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Readers set Reader_Name="{name}", Reader_Date="{date}", Reader_Address="{address}", Reader_Phone="{phone}"  WHERE Reader_ID={id}""")
        self.db.commit()
        cur.close()

    def update_publishers(self, id, name, address, phone, site):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Publishers set Publisher_Name="{name}", Publisher_Address="{address}", Publisher_Phone="{phone}", Publisher_Site="{site}" WHERE Publisher_ID={id}""")
        self.db.commit()
        cur.close()

    def update_employees(self, id, name, date, address, passport, phone, login, password, access, position_id):
        id = int(id)
        cur = self.db.cursor()
        cur.execute(
            f""" UPDATE Employees set Employee_Name="{name}", Employee_Date="{date}", Employee_Address="{address}", Employee_Passport="{passport}", Employee_Phone="{phone}",
             Login="{login}", Password="{password}", Access_Level={access}, Position_ID={position_id} WHERE Employee_ID={id}""")
        self.db.commit()
        cur.close()


if __name__ == "__main__":
    db = DataBase()
