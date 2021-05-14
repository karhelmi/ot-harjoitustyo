from database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa mahdolliset olemassa olevat taulukot tietokannasta.

    Args:
        connection: määritetty yhteys, missä taulukot on.
    """

    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    cursor.execute('''
        drop table if exists items;
    ''')

    connection.commit()


def create_tables(connection):
    """Metodi luo tyhjään tietokantaan oliotietoja varten kaksi taulukkoa.

    Args:
        connection: määritetty yhteys, mihin taulukot luodaan.
    """

    cursor = connection.cursor()

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

    connection.commit()


def initialize_database():
    """Luo tietokantayhteyden sekä poistaa siellä mahdollisesti olevat taulut ja luo uudet.
    """

    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
