from tkinter import ttk
import customtkinter as ctk


class TabelaViagens(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        
        self.tree = None

        self.criar_componentes()
        
    def criar_componentes(self):

        colunas = (
            "nome",
            "data",
            "km_saida",
            "hora_saida",
            "km_chegada",
            "hora_chegada",
            "destino",
            "carro",
            "placa"
        )

        self.tree = ttk.Treeview(
            self,
            columns=colunas,
            show="headings"
        )

        self.tree.heading("nome", text="Nome")
        self.tree.heading("data", text="Data")
        self.tree.heading("km_saida", text="KM Saída")
        self.tree.heading("hora_saida", text="Hora Saída")
        self.tree.heading("km_chegada", text="KM Chegada")
        self.tree.heading("hora_chegada", text="Hora Chegada")
        self.tree.heading("destino", text="Destino")
        self.tree.heading("carro", text="Carro")
        self.tree.heading("placa", text="Placa")

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    def carregar_dados(self, viagens):  
        viagens = self.viagem_service.listar_viagens()
        
        self.tabela.carregar_dados(viagens)

    def limpar(self):

        for item in self.tree.get_children():
            self.tree.delete(item)
            
    def criar_tabela(self):

        self.tabela = TabelaViagens(self.content)

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )
        
    def obter_indice_selecionado(self):

        selecao = self.tree.selection()

        if not selecao:
            return None

        item_selecionado = selecao[0]

        indice_visual = self.tree.index(item_selecionado)

        # +2 porque:
        # índice da tabela começa em 0
        # linha 1 do Excel é o cabeçalho
        return indice_visual + 2