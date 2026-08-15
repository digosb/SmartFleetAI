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

        self.config = ConfigService()
        self.excel = ExcelService()
         
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

        self.criar_tabela()
    
    def salvar_viagem(self):
        
        self.viagem_service = ViagemService(self.excel)

        sucesso = self.viagem_service.salvar_viagem(dados)

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
        
        # Obtém os dados do formulário de viagem.
        return self.formulario.obter_dados()  
         
    def criar_tabela(self):

        self.tabela = TabelaViagens(self.content)

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
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

            self.carregar_dados_tabela()

        else:

            print("Nenhuma planilha configurada.")

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
    
    def criar_content(self):

        self.content = ctk.CTkFrame(self)

        self.content.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
        
    def criar_formulario(self):

        self.formulario = FormViagem(self.content)

        self.formulario.pack(
            fill="x",
            padx=20,
            pady=10
         )
        
    def carregar_dados_tabela(self):

        workbook = self.excel.carregar_planilha()

        if workbook is None:
            return

        worksheet = workbook.active

        viagens = []

        for linha in worksheet.iter_rows(min_row=2, values_only=True):

            if linha:

                viagens.append({
                     "nome": linha[0],
                    "data": linha[1],
                    "km_saida": linha[2],
                    "hora_saida": linha[3],
                    "km_chegada": linha[4],
                    "hora_chegada": linha[5],
                    "destino": linha[6],
                    "carro": linha[7],
                    "placa": linha[8]
                })

        self.tabela.carregar_dados(viagens)