from services.excel_service import ExcelService



class ViagemService:

    def __init__(self, excel_service: ExcelService):
        self.excel = excel_service

    def salvar(self):

        dados = self.obter_dados_formulario()

        self.viagem_service.salvar_viagem(dados)

        self.carregar_tabela()

        self.limpar_campos()

    def listar_viagens(self):
        """Retorna todas as viagens."""
        pass

    def editar_viagem(self, id_viagem, dados):
        """Edita uma viagem existente."""
        pass

    def excluir_viagem(self, id_viagem):
        """Exclui uma viagem."""
        pass