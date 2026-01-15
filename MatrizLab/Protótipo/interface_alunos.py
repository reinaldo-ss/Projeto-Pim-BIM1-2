import utils
import chatbot

def login_aluno(alunos):
    aluno = None

    print("Seja bem vindo a área de login de alunos! Por favor, insira seus dados abaixo:")
    while True:
        Ra = input("Digite o seu RA:")
        for usuario in alunos: # Percorre toda a lista de alunos
            if Ra == usuario.get("RA"): # Se o RA digitado estiver na lista
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

def aluno_aprovado(nota):
    nota_minima = 6
    if nota >= nota_minima:
        return "Aprovado"
    else:
        return "Reprovado"
    
def consultar_notas(dados_aluno):
    utils.limpaTela()
    situacao_atual = aluno_aprovado(dados_aluno['nota'])
    print("==== Sua nota atual ====")
    
    print(f"{dados_aluno.get('nota')}, situação atual: {situacao_atual}")

# Função que consulta os dados do aluno logado
def consultar_dados(dados_aluno):
    utils.limpaTela()
    print("==== Dados do login efetuado ====\n")
    print(f"Nome Completo: {dados_aluno.get('nome')} {dados_aluno.get('sobrenome')}")
    print(f"RA: {dados_aluno.get('RA')}")
    print(f"Email: {dados_aluno.get('email')}")
    print(f"Código da Turma: {dados_aluno.get('codTurma')}")
    
    utils.voltar_menu()
    utils.limpaTela()
    return

def consultar_materiais(dados_aluno):
    utils.limpaTela()
    print(f"==== Materiais da Turma de {dados_aluno['codTurma']} ====")

    todos_materiais = utils.carregar_dados(utils.caminho_materiais)

    materiais_turma = [m for m in todos_materiais if m.get('codTurma') == dados_aluno['codTurma']]

    if not materiais_turma:
        print("\n Nenhum material de aula encontrado para a sua turma.")
        utils.voltar_menu()
    else:
        for material in materiais_turma:
            print("="*20)
            print(f"Título: {material.get('titulo')}")
            print(f"Professor: {material.get('nomeProfessor')}")
            print(f"Link: {material.get('link')}")
            print(f"Descrição: {material.get('descricao')}")

    utils.voltar_menu()

def consultar_atividades(dados_aluno):
    utils.limpaTela()
    print(f"==== Atividades da Turma {dados_aluno['codTurma']} ====")

    todas_atividades = utils.carregar_dados(utils.caminho_atividades)

    atividades_turma = [m for m in todas_atividades if m.get('codTurma') == dados_aluno['codTurma']]

    if not atividades_turma:
        print("\n Nenhuma atividade encontrada para a sua turma.")
        utils.voltar_menu()
    else:
        for atividade in atividades_turma:
            print("-"*20)
            print(f"Título: {atividade.get('titulo')}")
            print(f"Professor: {atividade.get('nomeProfessor')}")
            print(f"Link: {atividade.get('link')}")
            print(f"Descrição: {atividade.get('descricao')}")

    utils.voltar_menu()

# Função principal do sistema
def menu_alunos(dados_aluno):

    utils.limpaTela()
    print(f"Login Efetuado com Sucesso! Bem vindo(a) {dados_aluno['nome']}")

    # Interface inicial
    while True:
        print("\n---Sistema MatrizLab---\n")
        print("1. Consultar Notas")
        print("2. Consultar Dados")
        print("3. Consultar Atividades")
        print("4. Consultar Material")
        print("5. Voltar ao Menu Anterior")

        opcao = input("\nEscolha uma opção acima: ")

        if opcao == "1":
            consultar_notas(dados_aluno)
        elif opcao == "2":
            consultar_dados(dados_aluno)
        elif opcao == "3":
            consultar_atividades(dados_aluno)
        elif opcao == "4":
            consultar_materiais(dados_aluno)
        elif opcao == "5":
            break
        else:
            print(f"ERRO: A opção '{opcao}' é inválida, por favor tente novamente")
        
def iniciar_menu():
    alunos = utils.carregar_dados(utils.caminho_alunos)
    dados_aluno = login_aluno(alunos)
    if dados_aluno:
        menu_alunos(dados_aluno)
