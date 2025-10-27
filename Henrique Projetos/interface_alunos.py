import json
import os

file = "../cadastro_alunos/database/lista_alunos.json"

def limpaTela():
    os.system('cls')

def carregar_alunos():
    if os.path.exists(file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)
        
def login_aluno(alunos):
    aluno = None

    print("Seja bem vindo a área de login de alunos! Por favor, insira seus dados abaixo:")
    while True:
        RA = input("Digite o seu RA:")
        for usuario in alunos:
            if RA == usuario.get("RA"):
                aluno = usuario
                
            if aluno:
                senha_digitada = input("Digite a sua senha: ")

                if senha_digitada == aluno["senha"]:
                    return aluno
                else:
                    print(f"ERRO: A senha está incorreta, tente novamente")
            else:
                print(f"ERRO: O RA inserido não existe")
                break

def main():
    alunos = carregar_alunos()

    dados_aluno = login_aluno(alunos)

    limpaTela()
    print(f"Login Efetuado com Sucesso! Bem vindo(a) {dados_aluno['nome']}")

    while True:
        print("\n---Sistema MatrizLab---\n")
        print("1. Consultar Notas")
        print("2. Consultar Dados")
        print("3. Consultar Atividades")
        print("4. Consultar Material")

        opcao = input("\nEscolha uma opção acima: ")

        if opcao == "1":
            limpaTela()
            ""
        elif opcao == "2":
            limpaTela()
            print("Dados do login efetuado:\n")
            print(dados_aluno)
        elif opcao == "3":
            limpaTela()
            ""
        elif opcao == "4":
            limpaTela()
            ""
        else:
            print(f"ERRO: A opção '{opcao}' é inválida, por favor tente novamente")
        
if __name__ == "__main__":
    main()
