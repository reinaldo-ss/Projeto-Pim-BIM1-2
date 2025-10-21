import json
import os

file = "./database/lista_alunos.json"

# Função que carrega os dados existentes, caso o arquivo exista
def carregar_alunos():
    if os.path.exists(file):
        with open(file, "r", encoding = "utf-8") as f:
            return json.load(f)
    return []  # Se o arquivo não existir, é lançada uma lista vazia

# Função que salva os alunos no arquivo JSON
def salvar_alunos(alunos):
    with open(file, "w", encoding = "utf-8") as f:
        json.dump(alunos, f, indent=4)

# Função para cadastrar um aluno novo
def cadastrar_novo_aluno(alunos):
    nome = input("Digite o nome do aluno: \n")
    idade = input("Digite a idade do aluno: \n")
    email = input("Digite o email do aluno: \n")
    telefone = input("Digite o número de telefone do aluno: \n")
    curso = input("Digite o curso(s) do aluno: \n")

    novo_aluno = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone,
        "curso": curso
    }

    alunos.append(novo_aluno)
    salvar_alunos(alunos)
    print(f"\nAluno {nome} cadastrado com sucesso. \n")

# Função para listar os alunos cadastrados
def listar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno encontrado")
        return
    
    print("\nAlunos cadastrados:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['nome']} - {aluno['idade']} anos - Curso: {aluno['curso']}")
    print()

# Função principal
def main():
    alunos = carregar_alunos()

    while True:
        print("--- Sistema de Cadastro de Alunos ---")
        print("1. Cadastrar novo aluno")
        print("2. Listar Alunos")
        print("3. Sair\n")

        opcao = input("Escola uma opção: ")

        if opcao == "1":
            cadastrar_novo_aluno(alunos)
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            print("encerrando programa...")
            break
        else:
            print("opção inválida, por favor, tente novamente.\n")

if __name__ == "__main__":
    main()
