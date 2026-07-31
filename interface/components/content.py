def criar_content(self):
    """Cria a área principal da aplicação."""

    self.content = ctk.CTkFrame(self)
    self.content.pack(
        fill="both",
        expand=True,
        padx=15,
        pady=15
    )

    titulo = ctk.CTkLabel(
        self.content,
        text="Controle de Viagens",
        font=("Arial", 22, "bold")
    )

    titulo.pack(
        anchor="w",
        padx=20,
        pady=20
    )