import customtkinter as ctk
from interface.components.sidebar import Sidebar
from interface.screens.dashboard import Dashboard
from interface.components.header import Header


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("SmartFleet AI")

        self.geometry("1100x700")

        self.minsize(1000, 600)
        
viagem = Viagem(
    nome=entry_nome.get(),
    data=entry_data.get(),
    km_saida=entry_km_saida.get(),
    hora_saida=entry_hora_saida.get(),
    km_chegada=entry_km_chegada.get(),
    hora_chegada=entry_hora_chegada.get(),
    destino=entry_destino.get(),
    carro=entry_carro.get(),
    placa=entry_placa.get()
)                

worksheet.append([
    viagem.nome,
    viagem.data,
    viagem.km_saida,
    viagem.hora_saida,
    viagem.km_chegada,
    viagem.hora_chegada,
    viagem.destino,
    viagem.carro,
    viagem.placa
])