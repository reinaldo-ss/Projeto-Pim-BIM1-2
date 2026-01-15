import json
import os

caminho_alunos = "./database/alunos.json"
caminho_professores = "./database/professores.json"
caminho_turmas = "./database/turmas.json"
caminho_atividades = "./database/atividades.json"
caminho_materiais = "./database/materiais.json"

# -- Funções Genéricas --

def limpaTela():
    os.system('cls')

def carregar_dados(caminho_arquivo):
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding = "utf-8") as f:
            return json.load(f)
    return []
        
def salvar_dados(caminho_arquivo, dados):
    with open(caminho_arquivo, "w", encoding = "utf-8") as f:
        json.dump(dados, f, indent=4)

def voltar_menu():
    voltar_menu = input("\nPressione 'Enter' para retornar ao Menu: ")
    limpaTela()
