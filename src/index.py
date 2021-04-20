from tkinter import Tk
from repositories.user_repository import user_repository
from user import User
from services.app_service import app_service
from ui.ui import MasterUI
from database_initialize import initialize_database


def main():

    initialize_database()

    window = Tk()
    window.title("Vaate- ja tarvikerekisteri")

    master = MasterUI(window)
    master.start()

    window.mainloop()

    # 1 new_user_page = CreateNewUserUI(window)
    # 1 new_user_page.create_new_user_ui()  #start sitten myöhemmin

    # 2login_page = LoginUI(window)
    # 2login_page.login_ui()

    #user_repository.create_user_to_database(User("helmi", "salasana"))
    #user = app_service.create_new_user_command("Pekka", "Inkan3")

    # user_repository.find_all_users()

    # initialize_database()


if __name__ == "__main__":
    main()
