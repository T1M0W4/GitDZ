from netlistener import Listener
from netsender import Sender
from database import Database

class View:

    def __init__(self, controller):
        self.controller = controller

    def show_message(self, name_from, message):
        name_from = name_from.title()
        print(f"{name_from}: {message}")

    def get_message(self):
        msg = input('>>> ')
        # Привет всем!  - (для всех)
        # @иман Привет  - (иману)
        msg = msg.strip()
        self.controller.on_input(msg)
