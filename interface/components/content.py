

def criar_content(self):
    """Cria a área principal da aplicação."""

    # Conteúdo
    self.content = ctk.CTkFrame(self)
    self.content.pack(fill="both", expand=True, padx=15, pady=15)

    titulo_conteudo = ctk.CTkLabel(
        self.content,
        text="Controle de Viagens",
        font=("Arial", 22, "bold")
    )

    titulo_conteudo.pack(anchor="w", padx=20, pady=20)