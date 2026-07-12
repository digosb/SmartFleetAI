import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=60)

        self.grid_columnconfigure(0, weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="SmartFleet AI",
            font=("Arial", 24, "bold")
        )

        titulo.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        versao = ctk.CTkLabel(
            self,
            text="v0.1.0"
        )

        versao.grid(row=0, column=1, padx=20, pady=10, sticky="e")