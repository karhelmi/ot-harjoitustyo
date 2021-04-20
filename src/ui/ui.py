from ui.ui_login import LoginUI
from ui.ui_create_new_user import CreateNewUserUI
from ui.ui_item import ItemUI
from ui.ui_logout import LogoutUI


class MasterUI:
    def __init__(self, root):
        self._root = root
        self.current_view = None

    def start(self):
        self.show_login_view()
        # self.show_create_user_view()

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()

        self.current_view = LoginUI(
            self._root, self.show_item_view, self.show_create_user_view)

        self.current_view.pack()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateNewUserUI(self._root, self.show_login_view)
        #self.current_view = CreateNewUserUI(self._root, self.show_item_view, self.show_login_view)

        self.current_view.pack()

    def show_item_view(self):
        self.hide_current_view()

        self.current_view = ItemUI(self._root, self.show_logout_view)

        self.current_view.pack()

    def show_logout_view(self):
        self.hide_current_view()

        self.current_view = LogoutUI(self._root, self.show_login_view)

        self.current_view.pack()
