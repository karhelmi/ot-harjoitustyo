from tkinter import ttk, StringVar, constants, OptionMenu
import tkinter as tk
from services.app_service import app_service


class ItemListUI:
    def __init__(self, root, act_show_logout_view, act_show_item_add_view, username):
        self._root = root
        self.act_show_logout_view = act_show_logout_view
        self.act_show_item_add_view = act_show_item_add_view
        self.frame = None
        self.tree = None
        self.error_message = None
        self.error_label = None
        self.info_message = None
        self.info_label = None
        self.username = username
        self.selection_dropdown = ["kaikki", "vaate", "kengät", "muu tarvike"]
        self.selection = self.selection_dropdown[0]

        self.show_item_list_ui()

    def pack(self):
        self.frame.pack(fill=constants.X)
        self.tree.pack(fill=constants.BOTH, expand=1)

    def destroy(self):
        self.frame.destroy()
        self.tree.destroy()

    def show_item_list_ui(self):
        self.frame = ttk.Frame(master=self._root)
        heading_label = ttk.Label(
            master=self.frame, text="Tarvikelistasi")
        heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        self.frame.grid_columnconfigure(1, weight=1, minsize=1000)

        button_logout = tk.Button(
            master=self.frame, text="Kirjaudu ulos", command=self.handle_logout_button_click)
        button_logout.grid(row=3, column=2, columnspan=2, padx=5, pady=5)

        button_add_item = tk.Button(
            master=self.frame, text="Lisää uusi tarvike", command=self.handle_add_item_button_click)
        button_add_item.grid(row=3, column=0, padx=5, pady=5)

        button_delete_item = tk.Button(
            master=self.frame, text="Poista valittu tarvike", command=self.handle_delete_item_button_click)
        button_delete_item.grid(row=4, column=0, padx=5, pady=5)

        button_selection = tk.Button(
            master=self.frame, text="Näytä valitut tarvikkeet", command=self.handle_selection_button_click)
        button_selection.grid(row=5, column=0, padx=5, pady=5)

        self.dropdown = StringVar(master=self.frame)
        self.dropdown.set(self.selection)
        self.dropdown_menu = OptionMenu(
            self.frame, self.dropdown, *self.selection_dropdown)
        self.dropdown_menu.grid(
            row=5, column=1, sticky=(constants.W), padx=5, pady=5)

        self.show_item_table_as_list()

    def show_item_table_as_list(self):
        self.tree = ttk.Treeview(master=self._root, column=(
            "c1", "c2", "c3", "c4", "c5", "c6"), show="headings")
        self.tree.column("#1", anchor=tk.CENTER)
        self.tree.heading("#1", text="Tyyppi")
        self.tree.column("#2", anchor=tk.CENTER)
        self.tree.heading("#2", text="Kuvaus")
        self.tree.column("#3", anchor=tk.CENTER)
        self.tree.heading("#3", text="Koko")
        self.tree.column("#4", anchor=tk.CENTER)
        self.tree.heading("#4", text="Merkki")
        self.tree.column("#5", anchor=tk.CENTER)
        self.tree.heading("#5", text="Väri")
        self.tree.column("#6", anchor=tk.CENTER)
        self.tree.heading("#6", text="Käyttäjätunnus")

        all_items_table = app_service.retrieve_items_command(
            self.username, self.selection)

        for row in all_items_table:
            self.tree.insert("", tk.END, values=(
                row[1], row[2], row[3], row[4], row[5], row[6]))

    def handle_selection_button_click(self):
        self.tree.destroy()
        self.selection = self.dropdown.get()

        self.show_item_table_as_list()
        self.pack()

    def handle_logout_button_click(self):
        self.act_show_logout_view()

    def handle_add_item_button_click(self):
        self.act_show_item_add_view(self.username)

    def handle_delete_item_button_click(self):
        selected_row = self.tree.selection()[0]
        selected_item = list(self.tree.item(selected_row)['values'])
        app_service.delete_item_command(selected_item)
        self.tree.delete(selected_row)
