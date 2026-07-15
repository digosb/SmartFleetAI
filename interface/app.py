# Bibliotecas padrão do Python
from tkinter import filedialog
from tkinter import ttk

# Bibliotecas de terceiros
import customtkinter as ctk

# Módulos do projeto
from services.config_service import ConfigService
from services.excel_service import ExcelService


# Definindo as cores
fundo_tela = "#2e2e2e"

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        
        # Inicializando os serviços
        self.config = ConfigService()
        self.excel = ExcelService()
        
        # Inicializando variáveis
        self.caminho_planilha = None

        # Configuração da janela        
        self.title("SmartFleet AI")
        self.geometry("1200x700")
        self.minsize(1000, 600)
        self.configure(fg_color=fundo_tela)

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
        
        # Formulário
        self.formulario = ctk.CTkFrame(self.content)
        self.formulario.pack(fill="x", padx=20, pady=10)
        # Nome
        label_nome = ctk.CTkLabel(
        self.formulario,
        text="Nome"
    )

        label_nome.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_nome = ctk.CTkEntry(
        self.formulario,
        width=250
    )

        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        
        # Data
        label_data = ctk.CTkLabel(
        self.formulario,
        text="Data"
    )

        label_data.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        self.entry_data = ctk.CTkEntry(
        self.formulario,
        width=150
    )

        self.entry_data.grid(row=0, column=3, padx=10, pady=10)
        
        # Carro
        label_carro = ctk.CTkLabel(
        self.formulario,
        text="Carro"
    )
        label_carro.grid(row=0, column=4, padx=10, pady=10, sticky="w")

        self.entry_carro = ctk.CTkEntry(
        self.formulario,
        width=180
    )
        self.entry_carro.grid(row=0, column=5, padx=10, pady=10)

        # Placa
        label_placa = ctk.CTkLabel(
        self.formulario,
        text="Placa"
    )
        label_placa.grid(row=0, column=6, padx=10, pady=10, sticky="w")

        self.entry_placa = ctk.CTkEntry(
        self.formulario,
        width=120
    )
        self.entry_placa.grid(row=0, column=7, padx=10, pady=10)
        
        # Destino
        label_destino = ctk.CTkLabel(
        self.formulario,
        text="Destino"
    )

        label_destino.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_destino = ctk.CTkEntry(
        self.formulario,
        width=250
    )
        
        self.entry_destino.grid(row=1, column=1, padx=10, pady=10)

        # KM Saída
        label_km_saida = ctk.CTkLabel(
        self.formulario,
        text="KM Saída"
    )
        
        label_km_saida.grid(row=1, column=2, padx=10, pady=10, sticky="w")

        self.entry_km_saida = ctk.CTkEntry(
        self.formulario,
        width=120
    )
        self.entry_km_saida.grid(row=1, column=3, padx=10, pady=10)
        
        # Hora Saída
        label_hora_saida = ctk.CTkLabel(
        self.formulario,
        text="Hora Saída"
    )
        
        label_hora_saida.grid(row=1, column=4, padx=10, pady=10, sticky="w")

        self.entry_hora_saida = ctk.CTkEntry(
        self.formulario,
        width=120
    )
        
        self.entry_hora_saida.grid(row=1, column=5, padx=10, pady=10)

        # KM Chegada
        label_km_chegada = ctk.CTkLabel(
        self.formulario,
        text="KM Chegada"
    )

        label_km_chegada.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.entry_km_chegada = ctk.CTkEntry(
        self.formulario,
        width=120
    )
        
        self.entry_km_chegada.grid(row=2, column=1, padx=10, pady=10)

        # Hora Chegada
        label_hora_chegada = ctk.CTkLabel(
        self.formulario,
        text="Hora Chegada"
    )

        label_hora_chegada.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        self.entry_hora_chegada = ctk.CTkEntry(
        self.formulario,
        width=120
    )
        self.entry_hora_chegada.grid(row=2, column=3, padx=10, pady=10)
        
       # Frame dos botões
        self.frame_botoes = ctk.CTkFrame(self.content)
        self.frame_botoes.pack(fill="x", padx=20, pady=15)
       
        self.btn_salvar = ctk.CTkButton(
        self.frame_botoes,
        text="Salvar",
        width=120,
        command=self.salvar_viagem
    )

        self.btn_salvar.pack(side="left", padx=10)
       
        self.btn_limpar = ctk.CTkButton(
        self.frame_botoes,
        text="Limpar",
        width=120
    )

        self.btn_limpar.pack(side="left", padx=10)

        self.btn_planilha = ctk.CTkButton(
        self.frame_botoes,
        text="Selecionar Planilha",
        width=180,
        command=self.selecionar_planilha
    )

        self.btn_planilha.pack(side="left", padx=10)


        # Frame da tabela
        self.frame_tabela = ctk.CTkFrame(self.content)
        self.frame_tabela.pack(fill="both", expand=True, padx=20, pady=10)
       
        
        colunas = (
        "Nome",
        "Data",
        "Destino",
        "Carro",
        "Placa"
    )

        self.tree = ttk.Treeview(
        self.frame_tabela,
        columns=colunas,
        show="headings"
    )

        for coluna in colunas:
            self.tree.heading(coluna, text=coluna)

        self.tree.column("Nome", width=250)
        self.tree.column("Data", width=100)
        self.tree.column("Destino", width=300)
        self.tree.column("Carro", width=180)
        self.tree.column("Placa", width=120)


        self.tree.pack(fill="both", expand=True)
    
    # Rodapé
        self.footer = ctk.CTkFrame(self, height=35)
        self.footer.pack(fill="x")
        
        status = ctk.CTkLabel(
        self.footer,
        text="Status: Sistema iniciado"
    )

        status.pack(side="left", padx=20)
        self.carregar_tabela()
    
    def salvar_viagem(self):

        dados = self.obter_dados_formulario()

        sucesso = self.excel.salvar_viagem(dados)

        if sucesso:

            self.carregar_tabela()

            print("Viagem salva com sucesso!")

        else:

            print("Erro ao salvar a viagem.") 
            
    def obter_dados_formulario(self):
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
            
    def carregar_tabela(self):

        # Limpa a Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        workbook = self.excel.carregar_planilha()

        if workbook is None:
            return

        worksheet = workbook["Controle dos Veiculos"]

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

        caminho = filedialog.askopenfilename(
        title="Selecione a planilha de viagens",
        filetypes=[
            ("Planilhas Excel", "*.xlsx"),
            ("Todos os arquivos", "*.*")
        ]
    )


        if caminho:

            self.caminho_planilha = self.config.selecionar_planilha()

            print("Planilha selecionada:")
            print(self.caminho_planilha)

        else:

            print("Nenhuma planilha selecionada.")
            
           
        