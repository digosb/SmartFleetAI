import customtkinter as ctk


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.title("SmartFleet AI")
        self.geometry("1200x700")
        self.minsize(1000, 600)

        # Layout
        self.criar_layout()

    def criar_layout(self):

        # Header
        self.header = ctk.CTkFrame(self, height=70)
        self.header.pack(fill="x")
        
        titulo = ctk.CTkLabel(
        self.header,
        text="SmartFleet AI",
        font=("Arial", 24, "bold")
    )

        titulo.pack(side="left", padx=20, pady=15)

        # Conteúdo
        self.content = ctk.CTkFrame(self)
        self.content.pack(fill="both", expand=True, padx=15, pady=15)
        
        titulo_conteudo = ctk.CTkLabel(
        self.content,
        text="Controle de Viagens",
        font=("Arial", 22, "bold")
        )

        titulo_conteudo.pack(anchor="w", padx=20, pady=20)

        # Rodapé
        self.footer = ctk.CTkFrame(self, height=35)
        self.footer.pack(fill="x")
        
        status = ctk.CTkLabel(
        self.footer,
        text="Status: Sistema iniciado"
        )

        status.pack(side="left", padx=20)