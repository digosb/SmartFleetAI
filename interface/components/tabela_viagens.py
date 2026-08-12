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

        self.limpar()

        for viagem in viagens:

            self.tree.insert(
                "",
                "end",
                values=(
                    viagem["nome"],
                    viagem["data"],
                    viagem["km_saida"],
                    viagem["hora_saida"],
                    viagem["km_chegada"],
                    viagem["hora_chegada"],
                    viagem["destino"],
                    viagem["carro"],
                    viagem["placa"]
                )
            )


    def limpar(self):

        for item in self.tree.get_children():
            self.tree.delete(item)