import sqlite3
 
class AdvancedUserOperations:

    def __init__(self):

        self.conn = sqlite3.connect('user_database.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS user")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE, password TEXT, age INTEGER, gender TEXT, address TEXT)")
 


    def create_user_with_profile(self, name, email, password, age=None, gender=None, address=None):

        if name == "" or email == "" or password == "":
            return "Invalid user entry"
        self.cursor.execute("INSERT INTO user (name, email, password, age, gender, address) VALUES (?,?,?,?,?,?)", (name, email, password, age, gender, address))
        self.conn.commit()
        return "Inserted id " + str(self.cursor.lastrowid) + " into table user"
        
 

    def retrieve_users_by_criteria(self, min_age=None, max_age=None, gender=None):

        self.cursor.execute("SELECT * FROM user WHERE AGE >= ? AND AGE <= ? and gender = ?", (min_age, max_age, gender))
        return self.cursor.fetchall()

 

    def update_user_profile(self, email, age=None, gender=None, address=None):

        self.cursor.execute("UPDATE user SET age = ?, address = ? WHERE email = ?", (str(age), address, email))
        self.conn.commit()
        return "Changed age to '" + str(age) +"' and address to '" + address + "' for user profile: '" + email + "'"

 

    def delete_users_by_criteria(self, gender=None):

        self.cursor.execute("DELETE FROM user WHERE gender = ?", (gender,))
        self.conn.commit()
        return "Deleted all user entries where gender is '" + gender + "'"

 

    def __del__(self):

        self.conn.close()