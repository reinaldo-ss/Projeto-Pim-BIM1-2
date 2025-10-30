import utils
import random
import string
import re

# Função que valida o CPF
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

# Função que valida o nome
def validar_nome(entrada):
    maximo_letras = 25
    minimo_letras = 3

    if entrada.isalpha():
        if minimo_letras <= len(entrada) <= maximo_letras:
            return True, ""
        elif len(entrada) < minimo_letras:
            return False, "ERRO: O nome precisa ter no mínimo 3 letras"
        elif len(entrada) > maximo_letras:
            return False, "ERRO: O nome precisa ter no máximo 25 letras"
    else:
        return False, "ERRO: O nome deve conter apenas letras."

# Função que valida o email
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

# Função que valida a senha
def validar_senha(entrada):
    tamanho = len(entrada)

    maximo_caracteres = 30
    minimo_caracteres = 8
    caracteres_especiais = {"@", "#", "$", "%", "&"}

    if tamanho < minimo_caracteres:
        return False, f"ERRO: O mínimo de caracteres aceitos é de '{minimo_caracteres}' caracteres"

    if tamanho > maximo_caracteres:
        return False, f"ERRO: O máximo de caracteres aceitos é de '{maximo_caracteres}' caracteres"

    if not any(char in entrada for char in caracteres_especiais):
        return False, f"ERRO: A senha deve ter no mínimo UM dos caracteres listados a seguir: '{caracteres_especiais}'"

    return True, ""

# Função que valida o telefone
def validar_telefone(entrada):
    tamanho = len(entrada)

    valor_minimo = 10
    valor_maximo = 13

    if tamanho < valor_minimo or tamanho > valor_maximo :
        return False, f"ERRO: O número digitado deve estar entre {valor_minimo} e {valor_maximo} digitos"
    
    return True, ""

# Função de validação geral, que utiliza validações parciais
def validacao_geral(pergunta, funcao_validacao):
    dados_validados = False

    while not dados_validados:
        entrada_usuario = input(pergunta + " ")
        
        dados_validados, mensagem_erro = funcao_validacao(entrada_usuario)

        if not dados_validados and mensagem_erro:
            print(f"{mensagem_erro}")

    return entrada_usuario

# Função que verifica se um dado é repetido ou não
def obter_dado_valido_e_unico(pergunta, funcao_validacao, lista_dados, chave):
    while True:
        entrada_usuario = validacao_geral(pergunta, funcao_validacao)

        dado_existe = any(item.get(chave) == entrada_usuario for item in lista_dados)

        if not dado_existe:
            return entrada_usuario 
        else:
            print(f"ERRO: O {chave} '{entrada_usuario}' já está cadastrado.")

# --- INICIO CRUD ALUNOS ---

def cadastrar_novo_aluno():
    utils.limpaTela()
    alunos = utils.carregar_dados(utils.caminho_alunos)
    turmas = utils.carregar_dados(utils.caminho_turmas)

    #gerando RA aleatório
    letras_possiveis = random.choices(string.ascii_uppercase, k=5)
    numeros_possiveis = random.choices(string.digits, k=2)

    caracteres_unidos = letras_possiveis + numeros_possiveis
    random.shuffle(caracteres_unidos)
    ra_final = "".join(caracteres_unidos)

    prosseguir = input("Você selecionou a opção 'cadastrar novo aluno'. Se deseja continuar, digite '1'. Se deseja voltar ao menu, digite '0': ")
    if prosseguir == "0":
        utils.voltar_menu()
        return alunos
    
    # Perguntas sobre os dados a serem inseridos, e suas devidas validações
    nome = validacao_geral("Digite o nome do Aluno:", validar_nome)
    sobrenome = validacao_geral("Digite o sobrenome do Aluno:", validar_nome)
    email = obter_dado_valido_e_unico("Digite o email do Aluno:", validar_email, alunos, "email")
    senha = validacao_geral("Digite a senha do Aluno: ", validar_senha)
    telefone = obter_dado_valido_e_unico("Digite o telefone do Aluno: ", validar_telefone, alunos, "telefone")
    cpf = obter_dado_valido_e_unico("Digite o CPF do aluno:", validar_cpf, alunos, "cpf")

    print("\n--- Turmas Disponíveis ---")
    for turma in turmas:
        print(f"Código: {turma['codTurma']} - Curso: {turma['curso']}")

    codigos_de_turma_validos = [turma['codTurma'] for turma in turmas] # Cria uma lista só com os códigos
    
    while True:
        codTurma = input("\nDigite o código da turma do aluno: ")
        if codTurma in codigos_de_turma_validos:
            break
        else:
            print("ERRO: O código de turma inserido não existe.")

    novo_aluno = {
        "nome": nome,
        "sobrenome": sobrenome,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "cpf": cpf,
        "RA": ra_final,
        "codTurma": codTurma,
        "nota": 0.0
    }

    alunos.append(novo_aluno)
    utils.salvar_dados(utils.caminho_alunos, alunos)
    print(f"\n Aluno {nome} {sobrenome} (RA: {ra_final} cadastrado com sucesso.")
    utils.voltar_menu()
    return alunos

