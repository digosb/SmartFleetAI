import customtkinter as ctk


class FormViagem(ctk.CTkFrame):
    """Componente responsável pelo formulário de registro de viagens."""

    def __init__(self, master):
        super().__init__(master)

        self.campos = {}
        self.ao_salvar = ao_salvar

        self.criar_componentes()

    def criar_componentes(self):

        self.criar_primeira_linha()
        self.criar_segunda_linha()
        self.criar_terceira_linha()

        botao_salvar = ctk.CTkButton(
            self,
            text="Salvar",
            command=self.salvar
        )

        botao_salvar.grid(
            row=4,
            column=0,
            padx=10,
            pady=20
        )

        botao_limpar = ctk.CTkButton(
            self,
            text="Limpar",
            command=self.limpar
        )

        botao_limpar.grid(
            row=4,
            column=1,
            padx=10,
            pady=20
        )

    def criar_primeira_linha(self):

        # Nome
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
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        # Data
        ctk.CTkLabel(
            self,
            text="Data"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

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
        ).grid(
            row=0,
            column=4,
            padx=10,
            pady=10,
            sticky="w"
        )

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
        ).grid(
            row=0,
            column=6,
            padx=10,
            pady=10,
            sticky="w"
        )

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

    def criar_segunda_linha(self):

        # Destino
        ctk.CTkLabel(
            self,
            text="Destino"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.campos["destino"] = ctk.CTkEntry(
            self,
            width=250
        )

        self.campos["destino"].grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        # KM Saída
        ctk.CTkLabel(
            self,
            text="KM Saída"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.campos["km_saida"] = ctk.CTkEntry(
            self,
            width=120
        )

        self.campos["km_saida"].grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        # Hora Saída
        ctk.CTkLabel(
            self,
            text="Hora Saída"
        ).grid(
            row=1,
            column=4,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.campos["hora_saida"] = ctk.CTkEntry(
            self,
            width=120
        )

        self.campos["hora_saida"].grid(
            row=1,
            column=5,
            padx=10,
            pady=10
        )

    def criar_terceira_linha(self):

        # KM Chegada
        ctk.CTkLabel(
            self,
            text="KM Chegada"
        ).grid(
            row=2,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.campos["km_chegada"] = ctk.CTkEntry(
            self,
            width=120
        )

        self.campos["km_chegada"].grid(
            row=2,
            column=1,
            padx=10,
            pady=10
        )

        # Hora Chegada
        ctk.CTkLabel(
            self,
            text="Hora Chegada"
        ).grid(
            row=2,
            column=2,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.campos["hora_chegada"] = ctk.CTkEntry(
            self,
            width=120
        )

        self.campos["hora_chegada"].grid(
            row=2,
            column=3,
            padx=10,
            pady=10
        )

    def obter_dados(self):
        """Retorna os dados preenchidos no formulário."""

        return {
            chave: campo.get()
            for chave, campo in self.campos.items()
        }

    def limpar(self):
        """Limpa todos os campos do formulário."""

        for campo in self.campos.values():
            campo.delete(0, "end")

    def salvar(self):
        """Será conectado ao fluxo de salvamento posteriormente."""

        dados = self.obter_dados()
        if self.ao_salvar:
            self.ao_salvar(dados)