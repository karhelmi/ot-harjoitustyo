from tkinter import Tk
#from ui_create_new_user import CreateNewUserUI # vain tämä
from repositories.user_repository import user_repository
from user import User
from services.app_service import app_service
from ui.ui_create_new_user import CreateNewUserUI

def main():
    window = Tk()
    window.title("Vaate- ja tarvikerekisteri")

    new_user_page = CreateNewUserUI(window)
    new_user_page.create_new_user_ui()  #start sitten myöhemmin

    window.mainloop()

    #user_repository.create_user_to_database(User("helmi", "salasana"))
    #user = app_service.create_new_user_command("Pekka", "Inkan3")
    #print(user.username)

    user_repository.find_all_users()


if __name__ == "__main__":
    main()
