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

#--------------------------------------------------
def validar_cpf(entrada):
    numero_digitos = 11

    if len(entrada) == numero_digitos:
        return True, ""
    elif entrada.isalpha():
        return False, "ERRO: O CPF só deve conter números inteiros"
    elif len(entrada) < numero_digitos or len(entrada) > numero_digitos:
        return False, "ERRO: O CPF deve conter 11 dígitos"
    else:
        return False, "ERRO: O valor inserido é inválido"
    
def validar_idade(entrada):
    if entrada.isdigit():
        idade = int(entrada)
        if 18 <= idade <= 105:
            return True, ""
        else:
            return False, "ERRO: A idade deve estar entre 18 e 100 anos."
    else:
        return False, "ERRO: A idade deve ser um número inteiro."

def validar_nome(entrada):
    if entrada.isalpha():
        if 3 <= len(entrada) <= 50:
            return True, ""
        else:
            return False, "ERRO: O nome precisa ter no mínimo 3 letras"
    else:
        return False, "ERRO: O nome deve conter apenas letras."
    
def validar_email(entrada):
        entrada_limpa = entrada.strip()

        if " " in entrada_limpa:
            return False, "ERRO: o email não pode conter espaços vazios"
        
        if "@" not in entrada_limpa:
            return False, "ERRO: O email precisa conter um '@'"
        
        if "." not in entrada_limpa:
            return False, "ERRO: o email precisa conter um '.' "
        
        if entrada_limpa.count("@") > 1:
            return False, "ERRO: O email não pode conter mais de um '@' "
        
        if entrada_limpa.index("@") == 0 or entrada_limpa.endswith("."):
            return False, "ERRO: Verifique as posições dos caracteres '@' e '.' "
        
        if entrada_limpa.find(".") < entrada_limpa.find("@"):
            return False, "ERRO: Verifique a posição do caracter '.' "
        
        return True, ""

def validar_telefone(entrada):
        tamanho = len(entrada)

        valor_minimo = 10
        valor_maximo = 13

        if tamanho < valor_minimo or tamanho > valor_maximo :
            return False, f"ERRO: O número digitado deve estar entre {valor_minimo} e {valor_maximo} digitos"
        
        return True, ""
        
def validacao_geral(pergunta, funcao_validacao):
    dados_validados = False

    while not dados_validados:
        entrada_usuario = input(pergunta + " ")
        
        dados_validados, mensagem_erro = funcao_validacao(entrada_usuario)

        if not dados_validados and mensagem_erro:
            print(f"{mensagem_erro}")

    return entrada_usuario
    
# Função para cadastrar um aluno novo
def cadastrar_novo_aluno(alunos):
    nome = validacao_geral("Digite o nome do Aluno:", validar_nome)
    idade = validacao_geral("Digite a idade do Aluno:", validar_idade)
    email = validacao_geral("Digite o email do Aluno:", validar_email)
    telefone = validacao_geral("Digite o telefone do Aluno: ", validar_telefone)
    cpf = validacao_geral("Digite o CPF do aluno:", validar_cpf)
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


def limpaTela():
    os.system('cls')

# Função principal
def main():
    alunos = carregar_alunos()

    while True:
        print("--- Sistema de Cadastro de Alunos ---")
        print("1. Cadastrar novo aluno")
        print("2. Listar Alunos")
        print("3. Deletar Alunos")
        print("4. Editar Alunos")
        print("5. Sair\n")

        opcao = input("Escola uma opção: ")

        if opcao == "1":
            limpaTela()
            alunos = cadastrar_novo_aluno(alunos)
        elif opcao == "2":
            limpaTela()
            listar_alunos(alunos)
        elif opcao == "3":
            limpaTela()
            alunos = apagar_alunos(alunos)
        elif opcao == "4":
            limpaTela()
            alunos = modificar_alunos(alunos)
        elif opcao == "5":
            limpaTela()
            print("encerrando programa...")
            break
        else:
            print("opção inválida, por favor, tente novamente.\n")

if __name__ == "__main__":
    main()
