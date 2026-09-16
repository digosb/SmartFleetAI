#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test script to verify the complete CRUD flow of the SmartFleet AI application.
This tests the services without the GUI.
"""

import os
import sys
import tempfile
from pathlib import Path

# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from services.config_service import ConfigService
from services.excel_service import ExcelService
from services.viagem_service import ViagemService


def criar_config_teste():
    """Cria uma configuração de teste com arquivo temporário."""
    config = ConfigService()
    
    # Usa um arquivo temporário para testes
    temp_dir = tempfile.gettempdir()
    temp_file = os.path.join(temp_dir, "teste_viagens.xlsx")
    
    # Salva o caminho no config
    config_data = {"excel_path": temp_file}
    config.salvar_config(config_data)
    
    return config, temp_file


def teste_criar_planilha():
    """Teste 1: Criar uma planilha do zero"""
    print("\n" + "="*60)
    print("TESTE 1: CRIAR PLANILHA")
    print("="*60)
    
    config, temp_file = criar_config_teste()
    excel = ExcelService()
    
    # Remove arquivo se existir
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Cria a planilha
    workbook = excel.criar_planilha(temp_file)
    
    if os.path.exists(temp_file):
        print("✓ Planilha criada com sucesso!")
        print(f"  Localização: {temp_file}")
        return True
    else:
        print("✗ Falha ao criar planilha")
        return False


def teste_salvar_viagem():
    """Teste 2: Salvar uma viagem"""
    print("\n" + "="*60)
    print("TESTE 2: SALVAR VIAGEM")
    print("="*60)
    
    config, temp_file = criar_config_teste()
    excel = ExcelService()
    viagem_service = ViagemService(excel)
    
    # Remove arquivo se existir para começar do zero
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Cria a planilha
    excel.criar_planilha(temp_file)
    
    # Dados de teste
    dados_viagem = {
        "nome": "João Silva",
        "data": "2024-01-15",
        "carro": "Toyota Corolla",
        "placa": "ABC-1234",
        "destino": "São Paulo",
        "km_saida": 100,
        "hora_saida": "08:00",
        "km_chegada": 250,
        "hora_chegada": "12:00"
    }
    
    # Salva a viagem
    resultado = viagem_service.salvar_viagem(dados_viagem)
    
    if resultado:
        print("✓ Viagem salva com sucesso!")
        print(f"  Dados: {dados_viagem}")
        return True
    else:
        print("✗ Falha ao salvar viagem")
        return False


def teste_listar_viagens():
    """Teste 3: Listar viagens"""
    print("\n" + "="*60)
    print("TESTE 3: LISTAR VIAGENS")
    print("="*60)
    
    config, temp_file = criar_config_teste()
    excel = ExcelService()
    viagem_service = ViagemService(excel)
    
    # Remove arquivo se existir
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Cria a planilha
    excel.criar_planilha(temp_file)
    
    # Salva algumas viagens
    viagens_dados = [
        {
            "nome": "João Silva",
            "data": "2024-01-15",
            "carro": "Toyota Corolla",
            "placa": "ABC-1234",
            "destino": "São Paulo",
            "km_saida": 100,
            "hora_saida": "08:00",
            "km_chegada": 250,
            "hora_chegada": "12:00"
        },
        {
            "nome": "Maria Santos",
            "data": "2024-01-16",
            "carro": "Honda Civic",
            "placa": "XYZ-5678",
            "destino": "Rio de Janeiro",
            "km_saida": 50,
            "hora_saida": "09:00",
            "km_chegada": 200,
            "hora_chegada": "14:00"
        }
    ]
    
    for dados in viagens_dados:
        viagem_service.salvar_viagem(dados)
    
    # Lista as viagens
    viagens = viagem_service.listar_viagens()
    
    if len(viagens) == 2:
        print("✓ Viagens listadas com sucesso!")
        for v in viagens:
            print(f"  ID: {v['id']}, Nome: {v['nome']}, Destino: {v['destino']}")
        return True
    else:
        print(f"✗ Esperado 2 viagens, obteve {len(viagens)}")
        return False


def teste_validacao():
    """Teste 4: Validação de dados obrigatórios"""
    print("\n" + "="*60)
    print("TESTE 4: VALIDAÇÃO DE DADOS")
    print("="*60)
    
    excel = ExcelService()
    viagem_service = ViagemService(excel)
    
    # Dados inválidos (sem nome)
    dados_invalidos = {
        "nome": "",
        "data": "2024-01-15",
        "carro": "Toyota",
        "placa": "ABC-1234",
        "destino": "São Paulo",
        "km_saida": 100,
        "hora_saida": "08:00",
        "km_chegada": 250,
        "hora_chegada": "12:00"
    }
    
    resultado = viagem_service.salvar_viagem(dados_invalidos)
    
    if not resultado:
        print("✓ Validação funcionando: rejeita viagem sem nome")
    else:
        print("✗ Validação falhou: aceitou viagem sem nome")
        return False
    
    # Dados inválidos (sem data)
    dados_invalidos["nome"] = "João"
    dados_invalidos["data"] = ""
    resultado = viagem_service.salvar_viagem(dados_invalidos)
    
    if not resultado:
        print("✓ Validação funcionando: rejeita viagem sem data")
    else:
        print("✗ Validação falhou: aceitou viagem sem data")
        return False
    
    # Dados inválidos (sem destino)
    dados_invalidos["data"] = "2024-01-15"
    dados_invalidos["destino"] = ""
    resultado = viagem_service.salvar_viagem(dados_invalidos)
    
    if not resultado:
        print("✓ Validação funcionando: rejeita viagem sem destino")
        return True
    else:
        print("✗ Validação falhou: aceitou viagem sem destino")
        return False


def teste_excluir_viagem():
    """Teste 5: Excluir uma viagem"""
    print("\n" + "="*60)
    print("TESTE 5: EXCLUIR VIAGEM")
    print("="*60)
    
    config, temp_file = criar_config_teste()
    excel = ExcelService()
    viagem_service = ViagemService(excel)
    
    # Remove arquivo se existir
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Cria a planilha
    excel.criar_planilha(temp_file)
    
    # Salva uma viagem
    dados_viagem = {
        "nome": "João Silva",
        "data": "2024-01-15",
        "carro": "Toyota Corolla",
        "placa": "ABC-1234",
        "destino": "São Paulo",
        "km_saida": 100,
        "hora_saida": "08:00",
        "km_chegada": 250,
        "hora_chegada": "12:00"
    }
    
    viagem_service.salvar_viagem(dados_viagem)
    
    # Obtém o ID da viagem
    viagens = viagem_service.listar_viagens()
    if not viagens:
        print("✗ Falha: nenhuma viagem foi criada")
        return False
    
    id_viagem = viagens[0]["id"]
    
    # Exclui a viagem
    resultado = viagem_service.excluir_viagem(id_viagem)
    
    if resultado:
        viagens = viagem_service.listar_viagens()
        if len(viagens) == 0:
            print("✓ Viagem excluída com sucesso!")
            return True
        else:
            print("✗ Viagem ainda existe após exclusão")
            return False
    else:
        print("✗ Falha ao excluir viagem")
        return False


def teste_editar_viagem():
    """Teste 6: Editar uma viagem"""
    print("\n" + "="*60)
    print("TESTE 6: EDITAR VIAGEM")
    print("="*60)
    
    config, temp_file = criar_config_teste()
    excel = ExcelService()
    viagem_service = ViagemService(excel)
    
    # Remove arquivo se existir
    if os.path.exists(temp_file):
        os.remove(temp_file)
    
    # Cria a planilha
    excel.criar_planilha(temp_file)
    
    # Salva uma viagem
    dados_viagem = {
        "nome": "João Silva",
        "data": "2024-01-15",
        "carro": "Toyota Corolla",
        "placa": "ABC-1234",
        "destino": "São Paulo",
        "km_saida": 100,
        "hora_saida": "08:00",
        "km_chegada": 250,
        "hora_chegada": "12:00"
    }
    
    viagem_service.salvar_viagem(dados_viagem)
    
    # Obtém o ID da viagem
    viagens = viagem_service.listar_viagens()
    if not viagens:
        print("✗ Falha: nenhuma viagem foi criada")
        return False
    
    id_viagem = viagens[0]["id"]
    
    # Edita a viagem
    dados_editados = {
        "nome": "João Silva Editado",
        "data": "2024-01-20",
        "carro": "Honda Civic",
        "placa": "XYZ-5678",
        "destino": "Rio de Janeiro",
        "km_saida": 150,
        "hora_saida": "09:00",
        "km_chegada": 300,
        "hora_chegada": "13:00"
    }
    
    resultado = viagem_service.editar_viagem(id_viagem, dados_editados)
    
    if resultado:
        viagens = viagem_service.listar_viagens()
        viagem_editada = viagens[0]
        
        if (viagem_editada["nome"] == "João Silva Editado" and 
            viagem_editada["destino"] == "Rio de Janeiro" and
            viagem_editada["id"] == id_viagem):
            print("✓ Viagem editada com sucesso!")
            print(f"  ID permaneceu igual: {id_viagem}")
            print(f"  Nome: {viagem_editada['nome']}")
            print(f"  Destino: {viagem_editada['destino']}")
            return True
        else:
            print("✗ Dados não foram atualizados corretamente")
            return False
    else:
        print("✗ Falha ao editar viagem")
        return False


def executar_testes():
    """Executa todos os testes"""
    print("\n" + "="*60)
    print("INICIANDO TESTES DO SMARTFLEET AI")
    print("="*60)
    
    resultados = []
    
    # Executa cada teste
    resultados.append(("Criar Planilha", teste_criar_planilha()))
    resultados.append(("Salvar Viagem", teste_salvar_viagem()))
    resultados.append(("Listar Viagens", teste_listar_viagens()))
    resultados.append(("Validação", teste_validacao()))
    resultados.append(("Excluir Viagem", teste_excluir_viagem()))
    resultados.append(("Editar Viagem", teste_editar_viagem()))
    
    # Exibe relatório final
    print("\n" + "="*60)
    print("RELATÓRIO FINAL")
    print("="*60)
    
    passou = 0
    falhou = 0
    
    for teste, resultado in resultados:
        status = "✓ PASSOU" if resultado else "✗ FALHOU"
        print(f"{status}: {teste}")
        if resultado:
            passou += 1
        else:
            falhou += 1
    
    print(f"\nTotal: {passou} testes passaram, {falhou} testes falharam")
    
    if falhou == 0:
        print("\n🎉 TODOS OS TESTES PASSARAM! 🎉")
        return True
    else:
        print(f"\n❌ {falhou} TESTES FALHARAM")
        return False


if __name__ == "__main__":
    sucesso = executar_testes()
    sys.exit(0 if sucesso else 1)
