from item import Item
from database_connection import get_database_connection


def get_item_by_row(row):
    """Jos tarvikeolio on olemassa, metodi palauttaa tarvikeolion.

    Args:
        row: tietokannan rivi, johon on talletettu tarvikeolio.

    Returns:
        Tarvikeolion, jos sellainen on. False muuten.
    """

    if row:
        return Item(row["type"], row["description"], row["size"], row["brand"], row["color"], row["username"])


class ItemRepository:
    """Luokka, jonka avulla tarviketieto siirretään tietokantaan.

    Attributes:
        connection = tietokantayhteys
    """

    def __init__(self, connection):
        """Luokan konstruktori, joka luo yhteyden tietokantaan.

        Args:
            connection: tietokantayhteys
        """

        self.connection = connection

    def create_item_to_database(self, item):
        """Lisää uuden item- eli tarvikeolion eli tarviketiedot tietokantaan.

        Args:
            item: tarvikeolio, joka sisältää kuusi attribuuttia.

        Returns:
            Item- eli tarvikeolion.
        """

        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO  items (type, description, size, brand, color, username) VALUES (?, ?, ?, ?, ?, ?)", [
                       item.type, item.description, item.size, item.brand, item.color, item.username])

        self.connection.commit()

        return item

    def retrieve_items_from_database(self, username, selection):
        """Etsii, löytyykö tietokannasta argumenttina annettua käyttäjänimeä tarviketyyppiä.

        Args:
            username: käyttäjänimi, johon liittyviä tietoja etsitään tietokannasta.
            selection: tarviketyyppi, jonka tiedot etsitään tietokannasta.

        Returns:
            Käyttäjänimeä ja tarviketyyppiä vastaavan Item- eli tarvikeolion, jos se löytyy tietokannasta.
        """

        cursor = self.connection.cursor()

        if selection == "kaikki":
            all_items_table = cursor.execute(
                "SELECT * FROM  items WHERE username=?", [username]).fetchall()
        else:
            all_items_table = cursor.execute(
                "SELECT * FROM  items WHERE type=? AND username=?", [selection, username]).fetchall()

        return all_items_table

    def delete_item_from_database(self, selected_item: list):
        """Poistaa tietokannasta argumenttina annetut tarviketiedot.

        Args:
            selected_item: tarviketiedot

        Returns:
            Poistetut tarviketiedot.
        """

        cursor = self.connection.cursor()

        deleted_item = cursor.execute(
            "DELETE FROM items WHERE type=? AND description=? AND size=? AND brand=? AND color=? AND username=?", [selected_item[0], selected_item[1], selected_item[2], selected_item[3], selected_item[4], selected_item[5]])

        return deleted_item


item_repository = ItemRepository(get_database_connection())
