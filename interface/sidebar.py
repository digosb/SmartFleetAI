import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.configure(width=220)