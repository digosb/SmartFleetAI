import json
import os
from tkinter import filedialog

class ConfigService:

    def __init__(self):

        self.config_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.json"
        )
        
        
    def carregar_config(self):

        with open(self.config_file, "r", encoding="utf-8") as arquivo:

            return json.load(arquivo)        
    
    
    def salvar_config(self, dados):

        with open(self.config_file, "w", encoding="utf-8") as arquivo:

            json.dump(dados, arquivo, indent=4)    
        
        
    def selecionar_planilha(self):

        caminho = filedialog.askopenfilename(
            title="Selecione a planilha de viagens",
            filetypes=[
                ("Planilhas Excel", "*.xlsx"),
                ("Todos os arquivos", "*.*")
        ]
    )

        return caminho        

    def obter_caminho_excel(self):

        config = self.carregar_config()

        caminho = config.get("excel_path", "")
    
        if caminho and os.path.exists(caminho):
            return caminho
        
        caminho = self.selecionar_planilha()

        if caminho:

            config["excel_path"] = caminho

            self.salvar_config(config)

            return caminho

        return None

