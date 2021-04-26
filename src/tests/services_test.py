import unittest
from services.app_service import app_service
from tests.conftest import build_database_for_tests


class TestAppService(unittest.TestCase):
    def setUp(self):
        build_database_for_tests()

    def test_correct_name_and_password(self):

        user = app_service.create_new_user_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_correct_item_inputs(self):
        item = app_service.create_item_command(
            "vaate", "housut", "92", "Reima", "punainen", "T")

        self.assertEqual([item.type, item.description, item.size, item.brand, item.color, item.sex],
                         ["vaate", "housut", "92", "Reima", "punainen", "T"])

    def test_correct_item_output(self):
        app_service.create_item_command(
            "vaate", "housut", "92", "Reima", "punainen", "T")

        item = app_service.retrieve_items_command()

        for row in item:
            self.assertEqual([row[1], row[2], row[3], row[4], row[5], row[6]],
                             ["vaate", "housut", "92", "Reima", "punainen", "T"])

    def test_login_returns_correct(self):
        user = app_service.create_new_user_command("Testi", "testi")
        user = app_service.login_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_logout_returns_correct(self):
        user = app_service.logout_command()

        self.assertEqual([user],
                         [None])
