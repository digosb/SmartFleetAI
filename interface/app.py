import customtkinter as ctk
from interface.components.sidebar import Sidebar
from interface.screens.dashboard import Dashboard
from interface.components.header import Header


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SmartFleet AI")

        self.geometry("1100x700")

        self.minsize(1000, 600)