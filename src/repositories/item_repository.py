import sqlite3
import os
from item import Item
from database_connection import get_database_connection


def get_item_by_row(row):
    if row:
        return Item(row["type"], row["description"], row["size"], row["brand"], row["color"], row["sex"])


class ItemRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_item_to_database(self, item):
        cursor = self.connection.cursor()

        cursor.execute("INSERT INTO  items (type, description, size, brand, color, sex) VALUES (?, ?, ?, ?, ?, ?)", [
                       item.type, item.description, item.size, item.brand, item.color, item.sex])

        self.connection.commit()

        return item

    def find_all_items(self):
        cursor = self.connection.cursor()

        all_items_table = cursor.execute("SELECT * FROM  items").fetchall()

        print("Lista luoduista vaatteista, kengistä ja tarvikkeista")

        for row in all_items_table:
            print(row["type"], row["description"], row["size"],
                  row["brand"], row["color"], row["sex"])

    def find_by_item_type(self, typex):
        cursor = self.connection.cursor()

        row = cursor.execute(
            "SELECT * FROM  items WHERE type = ?", (typex,)).fetchall()

        return get_item_by_row(row)


item_repository = ItemRepository(get_database_connection())
