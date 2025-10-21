import json
import os
import re

caminho = "./data/database.json"

# Função que tira os dados anteriores, pra não ficar poluido a tela
def limpaTela():
    os.system('cls')

# Função para validar se o CPF existe e se possui letras ou caracter especial
def validar_cpf(cpf):
    cpf = re.sub(r'[^0-9]', '', cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[num]) * ((i + 1) - num) for num in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True

# Função para exibir os dados
def verDados():
    with open (caminho, "r") as f:
        dados = json.load(f)
        temp = dados["professores"]
        print ("\nProfessores Cadastrados\n")
        for entrada in temp:
            name = entrada["name"]
            cpf = entrada["cpf"]
            numTelefone = entrada["numTelefone"]
            curso = entrada["curso"]
            turma = entrada["turma"]
            materia = entrada["materia"]
            email = entrada["email"]

            print (f"Nome: {name}")
            print (f"CPF: {cpf}")
            print (f"Numero de Telefone: {numTelefone}")
            print (f"Curso: {curso}")
            print (f"Turma: {turma}")
            print (f"Materia: {materia}")
            print (f"Email: {email}")
            print ("----------------------------------------")

# Função para cadastrar professor.        
def addDados():
    item_dados = {}
    with open(caminho, "r") as f:
        dados = json.load(f)
        temp = dados["professores"]

        item_dados["name"] = input("Digite seu nome: ")

        # Laço de CPF com validador para ver se o CPF é real
        while True:
            cpf = input("Digite seu CPF com 11 dígitos (apenas números): ").strip()
            if validar_cpf(cpf):
                item_dados["cpf"] = cpf
                break
            else:
                print("CPF inválido. Tente novamente.")
    
        item_dados["numTelefone"] = int(input("Digite seu numero de telefone com DDD: "))        
        item_dados["curso"] = input("Digite o nome do curso: ")
        item_dados["turma"] = input("Digite o numero da turma: ")
        item_dados["materia"] = input("Digite a sua materia: ")
        item_dados["email"] = input("Digite seu email: ")
        temp.append(item_dados)

    with open(caminho, "w") as f:
        json.dump(dados, f, indent=4)

#Função principal de Escolhas existentes no programa

def Escolhas():
    print ("\nSistema para Gerenciar Dados!!\n")
    print ("Escolha uma das opcoes abaixo:\n")
    print ("(1) Ver Dados")
    print ("(2) Adicionar dados")
    print ("(3) Sair")

# Laço de repetição das escolhas que o usuario fizer.
while True:
    Escolhas()
    escolha = input("\nEscolha uma das opções: ")

    if escolha == "1":
        verDados()
        input("Pressione Enter para voltar ao menu inicial...")
        limpaTela()
    elif escolha == "2":
        limpaTela()
        print ("Vamos cadastrar o professor!\n")

        addDados()

        print("Seu cadastro foi feito com sucesso, digite 1 no menu principal se quiser ver os professores cadastrados!\n")
        input("Pressione Enter para voltar ao menu inicial...")
        limpaTela()
    elif escolha == "3":
        break

    else:
        print ("Escolha uma opção valida para poder continuar.")    
