import sqlite3


class DataBase:
    def __init__(self, name='data.db'):
        self.db = sqlite3.connect(f"{name}")
        cur = self.db.cursor()
        cur.execute("""PRAGMA foreign_keys = ON;""")

        cur.execute("""CREATE TABLE IF NOT EXISTS Readers (
            Reader_ID integer primary key,
            Reader_Name TEXT,
            Reader_Gender TEXT,
            Reader_Date TEXT,
            Reader_Address TEXT,
            Reader_Phone TEXT
            )
        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Publishers (
            Publisher_ID integer primary key,
            Publisher_Name TEXT,
            Publisher_Address TEXT,
            Publisher_Phone TEXT,
            Publisher_Site TEXT
            )
       """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Books (
                    Book_ID integer primary key,
                    Book_Name TEXT,
                    Book_Author TEXT,
                    Book_Date TEXT,
                    Publisher_ID INT,
                    FOREIGN KEY (Publisher_ID) REFERENCES Publishers(Publisher_ID) ON DELETE SET NULL ON UPDATE CASCADE
                    )
                """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Employees (
                    Employee_ID integer primary key,
                    Employee_Name TEXT,
                    Employee_Gender TEXT,
                    Employee_Date TEXT,
                    Employee_Address TEXT,
                    Employee_Passport TEXT,
                    Login TEXT,
                    Password TEXT,
                    Access_Level INT,
                    Position_ID INT,
                    FOREIGN KEY (Position_ID) REFERENCES Positions(Position_ID) ON DELETE SET NULL ON UPDATE CASCADE
                    )
                """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Positions (
                            Position_ID integer primary key,
                            Position_Name TEXT,
                            Employee_Salary INT
                            )
                        """)

        cur.execute("""CREATE TABLE IF NOT EXISTS Issues (
                                    Issue_Date TEXT,
                                    Return_Date TEXT,
                                    Return_Status TEXT,
                                    Reader_ID INT,
                                    Book_ID INT,
                                    FOREIGN KEY (Reader_ID) REFERENCES Readers(Reader_ID) ON DELETE SET NULL ON UPDATE CASCADE,
                                    FOREIGN KEY (Book_ID) REFERENCES Books(Book_ID) ON DELETE SET NULL ON UPDATE CASCADE
                                    )
                                """)
        self.db.commit()
        cur.close()

        def get_from_books(self):
            cur = self.db.cursor()
            cur.execute("""SELECT * FROM Books""")
            records = cur.fetchall()
            cur.close()
            return records

        def create_combobox_positions(self):  # Данные для комбобокса Position
            cur = self.db.cursor()
            cur.execute("""SELECT Position_ID, Position_Name FROM Positions""")
            records = cur.fetchall()
            l = []
            for i in records:
                l.append(str(i[0]) + ' ' + i[1])
            cur.close()
            return l

        def create_combobox_readers(self):  # Данные для комбобокса Position
            cur = self.db.cursor()
            cur.execute("""SELECT Reader_ID, Reader_Name FROM Readers""")
            records = cur.fetchall()
            l = []
            for i in records:
                l.append(str(i[0]) + ' ' + i[1])
            cur.close()
            return l

        def create_combobox_publishers(self):  # Данные для комбобокса Position
            cur = self.db.cursor()
            cur.execute("""SELECT Publisher_ID, Publisher_Name FROM Publishers""")
            records = cur.fetchall()
            l = []
            for i in records:
                l.append(str(i[0]) + ' ' + i[1])
            cur.close()
            return l

        def add_in_books(self, name, description, genre, publisher):
            cur = self.db.cursor()
            cur.execute("INSERT INTO Books VALUES (NULL, ?, ?, ?, ?)", (name, description, genre, publisher))
            self.db.commit()
            cur.close()

        # def delete_from_debtors2(self, id):
        #     id = int(id)
        #     cur = self.db.cursor()
        #     cur.execute(f"""DELETE from Debtors WHERE CD_ID={id}""")
        #     self.db.commit()
        #     cur.close()

        def delete_from_books(self, id):
            id = int(id)
            cur = self.db.cursor()
            cur.execute(f"""DELETE from Books WHERE Book_ID={id}""")
            self.db.commit()
            cur.close()

        def update_books(self, id, name, description, genre, publisher):
            id = int(id)
            cur = self.db.cursor()
            cur.execute(
                f""" UPDATE Books set CD_Name="{name}", CD_Description="{description}", CD_Genre="{genre}", CD_Publisher="{publisher}"  WHERE CD_ID={id}""")
            self.db.commit()
            cur.close()


if __name__ == "__main__":
    db = DataBase()
