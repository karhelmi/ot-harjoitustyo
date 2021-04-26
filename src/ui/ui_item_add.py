from tkinter import Tk, ttk, StringVar, constants, font
from services.app_service import app_service


class ItemAddUI:
    def __init__(self, root, act_show_logout_view, act_show_item_list_view):
        self._root = root
        self.act_show_logout_view = act_show_logout_view
        self.act_show_item_list_view = act_show_item_list_view
        self.frame = None
        self.error_message = None
        self.error_label = None
        self.info_message = None
        self.info_label = None

        self.type1_entry = None
        self.description2_entry = None
        self.size3_entry = None
        self.brand4_entry = None
        self.color5_entry = None
        self.sex6_entry = None

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
            master=self.frame, text="Lisää vaate, kengät tai tarvike")
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        type1_label = ttk.Label(
            master=self.frame, text="Tyyppi (vaate, kengät, tarvike)")
        type1_label.grid(row=1, column=0, padx=5, pady=5)

        self.type1_entry = ttk.Entry(master=self.frame)
        self.type1_entry.grid(row=1, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        description2_label = ttk.Label(
            master=self.frame, text="Kuvaus (esim. ulkohaalari, housut, paita jne.)")
        description2_label.grid(row=2, column=0, padx=5, pady=5)

        self.description2_entry = ttk.Entry(master=self.frame)
        self.description2_entry.grid(row=2, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        size3_label = ttk.Label(
            master=self.frame, text="Koko (esim. 92, 132, XS)")
        size3_label.grid(row=3, column=0, padx=5, pady=5)

        self.size3_entry = ttk.Entry(master=self.frame)
        self.size3_entry.grid(row=3, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        brand4_label = ttk.Label(
            master=self.frame, text="Merkki (esim. ReimaTec)")
        brand4_label.grid(row=4, column=0, padx=5, pady=5)

        self.brand4_entry = ttk.Entry(master=self.frame)
        self.brand4_entry.grid(row=4, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        color5_label = ttk.Label(
            master=self.frame, text="Väri")
        color5_label.grid(row=5, column=0, padx=5, pady=5)

        self.color5_entry = ttk.Entry(master=self.frame)
        self.color5_entry.grid(row=5, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        sex6_label = ttk.Label(
            master=self.frame, text="Sukupuoli (T, P, unisex)")
        sex6_label.grid(row=6, column=0, padx=5, pady=5)

        self.sex6_entry = ttk.Entry(master=self.frame)
        self.sex6_entry.grid(row=6, column=1, sticky=(
            constants.E, constants.W), padx=5, pady=5)

        button_add_item = ttk.Button(
            master=self.frame, text="Lisää listaan", command=self.handle_button_click)
        button_add_item.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

        button_logout = ttk.Button(
            master=self.frame, text="Kirjaudu ulos", command=self.handle_logout_button_click)
        button_logout.grid(row=9, column=4, columnspan=2, padx=5, pady=5)

        button_item_list = ttk.Button(
            master=self.frame, text="Siirry listanäkymääsi", command=self.handle_item_list_button_click)
        button_item_list.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

        self.frame.grid_columnconfigure(1, weight=1, minsize=500)

        self.hide_error()

    def handle_button_click(self):
        self.hide_error()

        type1 = self.type1_entry.get()
        description2 = self.description2_entry.get()
        size3 = self.size3_entry.get()
        brand4 = self.brand4_entry.get()
        color5 = self.color5_entry.get()
        sex6 = self.sex6_entry.get()

        if len(type1) == 0 or len(description2) == 0 or len(size3) == 0 or len(brand4) == 0 or len(color5) == 0 or len(sex6) == 0:
            self.show_error_message(
                "Et ole vielä täyttänyt kaikkia tietoja. Lisää puuttuvat tiedot.")
            return

        app_service.create_item_command(
            type1, description2, size3, brand4, color5, sex6)
        self.show_info_message(
            f"Seuraavat tiedot on lisätty listaasi: {type1}, {description2}, {size3}, {brand4}, {color5}, {sex6}. Voit nyt lisätä seuraavan tarvikkeen.")

        self.type1_entry.delete(0, "end")
        self.description2_entry.delete(0, "end")
        self.size3_entry.delete(0, "end")
        self.brand4_entry.delete(0, "end")
        self.color5_entry.delete(0, "end")
        self.sex6_entry.delete(0, "end")

    def handle_logout_button_click(self):
        self.act_show_logout_view()

    def handle_item_list_button_click(self):
        self.act_show_item_list_view()

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
