import customtkinter as ctk

class FormViagem(ctk.CTkFrame):
    """Componente responsável pelo formulário de registro de viagens."""
     
    def __init__(self, master):
        super().__init__(master)
        
        self.campos = {}
        
        self.criar_componentes()
        
    def criar_componentes(self):
        
        self.criar_primeira_linha()
        self.criar_segunda_linha()
        self.criar_terceira_linha()
        self.criar_quarta_linha()
        
        
        botao_salvar = ctk.CTkButton(
        self, text="Salvar",
        command=self.salvar 
        )
        
        botao_salvar.grid(row=5,column=0,padx=10,pady=20)
        
        botao_limpar = ctk.CTkButton(
            self, text="Limpar",
            command=self.limpar
        )
        botao_limpar.grid(row=5,column=1)
        
    def criar_primeira_linha(self):
        
        #Nome
        ctk.CTkLabel(
            self,
            text="Nome"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )
        
        self.campos["nome"] = ctk.CTkEntry(
            self,
            width=250
        )
        
        self.campos["nome"].grid(
            row=0,column=1,
            padx=10,
            pady=10
        )
        # Data
        ctk.CTkLabel(
            self,
            text="Data"
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.campos["data"] = ctk.CTkEntry(
            self,
            width=150
        )

        self.campos["data"].grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        # Carro
        ctk.CTkLabel(
            self,
            text="Carro"
        ).grid(row=0, column=4, padx=10, pady=10, sticky="w")

        self.campos["carro"] = ctk.CTkEntry(
            self,
            width=180
        )

        self.campos["carro"].grid(
            row=0,
            column=5,
            padx=10,
            pady=10
        )

        # Placa
        ctk.CTkLabel(
            self,
            text="Placa"
        ).grid(row=0, column=6, padx=10, pady=10, sticky="w")

        self.campos["placa"] = ctk.CTkEntry(
            self,
            width=120
        )

        self.campos["placa"].grid(
            row=0,
            column=7,
            padx=10,
            pady=10
        )
        
    def get_dados(self):
        """Retorna todos os dados do formulário."""

        return {
        chave: campo.get()
        for chave, campo in self.campos.items()
    }
        
    def limpar(self):
        """Limpa todos os campos do formulário."""

        for campo in self.campos.values():
            campo.delete(0, "end")
            
    def obter_dados(self):

        return {
            "nome": self.entry_nome.get(),
            "data": self.entry_data.get(),
            "carro": self.entry_carro.get(),
            "placa": self.entry_placa.get(),
            "destino": self.entry_destino.get(),
            "km_saida": self.entry_km_saida.get(),
            "hora_saida": self.entry_hora_saida.get(),
            "km_chegada": self.entry_km_chegada.get(),
            "hora_chegada": self.entry_hora_chegada.get()
        }