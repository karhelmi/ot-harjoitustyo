from tkinter import Tk, ttk, StringVar, constants
from services.app_service import app_service


class LogoutUI:
    def __init__(self, root, act_show_login_view):
        self._root = root
        self.act_show_login_view = act_show_login_view
        self.frame = None

        self.logout_ui()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def logout_ui(self):
        self.frame = ttk.Frame(master=self._root)

        label1 = ttk.Label(master=self.frame,
                           text="Kirjauduit ulos palvelusta")
        label1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        label2 = ttk.Label(
            master=self.frame, text="Jos haluat kirjautua takaisin palveluun, pääset kirjautumissivulle alta.")
        label2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        button_move_login = ttk.Button(
            master=self.frame, text="Siirry sisäänkirjautumissivulle", command=self.handle_button_click)
        button_move_login.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.frame.grid_columnconfigure(1, weight=1, minsize=500)

    def handle_button_click(self):
        self.act_show_login_view()
