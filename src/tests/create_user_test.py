import unittest
#from ui.ui_create_new_user import CreateNewUserUI
from services.app_service import app_service


class TestCreateUser(unittest.TestCase):
    def setUp(self):
        pass
        #self.created_user = CreateNewUserUI(root)

    def test_correct_name_and_password(self):
        user = app_service.create_new_user_command("Helmi", "Salasana123")

        self.assertEqual([user.username, user.password], ["Helmi", "Salasana123"])