from tkinter import Tk
from ui.ui import MasterUI


def main():
    """Metodi, joka käynnistää ohjelman.
    """

    window = Tk()
    window.title("Lastentarvikerekisteri")

    master = MasterUI(window)
    master.start()

    window.minsize(1000, 1000)

    window.mainloop()


if __name__ == "__main__":
    main()
