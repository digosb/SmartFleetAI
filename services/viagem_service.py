from services.excel_service import ExcelService


class ViagemService:

    def __init__(self, excel_service):
        self.excel = excel_service

    def salvar_viagem(self, dados):

        if not self.validar_dados(dados):
            return False

        return self.excel.salvar_viagem(dados)

    def validar_dados(self, dados):

        if not dados["nome"]:
            return False

        if not dados["data"]:
            return False

        if not dados["destino"]:
            return False

        return True

    def listar_viagens(self):
        return self.excel.listar_viagens()

    def excluir_viagem(self, indice):

        return self.excel.excluir_viagem(indice)

    def editar_viagem(self):
        pass