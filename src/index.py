from tkinter import Tk, ttk
from repositories.user_repository import user_repository
from user import User
from services.app_service import app_service
from ui.ui import MasterUI
from database_initialize import initialize_database


def main():
    """Metodi, joka käynnistää ohjelman.
    """
    # initialize_database()

    window = Tk()
    window.title("Vaate- ja tarvikerekisteri")

    master = MasterUI(window)
    master.start()

    # määrittää ikkunan minimikoon kaikille ikkunoille
    window.minsize(1000, 1000)

    window.mainloop()


if __name__ == "__main__":
    main()
