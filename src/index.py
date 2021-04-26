from tkinter import Tk, ttk
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

    # määrittää ikkunan minimikoon kaikille ikkunoille
    window.minsize(1000, 1000)

    window.mainloop()

    #style = ttk.Style(window)
    #style.configure("Treeview", rowcount=30)


if __name__ == "__main__":
    main()
