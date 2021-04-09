from tkinter import Tk, ttk, constants
from services.app_service import app_service

class CreateNewUserUI :
    def __init__(self, root):
        self._root = root
        self.username_entry = None
        self.password_entry = None
        self.frame = None

    def destroy(self):
        self.frame.pack(fill=constants.X)

    def create_new_user_ui(self):
        heading_label = ttk.Label(master=self._root, text="Luo uusi käyttäjätunnus ja salasana")
        heading_label.grid(row=0, column=0, columnspan=2, padx = 5, pady = 5)

        username_label = ttk.Label(master=self._root, text = "Käyttäjätunnus:")
        username_label.grid(row=1, column=0, padx = 5, pady = 5)
 
        self.username_entry = ttk.Entry(master=self._root)
        self.username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx = 5, pady = 5)

        password_label = ttk.Label(master=self._root, text = "Salasana:")
        password_label.grid(row=2, column=0, padx = 5, pady = 5)

        self.password_entry = ttk.Entry(master=self._root)
        self.password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx = 5, pady = 5)

        button_create = ttk.Button(master=self._root, text="Luo tunnus", command=self.handle_button_click)
        button_create.grid(row=3, column=0, columnspan=2, padx = 5, pady = 5)

        self._root.grid_columnconfigure(1, weight=1, minsize = 500)
       
    def handle_button_click(self):
        self.username_str = self.username_entry.get()
        self.password_str = self.password_entry.get()
        password_star = len(self.password_str) * "*"
        app_service.create_new_user_command(self.username_str, self.password_str)
        print(f"Käyttäjätunnus {self.username_str} ja salasana {password_star} luotu onnistuneesti.")


## Lukee asiat TkInter-taulusta: Lisää nappiin command=self.handle_button_click tai vastaava metodi.
