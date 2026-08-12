# Bibliotecas padrão do Python
from tkinter import messagebox

# Bibliotecas de terceiros
import customtkinter as ctk

# Módulos do projeto
from interface.components.header import Header
from services.config_service import ConfigService
from services.excel_service import ExcelService
from interface.components.form_viagem import FormViagem
from services.viagem_service import ViagemService
from interface.components.tabela_viagens import TabelaViagens


# Definindo as cores
fundo_tela = "#2e2e2e"

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        # Inicializando os serviços
        self._inicializar_servicos()
        self._inicializar_variaveis()
        
        # Configurando a janela   
        self.configurar_janela()
    
        # Layout
        self.criar_layout()
        
        # Inicializando a planilha
        self.inicializar_planilha()
        
    def _inicializar_servicos(self):
        """Inicializa os serviços da aplicação."""

        # Inicializa os serviços de configuração e Excel
        self.config = ConfigService()
        self.excel = ExcelService()
        self.viagem_service = ViagemService(self.excel)
        self.tabela = TabelaViagens(self.content)
        
    def _inicializar_variaveis(self):
        """Inicializa as variáveis da aplicação."""

        # Variável para armazenar o caminho da planilha
        self.caminho_planilha = None

    def configurar_janela(self):
             # Configuração da janela        
            self.title("SmartFleet AI")
            self.geometry("1200x700")
            self.minsize(1000, 600)
            self.configure(fg_color=fundo_tela)
            
    def criar_layout(self):

        self.header = Header(self)
        self.header.pack(fill="x")

        self.criar_content()

        self.criar_formulario()

        self.criar_botoes()

        self.criar_tabela()

        self.criar_footer()
    
    def salvar_viagem(self):

        dados = self.obter_dados_formulario()

        if not self.validar_dados(dados):
            return

        sucesso = self.excel.salvar_viagem(dados)

        if sucesso:
            self.carregar_tabela()
            self.limpar_campos()

            ctk.CTkMessagebox(
                title="Sucesso",
                message="Viagem salva com sucesso!"
            )
            messagebox.showinfo(
                "Sucesso",
                "Viagem salva com sucesso!"
            )

        else:

            print("Erro ao salvar a viagem.")
            
    def obter_dados_formulario(self):
        dados = self.formulario.obter_dados()  
            
    def carregar_tabela(self):

        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        workbook = self.excel.carregar_planilha()

        if workbook is None:
            return

        worksheet = workbook.active

        for linha in worksheet.iter_rows(min_row=2, values_only=True):

            if linha:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        linha[0],  # Nome
                        linha[1],  # Data
                        linha[6],  # Destino
                        linha[7],  # Carro
                        linha[8]   # Placa
                    )
                )        
            
    def selecionar_planilha(self):

        self.caminho_planilha = self.config.selecionar_planilha()

        if self.caminho_planilha:

            print("Planilha selecionada:")
            print(self.caminho_planilha)

            # Atualiza a tabela caso já exista uma planilha com dados
            self.carregar_tabela()

        else:

            print("Nenhuma planilha selecionada.")
             
    def inicializar_planilha(self):

        self.caminho_planilha = self.config.obter_caminho_salvo()

        if self.caminho_planilha:

            print("Planilha encontrada.")

            self.carregar_tabela()

        else:

            print("Nenhuma planilha configurada.")
            
        self.entry_nome.delete(0, "end")
        self.entry_data.delete(0, "end")
        self.entry_carro.delete(0, "end")
        self.entry_placa.delete(0, "end")
        self.entry_destino.delete(0, "end")
        self.entry_km_saida.delete(0, "end")
        self.entry_hora_saida.delete(0, "end")
        self.entry_km_chegada.delete(0, "end")
        self.entry_hora_chegada.delete(0, "end")

    def validar_dados(self, dados):

        if not dados["nome"]:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o nome."
            )
            return False

        if not dados["data"]:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe a data."
            )
            return False

        if not dados["destino"]:
            messagebox.showwarning(
                "Campo obrigatório",
                "Informe o destino."
            )
            return False

        return True            