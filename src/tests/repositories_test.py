import unittest
from user import User
from item import Item
#from tests.conftest import initialize_database
from repositories.user_repository import user_repository
from repositories.item_repository import item_repository


class TestRepositories(unittest.TestCase):
    def setUp(self):
        # build_database_for_tests()
        self.user = user_repository.create_user_to_database(
            User("Testi", "testi"))

    def test_correct_name_and_password(self):
        self.assertEqual([self.user.username, self.user.password],
                         ["Testi", "testi"])

    def test_correct_create_item(self):
        item = item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", "Testi"))

        self.assertEqual([item.type, item.description, item.size, item.brand, item.color, item.username],
                         ["vaate", "housut", "92", "Reima", "punainen", "Testi"])

    def test_correct_item_output(self):
        username = "Testi"
        selection = "kaikki"

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username))

        item = item_repository.retrieve_items_from_database(
            username, selection)

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "Testi"])

    def test_correct_item_output_type_selection(self):
        username = "Testi"
        selection = "vaate"

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username))

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username))

        item_repository.create_item_to_database(Item(
            "tarvike", "amme", "80x80", "Stokke", "oranssi", username))

        item = item_repository.retrieve_items_from_database(
            username, selection)

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "Testi"])

    def test_correct_item_output_per_username(self):
        username1 = "Testi"
        username2 = "Testi2"
        username3 = "Testi3"
        selection = "vaate"

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username1))

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username2))

        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", username3))

        item = item_repository.retrieve_items_from_database(
            username3, selection)

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "Testi3"])
