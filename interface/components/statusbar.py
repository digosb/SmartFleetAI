import customtkinter as ctk


class StatusBar(ctk.CTkFrame):
    """Barra de status da aplicação."""

    def __init__(self, master):
        super().__init__(master, height=35)

        self.pack_propagate(False)

        self.criar_componentes()

    def criar_componentes(self):

        self.lbl_status = ctk.CTkLabel(
            self,
            text="Sistema iniciado"
        )

        self.lbl_status.pack(
            side="left",
            padx=20
        )

    def atualizar_status(self, mensagem):
        self.lbl_status.configure(text=mensagem)