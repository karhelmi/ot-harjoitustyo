from user import User
from repositories.user_repository import user_repository ## suhteessa suoritettavaan tiedostoon! Eli index-tiedostoon tässä mallissa.

class AppService:
    def __init__(self, user_repository): 
        self.user = None
        #self.row_item_repository = row_item_repository LISÄTÄÄN MYÖHEMMIN
        self.user_repository = user_repository

    def create_new_user_command(self, username, password):
        user = self.user_repository.create_user_to_database(User(username, password)) #Ihan kuin tuota Useria ei luettaisi, miksi?
        return user


app_service = AppService(user_repository)