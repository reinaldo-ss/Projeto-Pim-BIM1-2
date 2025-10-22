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
    cpf = input("Digite o CPF do aluno: \n")
    endereco = input("Digite o endereço do aluno: \n")
    ra = input("Digite o Ra do Aluno: \n")
    curso = input("Digite o curso(s) do aluno: \n")

    novo_aluno = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone,
        "cpf": cpf,
        "endereco": endereco,
        "RA": ra,
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
        print(f"""{i}. 
    {aluno['nome']}: 
    {aluno['idade']} anos; 
    Curso: {aluno['curso']}; 
    Email: {aluno['email']};
    telefone: {aluno['telefone']};
    CPF: {aluno['cpf']};
    Endereco: {aluno['endereco']};
    RA: {aluno['RA']}""")
    print()

# Função que apaga um aluno cadastrado do JSON
def apagar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno encontrado")
        return
    raAluno = input("Digite o RA do aluno que deseja apagar: ")
    confirmacao = input("Tem certeza que deseja apagar o aluno selecionado?(s/n): ")

    if confirmacao == "s":
        lista_atualizada = [usuario for usuario in alunos if usuario["RA"] != raAluno]
        salvar_alunos(lista_atualizada)
        print(f"O aluno de RA: '{raAluno}' foi removido com sucesso.")
        return lista_atualizada
    elif confirmacao == "n":
        print("O processo de deletar usuário foi interrompido.")
    else:
        print(f"A resposta '{confirmacao}' é inválida, digite um valor válido para continuar")

def modificar_alunos(alunos):
    if not alunos:
        print("Nenhum aluno encontrado")
        return alunos
    
    ra_selecionado = input("Digite o RA desejado no campo a seguir: ")
    aluno_selecionado = None

    for aluno in alunos:
        if aluno.get("RA") == ra_selecionado:
            aluno_selecionado = aluno
            break

    if aluno_selecionado == None:
        print("Não foi encontrado um aluno com o RA digitado")
        return alunos
    
    print("Campos disponíveis: " + ", ".join(aluno_selecionado.keys()))

    chave_selecionada = input("Digite o nome EXATO da chave que você pretende modificar(ex: email): ")

    if chave_selecionada not in aluno_selecionado:
        print(f"\nErro: O campo '{chave_selecionada}' não existe no cadastro do aluno.\n")
        return alunos
        
    novo_valor = input(f"Digite o novo valor para '{chave_selecionada}': ")
    aluno_selecionado[chave_selecionada] = novo_valor

    print(f"'{chave_selecionada}' de '{aluno_selecionado['nome']}' atualizado com sucesso!")

    salvar_alunos(alunos)

    return alunos

# Função principal
def main():

    while True:
        print("--- Sistema de Cadastro de Alunos ---")
        print("1. Cadastrar novo aluno")
        print("2. Listar Alunos")
        print("3. Deletar Alunos")
        print("4. Editar Alunos")
        print("5. Sair\n")

        opcao = input("Escola uma opção: ")

        if opcao == "1":
            alunos = carregar_alunos()
        elif opcao == "2":
            listar_alunos(alunos)
        elif opcao == "3":
            alunos = apagar_alunos(alunos)
        elif opcao == "4":
            alunos = modificar_alunos(alunos)
        elif opcao == "5":
            print("encerrando programa...")
            break
        else:
            print("opção inválida, por favor, tente novamente.\n")

if __name__ == "__main__":
    main()

