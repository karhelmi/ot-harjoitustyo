import unittest
from tests.conftest import build_database_for_tests
from item import Item
from user import User
from repositories.user_repository import user_repository
from repositories.item_repository import item_repository


class TestRepositories(unittest.TestCase):
    def setUp(self):
        build_database_for_tests()

    def test_correct_name_and_password(self):
        user = user_repository.create_user_to_database(User("Testi", "testi"))

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_correct_create_item(self):
        item = item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", "T"))

        self.assertEqual([item.type, item.description, item.size, item.brand, item.color, item.sex],
                         ["vaate", "housut", "92", "Reima", "punainen", "T"])

    def test_correct_item_output(self):
        item_repository.create_item_to_database(Item(
            "vaate", "housut", "92", "Reima", "punainen", "T"))

        item = item_repository.retrieve_items_from_database()

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "T"])
