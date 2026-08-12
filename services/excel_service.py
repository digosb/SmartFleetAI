import os
from openpyxl import Workbook, load_workbook, Workbook
from services.config_service import ConfigService


class ExcelService:

    def __init__(self):
        super().__init__()

    def criar_planilha(self, caminho):
         
            workbook = Workbook()

            worksheet = workbook.active

            worksheet.title = "Controle dos Veiculos"

            worksheet.append(self.headers)

            workbook.save(caminho)

            return workbook
    
    def carregar_planilha(self):

            caminho = self.config.obter_caminho_salvo()

            if not caminho:
                return None

            if not os.path.exists(caminho):
                return self.criar_planilha(caminho)

            return load_workbook(caminho)
    
    def obter_planilha(self):

            workbook = self.carregar_planilha()

            if workbook is None:
                return None

            return workbook.active
        
    def salvar_viagem(self, dados):

            caminho = self.config.obter_caminho_salvo()

            if not caminho:
                return False

            worksheet = self.obter_planilha()

            if worksheet is None:
                return False

            worksheet.append([
                dados["nome"],
                dados["data"],
                dados["km_saida"],
                dados["hora_saida"],
                dados["km_chegada"],
                dados["hora_chegada"],
                dados["destino"],
                dados["carro"],
                dados["placa"]
            ])

            workbook = worksheet.parent
            workbook.save(caminho)

            return True
        
    def listar_viagens(self):

            worksheet = self.obter_planilha()

            if worksheet is None:
                return []

            viagens = []

            for linha in worksheet.iter_rows(min_row=2, values_only=True):

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

            return viagens
        

