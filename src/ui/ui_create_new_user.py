from tkinter import Tk, ttk, StringVar, constants, font
from services.app_service import app_service


class CreateNewUserUI:
    def __init__(self, root, act_show_login_view):
        self._root = root
        # self.act_create_user = act_create_user EI PÄÄSE SUORAAN VAATETAULUKKOON
        self.act_show_login_view = act_show_login_view
        self.frame = None
        self.username_entry = None
        self.password_entry = None
        self.error_message = None
        self.error_label = None

        self.create_new_user_ui()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_new_user_ui(self):
        self.frame = ttk.Frame(master=self._root)

        self.error_message = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame, textvariable=self.error_message)
        self.error_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.info_message = StringVar(self.frame)
        self.info_label = ttk.Label(
            master=self.frame, textvariable=self.info_message)
        self.info_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)


        heading_label = ttk.Label(
            master=self.frame, text="Luo uusi käyttäjätunnus ja salasana")
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

        button_create = ttk.Button(
            master=self.frame, text="Luo tunnus", command=self.handle_button_click)
        button_create.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        button_move_to_login = ttk.Button(
            master=self.frame, text="Siirry kirjautumaan sisään", command=self.handle_login_view_button_click)
        button_move_to_login.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

        
        self.frame.grid_columnconfigure(1, weight=1, minsize=500)

        self.hide_error()

    def handle_button_click(self):
        username_str = self.username_entry.get()
        password_str = self.password_entry.get()
        password_star = len(password_str) * "*"

        if len(username_str) == 0 or len(password_str) == 0:
            self.show_error_message(
                "Käyttäjänimi tai salasana ei voi olla tyhjä.")
            return

        try:
            app_service.create_new_user_command(
                username_str, password_str)
            self.show_info_message(f"Käyttäjätunnus {username_str} ja salasana {password_star} luotu onnistuneesti. Siirry kirjautumaan sisään.")
            #self.act_show_login_view()

        except ValueError:
            self.show_error_message(
                f"Käyttäjätunnus {username_str} on jo olemassa. Valitse toinen käyttäjätunnus.")

    def handle_login_view_button_click(self):
        self.act_show_login_view()

    def show_error_message(self, message):
        self.error_message.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def show_info_message(self, info_message):
        self.hide_error()
        self.info_message.set(info_message)
        self.info_label.grid()

    def hide_info_message(self):
        self.info_label.grid_remove()

# Lukee asiat TkInter-taulusta: Lisää nappiin command=self.handle_button_click tai vastaava metodi.
