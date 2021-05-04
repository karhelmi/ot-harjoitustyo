import unittest
from user import User
from item import Item
from services.app_service import app_service
from tests.conftest import initialize_database


class TestAppService(unittest.TestCase):
    def setUp(self):
        initialize_database()
        #self.user = app_service.create_new_user_command("Testi", "testi")

    def test_correct_name_and_password(self):
        user = app_service.create_new_user_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_correct_item_inputs(self):
        user = app_service.create_new_user_command("Testi", "testi")

        item = app_service.create_item_command(
            "vaate", "housut", "92", "Reima", "punainen", user.username)

        self.assertEqual([item.type, item.description, item.size, item.brand, item.color, item.username],
                         ["vaate", "housut", "92", "Reima", "punainen", "Testi"])

    def test_correct_item_output(self):
        user = app_service.create_new_user_command("Testi", "testi")

        #username = "Testi"
        selection = "kaikki"

        app_service.create_item_command(
            "vaate", "housut", "92", "Reima", "punainen", user.username)

        item = app_service.retrieve_items_command(user.username, selection)

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "Testi"])

    def test_login_returns_correct(self):
        app_service.create_new_user_command("Testi", "testi")

        user = app_service.login_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])
