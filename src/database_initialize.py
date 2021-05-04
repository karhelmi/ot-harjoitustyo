from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists items;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()  # "yhteys" tietokantaan

    cursor.execute('''
        CREATE TABLE users (
            id text primary key,
            username text,
            password text
        );
    ''')

    cursor.execute('''
        CREATE TABLE items (
            id text primary key,
            type text,
            description text,
            size text,
            brand text,
            color text,
            username text
        );
    ''')

    connection.commit()  # suorittaa, mitä olen määrännyt yllä.


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
