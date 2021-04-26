from tkinter import Tk, ttk, StringVar, constants, font
import tkinter as tk
from services.app_service import app_service


class ItemListUI:
    def __init__(self, root, act_show_logout_view, act_show_item_add_view):
        self._root = root
        self.act_show_logout_view = act_show_logout_view
        self.act_show_item_add_view = act_show_item_add_view
        self.frame = None
        self.error_message = None
        self.error_label = None
        self.info_message = None
        self.info_label = None
        # self.type1 =
        #self.description2_entry = None
        #self.size3_entry = None
        #self.brand4_entry = None
        #self.color5_entry = None
        #self.sex6_entry = None

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
        #self.frame.grid_rowconfigure(1, weight=1, minsize=700)

        button_logout = tk.Button(
            master=self.frame, text="Kirjaudu ulos", command=self.handle_logout_button_click)
        button_logout.grid(row=3, column=3, columnspan=2, padx=5, pady=5)

        button_add_item = tk.Button(
            master=self.frame, text="Lisää uusi tarvike", command=self.handle_add_item_button_click)
        button_add_item.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

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
        self.tree.heading("#6", text="Sukupuoli")
        #self.tree.grid(row=2, columnspan=6)

        all_items_table = app_service.retrieve_items_command()

        #self.tree.insert("", tk.END, values=("1", "2", "3", "4", "5", "6"))

        for row in all_items_table:
            self.tree.insert("", tk.END, values=(
                row[1], row[2], row[3], row[4], row[5], row[6]))

        #self.error_message = StringVar(self.frame)
        # self.error_label = ttk.Label(
         #   master=self.frame, textvariable=self.error_message)
        #self.error_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        #self.info_message = StringVar(self.frame)
        # self.info_label = ttk.Label(
         #   master=self.frame, textvariable=self.info_message)
        #self.info_label.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

        # heading_label = ttk.Label(
         #   master=self.frame, text="Tarvikelistasi")
        #heading_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # self.hide_error()

    # def handle_button_click(self): ####Ei voi palauttaa kuin yhden taulukon. Myöhemmin voi lisätä usernamen.
     #   app_service.retrieve_items_command()

    def handle_logout_button_click(self):
        self.act_show_logout_view()

    def handle_add_item_button_click(self):
        self.act_show_item_add_view()

    # def show_error_message(self, message):
     #   self.hide_info_message()
     #   self.error_message.set(message)
    #    self.error_label.grid()

   # def hide_error(self):
  #      self.error_label.grid_remove()

    # def show_info_message(self, info_message):
   #     self.info_message.set(info_message)
  #      self.info_label.grid()

 #   def hide_info_message(self):
#        self.info_label.grid_remove()
