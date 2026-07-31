import customtkinter as ctk


class Header(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master, height=60)

        self.grid_columnconfigure(0, weight=1)

        self.criar_componentes()

    def criar_componentes(self):

        self.lbl_titulo = ctk.CTkLabel(
            self,
            text="SmartFleet AI",
            font=("Arial", 24, "bold")
        )

        self.lbl_titulo.grid(
            row=0,
            column=0,
            padx=20,
            pady=10,
            sticky="w"
        )

        self.lbl_versao = ctk.CTkLabel(
            self,
            text="v0.1.0"
        )

        self.lbl_versao.grid(
            row=0,
            column=1,
            padx=20,
            pady=10,
            sticky="e"
        )