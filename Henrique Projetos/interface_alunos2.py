import json
import os

# Importa JSON de alunos
file = "../cadastro_alunos/database/lista_alunos.json"

# Função que limpa tela do terminal
def limpaTela():
    os.system('cls')

# Função que baixa os dados do arquivo
def carregar_alunos():
    if os.path.exists(file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)

# Função que executa o login do aluno
def login_aluno(alunos):
    aluno = None

    print("Seja bem vindo a área de login de alunos! Por favor, insira seus dados abaixo:")
    while True:
        RA = input("Digite o seu RA:")
        for usuario in alunos: # Percorre toda a lista de alunos
            if RA == usuario.get("RA"): # Se o RA digitado estiver na lista
                aluno = usuario # Variável aluno recebe os dados referentes ao RA digitado
                break
            
        if aluno:
            senha_digitada = input("Digite a sua senha: ") # Pede a senha do cadastro

            if senha_digitada == aluno["senha"]: # Caso esteja correta
                return aluno # retorna os dados do aluno
            else:
                print(f"ERRO: A senha está incorreta, tente novamente") # Mensagem de erro caso a senha esteja incorreta
        else:
            print(f"ERRO: O RA inserido não existe") # Mensagem de erro caso o RA esteja incorreto
            break

# Função que consulta os dados do aluno logado
def consultar_dados(dados_aluno):
    print("Dados do login efetuado:\n")
    print(dados_aluno)
    voltar_menu = input("\n Clique 'Enter' para voltar ao menu ")
    limpaTela()
    return

# Função principal do sistema
def main():
    alunos = carregar_alunos()

    dados_aluno = login_aluno(alunos)

    limpaTela()
    print(f"Login Efetuado com Sucesso! Bem vindo(a) {dados_aluno['nome']}")

    # Interface inicial
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
            consultar_dados(dados_aluno)
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
