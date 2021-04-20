import unittest
from services.app_service import app_service


class TestAppService(unittest.TestCase):
    def setUp(self):
        #self.created_user = CreateNewUserUI(root)
        pass

    def test_correct_name_and_password(self):
        user = app_service.create_new_user_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_correct_item_inputs(self):
        item = app_service.create_item_command(
            "vaate", "housut", "92", "Reima", "punainen", "T")

        self.assertEqual([item.type, item.description, item.size, item.brand, item.color, item.sex],
                         ["vaate", "housut", "92", "Reima", "punainen", "T"])

    def test_login_returns_correct(self):
        user = app_service.login_command("Testi", "testi")

        self.assertEqual([user.username, user.password],
                         ["Testi", "testi"])

    def test_logout_returns_correct(self):
        user = app_service.logout_command()

        self.assertEqual([user],
                         [None])
