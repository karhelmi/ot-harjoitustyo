from tkinter import Tk, ttk, StringVar, constants
from services.app_service import app_service


class LoginUI:
    def __init__(self, root, act_show_item_view, act_show_create_user_view):
        self._root = root
        self.act_show_item_view = act_show_item_view
        self.act_show_create_user_view = act_show_create_user_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_message = None
        self.error_label = None

        self.login_ui()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def login_ui(self):
        self.frame = ttk.Frame(master=self._root)

        self.error_message = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame, textvariable=self.error_message)
        self.error_label.grid(row=3, column=0, padx=5, pady=5)

        heading_label = ttk.Label(master=self.frame, text="Kirjaudu sisään")
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        username_label = ttk.Label(master=self.frame, text="Käyttäjätunnus:")
        username_label.grid(row=1, column=0, padx=5, pady=5)

        self.username_entry = ttk.Entry(master=self.frame)
        self.username_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        password_label = ttk.Label(master=self.frame, text="Salasana:")
        password_label.grid(row=2, column=0, padx=5, pady=5)

        self.password_entry = ttk.Entry(master=self.frame)
        self.password_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button_login = ttk.Button(
            master=self.frame, text="Kirjaudu sisään", command=self.handle_login_button_click)
        button_login.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        button_create = ttk.Button(
            master=self.frame, text="Luo uusi tunnus", command=self.handle_create_button_click)
        button_create.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.frame.grid_columnconfigure(1, weight=1, minsize=500)
        self.hide_error()

    def handle_login_button_click(self):
        username_str = self.username_entry.get()
        password_str = self.password_entry.get()

        try:
            app_service.login_command(username_str, password_str)
            self.act_show_item_view()  # Pitää oikeasti mennä Item-näkymään TOIMII!!! :)

        except ValueError:
            self.show_error_message(
                "Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")

    def handle_create_button_click(self):
        self.act_show_create_user_view()  # TOIMII!!!

    def show_error_message(self, message):
        self.error_message.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()
