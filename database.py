import pymysql


class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            port=3307,
            user='root',
            password='123abc',
            database='bank',
        )

    def selectCurrencies(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Currencies")
        currencies = cursor.fetchall()
        cursor.close()
        return currencies

    def selectPositions(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Positions")
        positions = cursor.fetchall()
        cursor.close()
        return positions

    def selectEmployees(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Employees")
        employees = cursor.fetchall()
        cursor.close()
        return employees

    def selectDepositors(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Depositors")
        depositors = cursor.fetchall()
        cursor.close()
        return depositors

    def selectDeposits(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Deposits")
        deposits = cursor.fetchall()
        cursor.close()
        return deposits

    def insertCurrencies(self, curr_name, exchange_rate):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Currencies"
            f"(`Curr_Name`, `Exchange_Rate`)"
            f"VALUES ('{curr_name}', {exchange_rate})"
        )
        self.connection.commit()
        cursor.close()

    def insertPositions(self, pos_name, salary, responsibility, requirement):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Positions"
            f"(`Pos_Name`, `Salary`, `Responsibility`, `Requirement`)"
            f"VALUES ('{pos_name}', {salary}, '{responsibility}', '{requirement}')"
        )
        self.connection.commit()
        cursor.close()

    def insertEmployees(self, emp_name, login, password, role, emp_phone, emp_passport, pos_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Employees"
            f"(`Emp_Name`, `Login`, `Password`, `Role`, `Emp_Phone`, `Emp_Passport`, `Position_ID`)"
            f"VALUES ('{emp_name}', '{login}', '{password}', '{role}', '{emp_phone}', '{emp_passport}', {pos_id})"
        )
        self.connection.commit()
        cursor.close()

    def insertDepositors(self, depositor_name, depositor_phone, depositor_passport, dep_sum, ref_sum, dep_date, ref_date, ref_status, emp_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Depositors"
            f"(`Depositor_Name`, `Depositor_Phone`, `Depositor_Passport`, `Dep_Sum`, `Refund_Sum`, `Dep_Date`, `Refund_Date`, `Refund_Status`, `Employee_ID`)"
            f"VALUES ('{depositor_name}', '{depositor_phone}', '{depositor_passport}', {dep_sum}, {ref_sum}, '{dep_date}', '{ref_date}', '{ref_status}', {emp_id})"
        )
        self.connection.commit()
        cursor.close()

    def insertDeposits(self, dep_name, percent_rate, curr_id, depositor_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"INSERT INTO Deposits"
            f"(`Dep_Name`, `Percent_Rate`, `Currency_ID`, `Depositor_ID`)"
            f"VALUES ('{dep_name}', {percent_rate}, {curr_id}, {depositor_id})"
        )
        self.connection.commit()
        cursor.close()

    def deleteCurrencies(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Currencies WHERE `Currency_ID`={id}")
        self.connection.commit()
        cursor.close()

    def deletePositions(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Positions WHERE `Position_ID`={id}")
        self.connection.commit()
        cursor.close()

    def deleteEmployees(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Employees WHERE `Employee_ID`={id}")
        self.connection.commit()
        cursor.close()

    def deleteDepositors(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Depositors WHERE `Depositor_ID`={id}")
        self.connection.commit()
        cursor.close()

    def deleteDeposits(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"DELETE FROM Deposits WHERE `Deposit_ID`={id}")
        self.connection.commit()
        cursor.close()

    def updateEmployees(self, id, emp_name, login, password, role, emp_phone, emp_passport, pos_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Employees set `Emp_Name`='{emp_name}', `Login`='{login}', `Password`='{password}', `Role`='{role}', `Emp_Phone`='{emp_phone}', `Emp_Passport`='{emp_passport}', `Position_ID`={pos_id} WHERE `Employee_ID`={id}")
        self.connection.commit()
        cursor.close()

    def updateDeposits(self, id, dep_name, percent_rate, curr_id, depositor_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Deposits set `Dep_Name`='{dep_name}', `Percent_Rate`={percent_rate}, `Currency_ID`={curr_id}, `Depositor_ID`={depositor_id} WHERE `Deposit_ID`={id}")
        self.connection.commit()
        cursor.close()

    def updatePositions(self, id, pos_name, salary, responsibility, requirement):
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Positions set `Pos_Name`='{pos_name}', `Salary`={salary}, `Responsibility`='{responsibility}', `Requirement`='{requirement}' WHERE `Position_ID`={id}")
        self.connection.commit()
        cursor.close()

    def updateCurrencies(self, id, curr_name, ex_rate):
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Currencies set `Curr_Name`='{curr_name}', `Exchange_Rate`={ex_rate} WHERE `Currency_ID`={id}")
        self.connection.commit()
        cursor.close()

    def updateDepositors(self, id, depositor_name, depositor_phone, depositor_passport, dep_sum, ref_sum, dep_date, ref_date, ref_status, emp_id):
        cursor = self.connection.cursor()
        cursor.execute(
            f"UPDATE Depositors set `Depositor_Name`='{depositor_name}', `Depositor_Phone`='{depositor_phone}', `Depositor_Passport`='{depositor_passport}', `Dep_Sum`={dep_sum}, `Refund_Sum`={ref_sum}, `Dep_Date`='{dep_date}', `Refund_Date`='{ref_date}', `Refund_Status`='{ref_status}', `Employee_ID`={emp_id} WHERE `Depositor_ID`={id}")
        self.connection.commit()
        cursor.close()

    def get_pas(self, log):
        cur = self.connection.cursor()
        try:
            cur.execute(f"""SELECT Employee_ID, Password, Role FROM Employees WHERE Login='{log}'""")
            rec = cur.fetchall()[0]
            cur.close()
            return rec[0], rec[1], rec[2]
        except Exception:
            cur.close()
            return '', '', ''


if __name__ == '__main__':
    D = Database()
