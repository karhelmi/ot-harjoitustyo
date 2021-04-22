from user import User
from item import Item
# suhteessa suoritettavaan tiedostoon! Eli index-tiedostoon tässä mallissa.
from repositories.user_repository import user_repository
from repositories.item_repository import item_repository


class AppService:
    def __init__(self, user_repository, item_repository):
        self.user = None
        self.user_repository = user_repository
        self.item_repository = item_repository

    def create_new_user_command(self, username, password):
        user_exists = self.user_repository.find_by_username(username)

        if user_exists:
            # (f"Käyttäjätunnus {username} on jo olemassa. Valitse toinen käyttäjätunnus.")
            raise ValueError

        user = self.user_repository.create_user_to_database(
            User(username, password))

        return user

    def login_command(self, username, password):
        user = self.user_repository.find_by_username(username)

        if user is None or user.password != password:
            raise ValueError(
                "Annettua käyttäjätunnusta ei löytynyt tai salasana on väärä.")

        self.user = user

        return user

    def create_item_command(self, type1, description2, size3, brand4, color5, sex6):
        item = self.item_repository.create_item_to_database(
            Item(type1, description2, size3, brand4, color5, sex6))

        return item

    def retrieve_items_command(self):
        all_items_table = self.item_repository.retrieve_items_from_database()

        return all_items_table

    def logout_command(self):
        self.user = None

        return self.user


app_service = AppService(user_repository, item_repository)
