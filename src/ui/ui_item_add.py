from tkinter import Tk, ttk, StringVar, constants, font, OptionMenu
from services.app_service import app_service


class ItemAddUI:
    def __init__(self, root, act_show_logout_view, act_show_item_list_view, username):
        self._root = root
        self.act_show_logout_view = act_show_logout_view
        self.act_show_item_list_view = act_show_item_list_view
        self.frame = None
        self.dropdown = None
        self.dropdown_menu = None
        self.error_message = None
        self.error_label = None
        self.info_message = None
        self.info_label = None

        self.type1_dropdown = ["vaate", "kengät", "tarvike"]
        self.description2_entry = None
        self.size3_entry = None
        self.brand4_entry = None
        self.color5_entry = None
        self.username = username

        self.create_item_add_ui()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def create_item_add_ui(self):
        self.frame = ttk.Frame(master=self._root)

        self.error_message = StringVar(self.frame)
        self.error_label = ttk.Label(
            master=self.frame, textvariable=self.error_message)
        self.error_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        self.info_message = StringVar(self.frame)
        self.info_label = ttk.Label(
            master=self.frame, textvariable=self.info_message)
        self.info_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        heading_label = ttk.Label(
            master=self.frame, text="Lisää tarvike")
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.add_row1_dropdown_type_info()
        self.add_row2_description_info()
        self.add_row3_size_info()
        self.add_row4_brand_info()
        self.add_row5_color_info()
        self.add_row6_username_info()

        self.add_button_layout()

        self.frame.grid_columnconfigure(1, weight=1, minsize=500)

        self.hide_error()

    def add_row1_dropdown_type_info(self):
        type1_label = ttk.Label(
            master=self.frame, text="Tarviketyyppi")
        type1_label.grid(row=1, column=0, padx=5, pady=5)

        self.dropdown = StringVar(master=self.frame)
        self.dropdown.set("Valitse tarviketyyppi")
        self.dropdown_menu = OptionMenu(
            self.frame, self.dropdown, *self.type1_dropdown)
        self.dropdown_menu.grid(
            row=1, column=1, sticky=(constants.W), padx=5, pady=5)

    def add_row2_description_info(self):

        description2_label = ttk.Label(
            master=self.frame, text="Kuvaus (esim. ulkohaalari, housut, paita jne.)")
        description2_label.grid(row=2, column=0, padx=5, pady=5)

        self.description2_entry = ttk.Entry(master=self.frame)
        self.description2_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def add_row3_size_info(self):
        size3_label = ttk.Label(
            master=self.frame, text="Koko (esim. 92, 132, XS)")
        size3_label.grid(row=3, column=0, padx=5, pady=5)

        self.size3_entry = ttk.Entry(master=self.frame)
        self.size3_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def add_row4_brand_info(self):
        brand4_label = ttk.Label(
            master=self.frame, text="Merkki (esim. ReimaTec)")
        brand4_label.grid(row=4, column=0, padx=5, pady=5)

        self.brand4_entry = ttk.Entry(master=self.frame)
        self.brand4_entry.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def add_row5_color_info(self):
        color5_label = ttk.Label(
            master=self.frame, text="Väri")
        color5_label.grid(row=5, column=0, padx=5, pady=5)

        self.color5_entry = ttk.Entry(master=self.frame)
        self.color5_entry.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def add_row6_username_info(self):
        username_label = ttk.Label(
            master=self.frame, text="Käyttäjätili")
        username_label.grid(row=6, column=0, padx=5, pady=5)

        username_label2 = ttk.Label(master=self.frame, text=self.username)
        username_label2.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

    def add_button_layout(self):
        button_add_item = ttk.Button(
            master=self.frame, text="Lisää listaan", command=self.handle_add_item_button_click)
        button_add_item.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        button_logout = ttk.Button(
            master=self.frame, text="Kirjaudu ulos", command=self.handle_logout_button_click)
        button_logout.grid(row=9, column=4, columnspan=2, padx=5, pady=5)

        button_item_list = ttk.Button(
            master=self.frame, text="Siirry listanäkymääsi", command=self.handle_item_list_button_click)
        button_item_list.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

    def handle_add_item_button_click(self):
        self.hide_error()

        type1 = self.dropdown.get()
        description2 = self.description2_entry.get()
        size3 = self.size3_entry.get()
        brand4 = self.brand4_entry.get()
        color5 = self.color5_entry.get()
        username = self.username

        if type1 == "Valitse tarviketyyppi" or len(description2) == 0 or len(size3) == 0 or len(brand4) == 0 or len(color5) == 0:
            self.show_error_message(
                "Et ole vielä täyttänyt kaikkia tietoja. Lisää puuttuvat tiedot.")
            return

        app_service.create_item_command(
            type1, description2, size3, brand4, color5, username)
        self.show_info_message(
            f"Seuraavat tiedot on lisätty listaasi: {type1}, {description2}, {size3}, {brand4}, {color5}. Voit nyt lisätä seuraavan tarvikkeen.")

        self.dropdown.set("Valitse tarviketyyppi")
        self.description2_entry.delete(0, "end")
        self.size3_entry.delete(0, "end")
        self.brand4_entry.delete(0, "end")
        self.color5_entry.delete(0, "end")

    def handle_logout_button_click(self):
        self.act_show_logout_view()

    def handle_item_list_button_click(self):
        self.act_show_item_list_view(self.username)

    def show_error_message(self, message):
        self.hide_info_message()
        self.error_message.set(message)
        self.error_label.grid()

    def hide_error(self):
        self.error_label.grid_remove()

    def show_info_message(self, info_message):
        self.info_message.set(info_message)
        self.info_label.grid()

    def hide_info_message(self):
        self.info_label.grid_remove()