def listar_alunos():
    utils.limpaTela()
    alunos = utils.carregar_dados(utils.caminho_alunos)

    print("--- Alunos Cadastrados ---")
    if not alunos:
        print("ERRO: Nenhum aluno encontrado\n")
        utils.voltar_menu()
        return alunos
    
    print("\n Alunos Cadastrados: ")
    for aluno in alunos:
        print("-" * 20)
        print(f"Nome: {aluno['nome']} {aluno['sobrenome']}")
        print(f"RA: {aluno['RA']}")
        print(f"Email: {aluno['email']}")
        print(f"Turma: {aluno['codTurma']}")
        print(f"Nota: {aluno['nota']}")
    utils.voltar_menu()
    return alunos

def modificar_alunos():
    utils.limpaTela()
    alunos = utils.carregar_dados(utils.caminho_alunos)

    if not alunos:
        print("ERRO: Nenhum aluno encontrado\n")
        utils.voltar_menu()
        return alunos
    
    print("--- Lista de alunos cadastrados ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['nome']} {aluno['sobrenome']} | RA: {aluno['RA']}")

    ra_selecionado = input("\nDigite o RA desejado no campo a seguir(Digite 'cancelar' se quiser voltar ao Menu): ")
    if ra_selecionado == "cancelar":
        return alunos
    aluno_selecionado = None

    for aluno in alunos:
        if aluno.get("RA") == ra_selecionado:
            aluno_selecionado = aluno
            break

    if aluno_selecionado == None:
        utils.limpaTela()
        print("Não foi encontrado um aluno com o RA digitado")
        utils.voltar_menu()
        return alunos
    
    print("\nCampos disponíveis: " + ", ".join(aluno_selecionado.keys())) # Mostra todas as chaves disponíveis

    chave_selecionada = input("\nDigite o nome EXATO da chave que você pretende modificar(ex: email): ")

    if chave_selecionada not in aluno_selecionado: # Se chave digitada não existir
        print(f"\nErro: O campo '{chave_selecionada}' não existe no cadastro do aluno.\n")
        return alunos
        
    novo_valor = input(f"\nDigite o novo valor para '{chave_selecionada}': ")
    aluno_selecionado[chave_selecionada] = novo_valor

    utils.limpaTela()
    print(f"'{chave_selecionada}' de '{aluno_selecionado['nome']}' atualizado com sucesso!")
    utils.voltar_menu()

    utils.salvar_dados(utils.caminho_alunos, alunos)

    return alunos

def apagar_alunos():
    utils.limpaTela()
    alunos = utils.carregar_dados(utils.caminho_alunos)
    
    if not alunos:
        print("ERRO: Nenhum aluno encontrado\n")
        utils.voltar_menu()
        return alunos
    
    print("--- Lista de alunos cadastrados ---")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}. {aluno['nome']} {aluno['sobrenome']} | RA: {aluno['RA']}")

    raAluno = input("\nDigite o RA desejado no campo a seguir(Digite 'cancelar' se quiser voltar ao Menu): ")
    if raAluno == "cancelar":
        return alunos
    confirmacao = input("Tem certeza que deseja apagar o aluno selecionado?(s/n): ")

    if confirmacao == "s":
        lista_atualizada = [usuario for usuario in alunos if usuario["RA"] != raAluno]
        utils.salvar_dados(utils.caminho_alunos, lista_atualizada)
        utils.limpaTela()
        print(f"O aluno de RA: '{raAluno}' foi removido com sucesso.")
        utils.voltar_menu()
        return lista_atualizada
    
    elif confirmacao == "n":
        utils.limpaTela()
        print("O processo de deletar usuário foi interrompido.")
        utils.voltar_menu()
        return alunos
    else:
        print(f"A resposta '{confirmacao}' é inválida, digite um valor válido para continuar")

