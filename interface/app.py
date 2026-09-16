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
        self.viagem_service = ViagemService(self.excel)
         
    def _inicializar_variaveis(self):
        """Inicializa as variáveis da aplicação."""

        # Variável para armazenar o caminho da planilha
        self.caminho_planilha = None
        
        # Variável para controlar se está editando uma viagem
        self.viagem_em_edicao = None

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
    
    def salvar_viagem(self, dados):
        """Salva uma nova viagem ou edita uma existente."""
        if self.viagem_em_edicao:
            # Editar viagem existente
            resultado = self.viagem_service.editar_viagem(self.viagem_em_edicao, dados)
            if resultado:
                self.carregar_dados_tabela()
                self.formulario.limpar()
                self.viagem_em_edicao = None
                messagebox.showinfo(
                    "Sucesso",
                    "Viagem editada com sucesso!"
                )
            else:
                messagebox.showwarning(
                    "Dados inválidos",
                    "Verifique se os campos obrigatórios (nome, data, destino) estão preenchidos."
                )
        else:
            # Criar nova viagem
            resultado = self.viagem_service.salvar_viagem(dados)

            if resultado:
                self.carregar_dados_tabela()
                self.formulario.limpar()
                messagebox.showinfo(
                    "Sucesso",
                    "Viagem salva com sucesso!"
                )
            else:
                messagebox.showwarning(
                    "Dados inválidos",
                    "Verifique se os campos obrigatórios (nome, data, destino) estão preenchidos."
                )
                
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

        # Frame para os botões
        frame_botoes = ctk.CTkFrame(self.content)
        frame_botoes.pack(pady=10)

        self.botao_selecionar = ctk.CTkButton(
            frame_botoes,
            text="Selecionar Planilha",
            command=self.selecionar_planilha
        )
        self.botao_selecionar.pack(side="left", padx=5)

        self.botao_editar = ctk.CTkButton(
            frame_botoes,
            text="Editar Viagem",
            command=self.editar_viagem_selecionada
        )
        self.botao_editar.pack(side="left", padx=5)

        self.botao_excluir = ctk.CTkButton(
            frame_botoes,
            text="Excluir Viagem",
            command=self.excluir_viagem
        )
        self.botao_excluir.pack(side="left", padx=5)
      
    def selecionar_planilha(self):

        self.caminho_planilha = self.config.selecionar_planilha()

        if self.caminho_planilha:

            print("Planilha selecionada:")
            print(self.caminho_planilha)

            # Atualiza a tabela caso já exista uma planilha com dados
            self.carregar_dados_tabela()

        else:

            print("Nenhuma planilha selecionada.")
             
    def inicializar_planilha(self):

        self.caminho_planilha = self.config.obter_caminho_salvo()

        if self.caminho_planilha:

            print("Planilha encontrada.")

            self.carregar_dados_tabela()

        else:

            print("Nenhuma planilha configurada.")            
    
    def criar_content(self):

        self.content = ctk.CTkFrame(self)

        self.content.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )
        
    def criar_formulario(self):

        self.formulario = FormViagem(self.content, ao_salvar=self.salvar_viagem)

        self.formulario.pack(
            fill="x",
            padx=20,
            pady=10
         )
        
    def carregar_dados_tabela(self):

        viagens = self.viagem_service.listar_viagens()
        self.tabela.carregar_dados(viagens)
        
    def excluir_viagem(self):
        """Exclui a viagem selecionada."""
        id_viagem = self.tabela.obter_viagem_selecionada()

        if id_viagem is None:
            messagebox.showwarning(
                "Nenhuma seleção",
                "Selecione uma viagem na tabela."
            )
            return

        confirmar = messagebox.askyesno(
            "Confirmar exclusão",
            "Deseja realmente excluir esta viagem?"
        )

        if not confirmar:
            return

        sucesso = self.viagem_service.excluir_viagem(id_viagem)

        if sucesso:
            self.carregar_dados_tabela()
            messagebox.showinfo(
                "Sucesso",
                "Viagem excluída com sucesso!"
            )
        else:
            messagebox.showerror(
                "Erro",
                "Não foi possível excluir a viagem."
            )

    def editar_viagem_selecionada(self):
        """Carrega a viagem selecionada no formulário para edição."""
        id_viagem = self.tabela.obter_viagem_selecionada()

        if id_viagem is None:
            messagebox.showwarning(
                "Nenhuma seleção",
                "Selecione uma viagem na tabela."
            )
            return

        # Encontra os dados da viagem
        viagens = self.viagem_service.listar_viagens()
        viagem = None
        for v in viagens:
            if v["id"] == id_viagem:
                viagem = v
                break

        if viagem is None:
            messagebox.showerror(
                "Erro",
                "Viagem não encontrada."
            )
            return

        # Carrega os dados no formulário
        self.formulario.carregar_dados(viagem)
        self.viagem_em_edicao = id_viagem
            