import os
from openpyxl import Workbook, load_workbook
from services.config_service import ConfigService   


class ExcelService:

    def __init__(self):
        super().__init__()
        
        self.config = ConfigService()   
        
        self.headers = [
            "ID",
            "NOME",
            "DATA",
            "KM SAIDA",
            "HORA SAIDA",
            "KM CHEGADA",
            "HORA CHEGADA",
            "DESTINO",
            "CARRO",
            "PLACA"
        ]

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

            workbook = Workbook()

            worksheet = workbook.active

            worksheet.title = "Controle dos Veiculos"

            worksheet.append(self.headers)

            workbook.save(caminho)

        workbook = load_workbook(caminho)

        worksheet = workbook.active

        # Verifica se a planilha antiga ainda não possui ID
        if worksheet.cell(row=1, column=1).value != "ID":

            worksheet.insert_cols(1)

            worksheet.cell(
                row=1,
                column=1,
                value="ID"
            )

            # Adiciona IDs às viagens já existentes
            for indice in range(2, worksheet.max_row + 1):

                worksheet.cell(
                    row=indice,
                    column=1,
                    value=indice - 1
                )

            workbook.save(caminho)

        return workbook
    
    def obter_planilha(self):

            workbook = self.carregar_planilha()

            if workbook is None:
                return None

            return workbook.active
        
    def salvar_viagem(self, dados):

        caminho = self.config.obter_caminho_salvo()

        if not caminho:
            return False

        workbook = self.carregar_planilha()

        if workbook is None:
            return False

        worksheet = workbook.active

        proximo_id = self.gerar_proximo_id(worksheet)

        worksheet.append([
            proximo_id,
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

        workbook.save(caminho)

        return True
        
    def listar_viagens(self):

        workbook = self.carregar_planilha()

        if workbook is None:
            return []

        worksheet = workbook.active

        viagens = []

        for linha in worksheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if not linha:
                continue

            viagens.append({
                "id": linha[0],
                "nome": linha[1],
                "data": linha[2],
                "km_saida": linha[3],
                "hora_saida": linha[4],
                "km_chegada": linha[5],
                "hora_chegada": linha[6],
                "destino": linha[7],
                "carro": linha[8],
                "placa": linha[9]
            })

        return viagens

    def excluir_viagem(self, id_viagem):
        """Exclui uma viagem pelo ID."""
        caminho = self.config.obter_caminho_salvo()

        if not caminho:
            return False

        workbook = self.carregar_planilha()

        if workbook is None:
            return False

        worksheet = workbook.active

        # Encontra a linha com o ID correspondente
        for indice, linha in enumerate(worksheet.iter_rows(min_row=2, values_only=False), start=2):
            if linha and linha[0].value == id_viagem:
                worksheet.delete_rows(indice)
                workbook.save(caminho)
                return True

        return False
    
    def gerar_proximo_id(self, worksheet):

        maior_id = 0

        for linha in worksheet.iter_rows(
            min_row=2,
            values_only=True
        ):

            if linha and linha[0]:

                try:
                    id_viagem = int(linha[0])

                    if id_viagem > maior_id:
                        maior_id = id_viagem

                except (ValueError, TypeError):
                    continue

        return maior_id + 1

    def editar_viagem(self, id_viagem, dados):
        """Edita uma viagem existente pelo ID."""
        caminho = self.config.obter_caminho_salvo()

        if not caminho:
            return False

        workbook = self.carregar_planilha()

        if workbook is None:
            return False

        worksheet = workbook.active

        # Encontra a linha com o ID correspondente
        for linha in worksheet.iter_rows(min_row=2):
            if linha and linha[0].value == id_viagem:
                linha[1].value = dados.get("nome", "")
                linha[2].value = dados.get("data", "")
                linha[3].value = dados.get("km_saida", "")
                linha[4].value = dados.get("hora_saida", "")
                linha[5].value = dados.get("km_chegada", "")
                linha[6].value = dados.get("hora_chegada", "")
                linha[7].value = dados.get("destino", "")
                linha[8].value = dados.get("carro", "")
                linha[9].value = dados.get("placa", "")
                workbook.save(caminho)
                return True

        return False