# --- SEÇÃO DE GERENCIAMENTO DE PROFESSORES ---

def cadastrar_novo_professor():
    #gerando RA aleatório
    letras_possiveis = random.choices(string.ascii_uppercase, k=5)
    numeros_possiveis = random.choices(string.digits, k=3)

    caracteres_unidos = letras_possiveis + numeros_possiveis
    random.shuffle(caracteres_unidos)
    rp_final = "".join(caracteres_unidos)

    utils.limpaTela()
    professores = utils.carregar_dados(utils.caminho_professores)

    prosseguir = input("Você selecionou a opção 'cadastrar novo professor'. Se deseja continuar, digite '1'. Se deseja voltar ao menu, digite '0': ")
    if prosseguir == "0":
        utils.voltar_menu()
        return professores
    
    nome = validacao_geral("Digite o nome do Professor:", validar_nome)
    sobrenome = validacao_geral("Digite o sobrenome do Professor:", validar_nome)
    cpf = obter_dado_valido_e_unico("Digite o CPF do Professor:", validar_cpf, professores, "cpf")
    email = obter_dado_valido_e_unico("Digite o email do Professor:", validar_email, professores, "email")
    senha = validacao_geral("Digite a senha do Professor:", validar_senha)
    telefone = obter_dado_valido_e_unico("Digite o telefone do Professor: ", validar_telefone, professores, "telefone")

    novo_professor = {
        "nome": nome,
        "sobrenome": sobrenome,
        "cpf": cpf,
        "email": email,
        "senha": senha,
        "telefone": telefone,
        "RP": rp_final
    }

    professores.append(novo_professor)
    utils.salvar_dados(utils.caminho_professores, professores)
    print(f"\n Professor {nome} {sobrenome} (RP: {rp_final} cadastrado com sucesso. \n")
    input("\nPressione 'Enter' para retornar ao menu.")
    return professores

def listar_professores():
    utils.limpaTela()
    professores = utils.carregar_dados(utils.caminho_professores)

    print("--- Professores Cadastrados ---")
    if not professores:
        print("ERRO: Nenhum professor encontrado\n")
        utils.voltar_menu()
        return professores
    
    print("\n Professores Cadastrados: ")
    for professor in professores:
        print("-" * 20)
        print(f"Nome: {professor['nome']} {professor.get('sobrenome')}")
        print(f"RP: {professor['RP']}")
        print(f"Email: {professor['email']}")
        print(f"Senha: {professor['senha']}")
        print(f"CPF: {professor['cpf']}")
        print(f"Telefone: {professor['telefone']}")
    utils.voltar_menu()
    return professores

def modificar_professores():
    utils.limpaTela()
    professores = utils.carregar_dados(utils.caminho_professores)

    if not professores:
        print("ERRO: Nenhum professor encontrado\n")
        utils.voltar_menu()
        return professores
    
    print("--- Lista de professores cadastrados ---")
    for i, professor in enumerate(professores, start=1):
        print(f"{i}. {professor['nome']} {professor['sobrenome']} | RP: {professor['RP']}")

    rp_selecionado = input("\nDigite o RP desejado no campo a seguir(Digite 'cancelar' se quiser voltar ao Menu): ")
    if rp_selecionado == "cancelar":
        return professores
    professor_selecionado = None

    for professor in professores:
        if professor.get("RP") == rp_selecionado:
            professor_selecionado = professor
            break

    if professor_selecionado == None:
        utils.limpaTela()
        print("Não foi encontrado um professor com o RP digitado")
        utils.voltar_menu()
        return professores
    
    print("\nCampos disponíveis: " + ", ".join(professor_selecionado.keys())) # Mostra todas as chaves disponíveis

    chave_selecionada = input("\nDigite o nome EXATO da chave que você pretende modificar(ex: email): ")

    if chave_selecionada not in professor_selecionado: # Se chave digitada não existir
        print(f"\nErro: O campo '{chave_selecionada}' não existe no cadastro do professor.\n")
        return professores
        
    novo_valor = input(f"\nDigite o novo valor para '{chave_selecionada}': ")
    professor_selecionado[chave_selecionada] = novo_valor

    utils.limpaTela()
    print(f"'{chave_selecionada}' de '{professor_selecionado['nome']}' atualizado com sucesso!")
    utils.voltar_menu()

    utils.salvar_dados(utils.caminho_professores, professores)

    return professores

