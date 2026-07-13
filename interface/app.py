import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SmartFleet AI")

        self.geometry("1200x700")

        self.minsize(1000, 600)