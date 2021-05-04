import sqlite3
import os
from user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    """Jos käyttäjäolio on olemassa, metodi palauttaa käyttäjäolion.

    Args:
        row: tietokannan rivi, johon on talletettu käyttäjäolio.

    Returns:
        Käyttäjäolion, jos sellainen on. False muuten.
    """

    if row:
        return User(row["username"], row["password"])


class UserRepository:
    """Luokka, jonka avulla käyttäjätieto siirretään tietokantaan.

    Attributes:
        connection = tietokantayhteys
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka luo yhteyden tietokantaan.

        Args:
            connection: tietokantayhteys
        """

        self.connection = connection

    def create_user_to_database(self, user):
        """Lisää uuden user-olion eli käyttäjänimen ja salasanan tietokantaan.

        Args:
            user: käyttäjäolio, joka sisältää käyttäjänimen ja salasanan.

        Returns:
            User- eli käyttäjäolion.
        """

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO  users (username, password) VALUES (?, ?)", [
                       user.username, user.password])

        self.connection.commit()

        return user

    def find_by_username(self, username):
        """Etsii, löytyykö tietokannasta argumenttina annettua käyttäjänimeä.

        Args:
            username: käyttäjänimi, jota etsitään tietokannasta.

        Returns:
            Käyttäjänimeä vastaavan User- eli käyttäjäolion, jos se löytyy tietokannasta.
        """

        cursor = self.connection.cursor()

        row = cursor.execute(
            "SELECT * FROM  users WHERE username = ?", (username,)).fetchone()

        return get_user_by_row(row)

    def find_all_users(self):
        """Etsii tietokannasta kaikki käyttäjät ja salasanat. Ei vielä käytössä.
        """

        cursor = self.connection.cursor()

        all_users_table = cursor.execute("SELECT * FROM  users").fetchall()

        print("Lista luoduista käyttäjätunnuksista ja salasanoista")

        for row in all_users_table:
            print(row["username"], row["password"])


user_repository = UserRepository(get_database_connection())
