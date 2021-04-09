import sqlite3
import os
from user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    if row:
        return User(row["username"], row["password"])

class UserRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_user_to_database(self, user):
        cursor = self.connection.cursor()

        #db.execute("INSERT INTO  Users (username, password) VALUES (?, ?)", [user.username, user.password])
        cursor.execute("INSERT INTO  users (username, password) VALUES (?, ?)", [user.username, user.password])

        self.connection.commit()

        return user

    def find_all_users(self):
        cursor = self.connection.cursor()

        all_users_table = cursor.execute("SELECT * FROM  users").fetchall()

        #self.connection.commit() EI TARVITSE, KOSKA EI KIRJOITETA MITÄÄN. Mutta ei ole haittaakaan.
        print("Lista luoduista käyttäjätunnuksista ja salasanoista")
        for row in all_users_table:
            print(row["username"], row["password"])
        #print(list(map(get_user_by_row, all_users_table)))

user_repository = UserRepository(get_database_connection())