def apagar_professores():
    utils.limpaTela()
    professores = utils.carregar_dados(utils.caminho_professores)
    
    if not professores:
        print("ERRO: Nenhum professor encontrado\n")
        utils.voltar_menu()
        return professores
    
    print("--- Lista de professores cadastrados ---")
    for i, professor in enumerate(professores, start=1):
         print(f"{i}. {professor['nome']} {professor['sobrenome']} | RP: {professor['RP']}")

    rpProfessor = input("\nDigite o RP desejado no campo a seguir(Digite 'cancelar' se quiser voltar ao Menu): ")
    if rpProfessor == "cancelar":
        return professores
    confirmacao = input("Tem certeza que deseja apagar o professor selecionado?(s/n): ")

    if confirmacao == "s":
        lista_atualizada = [usuario for usuario in professores if usuario["RP"] != rpProfessor]
        utils.salvar_dados(utils.caminho_professores, lista_atualizada)
        utils.limpaTela()
        print(f"O professor de RP: '{rpProfessor}' foi removido com sucesso.")
        utils.voltar_menu()
        return lista_atualizada
    
    elif confirmacao == "n":
        utils.limpaTela()
        print("O processo de deletar usuário foi interrompido.")
        utils.voltar_menu()
        return professores
    else:
        print(f"A resposta '{confirmacao}' é inválida, digite um valor válido para continuar")

# --- MENUS DE GERENCIAMENTO ---

def menu_gerenciar_alunos():
    while True:
        utils.limpaTela()
        print("--- Gerenciar ALunos ---")
        print("1. Cadastrar Novo Aluno")
        print("2. Listar Alunos")
        print("3. Editar Alunos")
        print("4. Deletar Alunos")
        print("5. Voltar ao Menu Principal")
        
        opcao = input("\n Escolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_aluno()
        elif opcao == "2":
            listar_alunos()
        elif opcao == "3":
            modificar_alunos()
        elif opcao == "4":
            apagar_alunos()
        elif opcao == "5":
            break
        else:
            utils.limpaTela()
            print(f"\nO valor '{opcao}' é inválido. Clique 'Enter' para tentar novamente.\n")

def menu_gerenciar_professores():
    while True:
        utils.limpaTela()
        print("--- Gerenciar Professores ---")
        print("1. Cadastrar Novo Professor")
        print("2. Listar Professores")
        print("3. Editar Professores")
        print("4. Deletar Professores")
        print("5. Voltar ao Menu Principal")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_novo_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            modificar_professores()
        elif opcao == "4":
            apagar_professores()
        elif opcao == "5":
            break
        else:
            utils.limpaTela()
            print(f"\nO valor '{opcao}' é inválido. Clique 'Enter' para tentar novamente.\n")

def iniciar_menu():
    while True:
        utils.limpaTela()
        print("--- Painel do Administrador ---")
        print("1. Gerenciar ALunos")
        print("2. Gerenciar Professores")
        print("3. Voltar ao Menu Inicial")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            menu_gerenciar_alunos()
        elif opcao == "2":
            menu_gerenciar_professores()
        elif opcao == "3":
            return
        else:
            utils.limpaTela()
            print(f"\nO valor '{opcao}' é inválido. Clique 'Enter' para tentar novamente.\n")


if __name__ == "__main__":
    iniciar_menu()
