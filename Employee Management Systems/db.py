print("Hi Welcome to DB Page ")

import sqlite3


class Database:
    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        sql = """
        Create Table if not exists employees(
            Id Integer Primary key,
            name Text,
            age Text,
            doj Text,
            email Text,
            gender Text,
            contact Text,
            address Text
        )
        """
        self.cursor.execute(sql)
        self.connection.commit()

    # Insert function

    def insert(self, name, age, doj, email, gender, contact, address):
        self.cursor.execute("insert into employees values (Null,?,?,?,?,?,?,?)",
                            (name, age, doj, email, gender, contact, address))
        self.connection.commit()

    # Fetch All Data from Db

    def fetch(self):
        self.cursor.execute("Select * from employees")
        rows = self.cursor.fetchall()
        # print(rows)
        return rows

    # Delete Data from Db

    def delete(self, id):
        self.cursor.execute('delete from employees where id=?', (id,))
        self.connection.commit()

    # Update Data from Db

    def update(self, id, name, age, doj, email, gender, contact, address):
        self.cursor.execute(
            "update employees set name=?, age=?, doj=?, email=?, gender=?, contact=?, address=? where id=?",
            (name, age, doj, email, gender, contact, address, id))
        self.connection.commit()


'''

obj = Database("Employee.db")
                    # For Insert
# obj.insert("ABC", "12", "14.09.2018", "ABC123@gmail.com", "male", "9876543210", "CBE")

                    # For FetchAll (Insert data Subha)
# obj.insert("ABC", "12", "12.09.2019", "ABC123@gmail.com", "fe-male", "9876543210", "CH")
# obj.fetch()

                    #For Delete inserting dummy data as subbu
#obj.insert("ABC", "12", "12.09.2015", "ABC123@gmail.com", "fe-male", "9876543210", "TJN")
#obj.delete("4")

                    # For Update select the id from DB for which employee you have to update for
# obj.update("2","ABC","12","01.12.2012","ABC123@yahoo.com","Fe-male", "9876543210", "KMU")

'''
