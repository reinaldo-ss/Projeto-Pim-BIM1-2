import json

caminho = "./data/database.json"

def Escolhas():
    print ("\nSistema para Gerenciar Dados!!\n")
    print ("Escolha uma das opcoes abaixo:\n")
    print ("(1) Ver Dados")
    print ("(2) Editar dados")
    print ("(3) Sair")

def verDados():
    with open (caminho, "r") as f:
        dados = json.load(f)
        for entrada in dados:
            name = entrada["name"]
            profissao = entrada["profissao"]
            materia = entrada["materia"]

            print (f"Nome:  {name}")
            print (f"Profissao:  {profissao}")
            print (f"Materia:  {materia}")
            print ("\n\n")

def addDados():
    item_dados = {}
    with open (caminho, "r") as f:
        dados = json.load(f)
    item_dados["name"] = input("Digite seu nome: ")
    item_dados["profissao"] = input("Digite a sua profissao: ")
    item_dados["materia"] = input("Digite a sua disciplina")
    dados.append(item_dados)
    with open (caminho, "w") as f:
        json.dump(dados, f, indent=4)

while True:
    Escolhas()
    escolha = input("\nEscolha uma das opções: ")

    if escolha == "1":
        verDados()

    elif escolha == "2":
        addDados()

    elif escolha == "3":
        break

    else:
        print ("Escolha uma opção valida para poder continuar.")    
