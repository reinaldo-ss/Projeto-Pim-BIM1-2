import json
import os

from urllib.parse import urlparse

# Diretório base (onde o script atual está salvo)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos absolutos baseados na localização do script
caminhoAlunos = os.path.join(base_dir, "alunos", "alunos.json")
caminhoAtividade = os.path.join(base_dir, "atividade", "atividade.json")
caminhoMaterial = os.path.join(base_dir, "material", "material.json")
caminhoProfessor = os.path.join(base_dir, "professor", "dadosProfessor.json")
caminhoTurmas = os.path.join(base_dir, "turmas", "turmas.json")

# Função que tira os dados anteriores, pra não ficar poluido a tela
def limpaTela():
    os.system("cls")

# Carregamento de arquivos JSON:
def carregar_alunos():
    # Esta função carrega os dados do arquivo .json.
    try:
        with open(caminhoAlunos, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'alunos.json' não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo 'alunos.json' está mal formatado.")
        return []

def carregar_atividade():
    try:
        with open(caminhoAtividade, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'usuarios.json' não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo 'usuarios.json' está mal formatado.")
        return []
    
def carregar_material():
    try:
        with open(caminhoMaterial, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'usuarios.json' não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo 'usuarios.json' está mal formatado.")
        return []
    
def carregar_professores():
    try:
        with open(caminhoProfessor, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'professor.json' não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo 'professor.json' está mal formatado.")
        return []
    
def carregar_turmas():
    try:
        with open(caminhoTurmas, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Arquivo 'usuarios.json' não encontrado!")
        return []
    except json.JSONDecodeError:
        print("Erro: O arquivo 'usuarios.json' está mal formatado.")
        return []
# ------- Fim carregamento JSON -------

# Salvar material
def salvarMaterial(material):
    with open(caminhoMaterial, 'w', encoding='utf-8') as f:
        json.dump(material, f, indent=4)

# Salvar atividades
def salvarAtividades(atividades):
    with open(caminhoAtividade, 'w', encoding='utf-8') as f:
        json.dump(atividades, f, indent=4)

# Salvar Alunos
def salvar_alunos(alunos):
    with open(caminhoAlunos, 'w', encoding='utf-8') as f:
        json.dump(alunos, f, indent=4)

# --------- Validando dados para cadastrar Atividade e Material ---------

# Validando codigo turma
def validar_turma(codigoTurma):
    dadosTurma = carregar_turmas()

    for codTurma in dadosTurma:
        if codTurma['codTurma'] == codigoTurma:
            return codigoTurma
        
# Validando titulo
def validar_titulo(titulo):
    if len(titulo) < 5:
        return False
    return True

# Validando disciplina
def validar_disciplina(disciplina):
    if len(disciplina) < 5:
        return False
    return True

# Validando link
def validar_link(link):
    """
    Esta função verifica se uma string (texto) fornecida tem a estrutura de uma URL válida.
    Ela usa a biblioteca 'urllib' para analisar a estrutura do link.

    Parâmetros:
    - link (str): O texto que você quer validar.

    Retorna:
    - True: se o texto for uma URL válida.
    - False: se o texto não for uma URL válida.
    """
    # Usamos um bloco try...except por segurança, para o caso de entradas muito inesperadas.
    try:
        # Tentamos "desmontar" o link em suas partes
        resultado = urlparse(link)
        
        # Verificamos se as duas partes essenciais (scheme e netloc) existem
        # A função all() retorna True somente se todos os itens na lista forem verdadeiros.
        # Strings vazias são consideradas 'False', então se 'scheme' ou 'netloc' não existirem,
        # o resultado será False.
        return all([resultado.scheme, resultado.netloc])
            
    except:
        # Se qualquer erro inesperado acontecer durante a análise, retorna False.
        return False
# ------- Fim das validações  -------

# Validar nota Aluno
def validar_nota(nota_str):
   
    # Valida se a string fornecida é uma nota válida (um número entre 0 a 10).
    # Retorna True se for válida, False caso contrário.
    
    try:
        # Tenta converter a string para um número float
        nota = float(nota_str)
        # Verifica se o número está no intervalo de 0 a 10
        if 0 <= nota <= 10:
            return True
        else:
            return False
    except ValueError:
        # Se a conversão para float falhar (ex: o usuário digitou "abc"), retorna False
        return False
# ------- Fim da validação nota aluno -------

# Efetuando login do professor
def fazer_login():
    """
    Esta função agora retorna os dados do professor se o login for bem-sucedido,
    ou retorna None se falhar.
    """
    limpaTela()
    print("====== Tela de Login ====== \n")
    professor_digitado = input("Digite seu RP: ")
    senha_digitada = input("Digite sua senha: ")

    professores = carregar_professores()

    # Procura pelo usuário na lista
    for professor in professores:
        if professor['rP'] == professor_digitado and professor['senha'] == senha_digitada:
            limpaTela()
            return professor # Retorna o dicionário completo do usuário

    # Se o loop terminar e não encontrar, retorna None
    input("\nNome de usuário ou senha incorretos.\nPressione enter para voltar ao menu anterior e tentar novamente...")
    limpaTela()
    return None
# ------- Fim do fazer login  -------

# Exibir os dados do usuario logado
def verMeusDados(professor):
    """
    Esta função recebe os dados do usuário como um parâmetro.
    Isso a torna mais independente e fácil de testar.
    """
    limpaTela()
    print("====== Meus Dados ======\n")
    print(f"Nome: {professor['name']}")
    print(f"CPF: {professor['cpf']}")
    print(f"E-mail: {professor['email']}")
    print(f"Telefone: {professor['numTelefone']}")
    print(f"RP(Registro do Professor): {professor['rP']}\n")
    print("======================================================\n")
    
    input("Pressione enter para voltar ao menu anterior...")
    limpaTela()

# Menu dos materiais: criar, alterar, deletar e visualizar
def menuMaterial(professor): 

    limpaTela()
    while True:
        print("====== Menu Material ======\n")
        print("1. Criar material")
        print("2. Ver materiais")
        print("3. Alterar material")
        print("4. Deletar material")
        print("5. Retornar a página anterior\n")
        print("======================================================\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criarMaterial(professor)
        elif escolha == "2":
            verMateriais(professor)
        elif escolha == "3":
            alterarMaterial(professor)
        elif escolha == "4":
            deletarMaterial(professor)
        elif escolha == "5":
            limpaTela()
            return
        else:
            input("\nOpção inválida. Pressione enter para tentar novamente...")
            limpaTela()

# Criando material
def criarMaterial(professor):

    item_dados = {}
    material = carregar_material()
    todas_as_turmas = carregar_turmas()

    limpaTela()
    # Mostrando turmas disponiveis
    print("====== Cadastrar um Material ======\n")
    print("Turmas disponíveis:")
    for turma in todas_as_turmas:
        print(f"  - Código: {turma.get('codTurma')} ({turma.get('curso')})")
    
    # Inserindo codigo da turma
    while True:
        codigoTurma = input("\nDigite o codigo da turma que deseja criar este material(digite 'cancelar' para sair): ").strip()

        if codigoTurma.lower() == 'cancelar':
            input("\nCriar material cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente
    
        if validar_turma(codigoTurma):
            item_dados["codTurma"] = codigoTurma
            break
        else:
            print("\nTurma não existe. Digite uma turma válida.")

    # Inserindo titulo material
    limpaTela()
    print("====== Cadastrar um Material ======\n")
    print (f"Turma selecionada: {item_dados["codTurma"]}")
    while True:
        titulo = input("\nDigite o titulo deste material: ")

        if not validar_titulo(titulo):
            print("\nO titulo precisa ter no minimo 5 caracteres.")
        else:
            item_dados["titulo"] = titulo
            break

    # Inserindo disciplina do material
    limpaTela()
    print("====== Cadastrar um Material ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    while True:
        disciplina = input("\nDigite a disciplina na qual esse material pertence: ")

        if not validar_disciplina(disciplina):
            print("\nDisciplina precisa ter no minimo 5 caracteres.")
        else:
            item_dados["disciplina"] = disciplina
            break

    # Inserindo link para material
    limpaTela()
    print("====== Cadastrar um Material ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    while True:
        link = input("\nCopie e cole aqui apenas 1 link para google drive, one drive ou afins: ")

        if not validar_link(link):
            print("\nDigite um link válido para prosseguir.")    
        else:
            item_dados["link"] = link
            break

    # Inserindo descrição
    limpaTela()
    print("====== Cadastrar um Material ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    print(f"Link: {item_dados["link"]}")
    
    item_dados["descricao"] = input("\nDigite uma descrição para seu material(pode deixar vazio também): ")

    # Inserindo rp e nome do professor ao material
    item_dados["RPprofessor"] = professor["rP"]
    item_dados["nomeProfessor"] = professor["name"]

    material.append(item_dados)
    salvarMaterial(material)

    limpaTela()
    print("====== Material Criado ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    print(f"Link: {item_dados["link"]}")
    print(f"Descrição: {item_dados["descricao"]}\n")
    print("Para alterar qualquer informação, volte ao menu anterior\n")
    print("======================================================\n")
    input("Pressione enter para voltar ao menu anterior...")
    limpaTela()

# ------- Fim do Criando Material -------

# Ver material postado pelo professor
def verMateriais(professor):
    
    # Usando uma variável de controle (flag).
    todos_os_materiais = carregar_material()
    encontrou_material = False # 1. A Flag começa como Falsa.
    i = 1

    limpaTela()
    print(f"====== Materiais Cadastrados por {professor['name']} ======")

    # Passamos por todos os materiais
    for material in todos_os_materiais:
        if material.get("RPprofessor") == professor['rP']:
            if not encontrou_material: # Se for o PRIMEIRO material encontrado
                encontrou_material = True # Envia um "aviso" para dizer que encontramos algo.

            # Exibimos o material imediatamente
            print(f"\nMaterial: {i}\n")
            print(f"Turma(Codigo): {material.get('codTurma', 'N/A')}")
            print(f"Título: {material.get('titulo', 'N/A')}")
            print(f"Professor: {material.get('nomeProfessor', 'N/A')}")
            print(f"Disciplina: {material.get('disciplina', 'N/A')}")
            print(f"Link do conteúdo: {material.get('link', 'N/A')}")
            print(f"Descrição: {material.get('descricao', 'N/A')}\n")
            print("=========================================")
            i = i+1
    if not encontrou_material: # Se o aviso nunca foi recebido...
        print("\nVocê ainda não cadastrou nenhum material.\n")
        print("=========================================")

    input("\nPressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Ver Material -------

# Deletar o material
def deletarMaterial(professor):
    
    # Exibe os materiais do professor, pede para ele escolher um número e o deleta após confirmação.
    limpaTela()
    print("====== Deletar Material Cadastrado ======")
    todos_os_materiais = carregar_material()
    
    # Filtrar e encontrar apenas os materiais do professor logado
    meus_materiais = [
        mat for mat in todos_os_materiais
        if mat.get("RPprofessor") == professor['rP']
        ]
    
    if not meus_materiais:
        input("Você não possui nenhum material para deletar. Pressione enter para voltar ao menu anterior...")
        limpaTela()
        return

    # Exibir a lista numerada de materiais para o professor escolher
    print("\nEstes são os seus materiais cadastrados:")
    for i, material in enumerate(meus_materiais, start=1):
        print(f"  {i}. Título: {material.get('titulo', 'N/A')} (Turma: {material.get('codTurma', 'N/A')})")
    print("\n======================================================\n")

    material_para_deletar = None
    
    # Loop para garantir que um número válido seja inserido
    while True:
        escolha = input("Digite o NÚMERO do material a ser deletado (ou 'cancelar' para voltar): ").strip()
        
        if escolha.lower() == 'cancelar':
            input("\nDeletar material cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return

        # Validação para garantir que a entrada é um número e está na faixa correta
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1 # O índice da lista é o número - 1
            if 0 <= escolha_idx < len(meus_materiais):
                material_para_deletar = meus_materiais[escolha_idx]
                break # Número válido, sai do loop
            else:
                print(f"Erro: Número '{escolha}' está fora do alcance. Escolha um número da lista.\n")
        else:
            print("Erro: Por favor, digite apenas o número correspondente ao material.\n")

    # Confirmação
    confirmacao = input(f"\nATENÇÃO: Tem certeza que deseja deletar o material '{material_para_deletar.get('titulo')}'? (S/N): ").strip()
    
    if confirmacao.upper() == "S":
        # Recria a lista de 'todos_os_materiais' excluindo o material escolhido.
        # É importante comparar o objeto inteiro para garantir que o item certo seja removido.
        materiais_atualizados = [mat for mat in todos_os_materiais if mat != material_para_deletar]
        
        salvarMaterial(materiais_atualizados)
        print("\n======================================================\n")
        input("Material deletado com sucesso. Pressione enter para voltar ao menu anterior...")
        limpaTela()
    else:
        print("\n======================================================\n")
        input("Deletar material cancelado. Pressione enter para voltar ao menu anterior...")
        limpaTela()
# ------- Fim do Deletar Material -------

# Alterar Material
def alterarMaterial(professor):
    """
    Exibe os materiais, permite ao professor escolher um para alterar um campo específico,
    e valida a nova entrada usando os validadores fornecidos.
    """
    # O dicionário de validadores, adaptado para os campos de material
    VALIDADORES = {
        "codTurma": (validar_turma, "Código de turma inválido ou não encontrado."),
        "titulo": (validar_titulo, "Título inválido. Deve ter no mínimo 5 caracteres."),
        "disciplina": (validar_disciplina, "Disciplina inválida. Deve ter no mínimo 5 caracteres."),
        "link": (validar_link, "Link inválido. Insira uma URL completa (ex: http://www.site.com).")
    }
    limpaTela()
    print("====== Alterar Material Cadastrado ======\n")
    todos_os_materiais = carregar_material()
    meus_materiais = [mat for mat in todos_os_materiais if mat.get("RPprofessor") == professor['rP']]
    
    if not meus_materiais:
        print("Você não possui nenhum material para alterar.\n")
        print("======================================================\n")
        input("Pressione enter para voltar ao menu anterior...")
        limpaTela()
        return

    # Etapa de seleção do material (idêntica à função de deletar)
    print("Estes são os seus materiais cadastrados:")
    for i, material in enumerate(meus_materiais, start=1):
        print(f"  {i}. Título: {material.get('titulo', 'N/A')} (Turma: {material.get('codTurma', 'N/A')})")
    print("\n======================================================")
    material_para_alterar = None

    # Laço para garantir que um número valido seja digitado.
    while True:
        escolha = input("\nDigite o número do material a ser alterado (ou 'cancelar' para voltar): ").strip()
        if escolha.lower() == 'cancelar':
            input("\nAlterar material cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela() 
            return
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(meus_materiais):
                material_para_alterar = meus_materiais[escolha_idx]
                break
            else:
                print(f"Erro: Número '{escolha}' não corresponde ao material.")
        else:
            print("Erro: Por favor, digite apenas o número presente na lista.")

    # Etapa de seleção do campo a ser alterado
    limpaTela()
    print("====== Alterando Material Cadastrado ======\n")
    print(f"Material: '{material_para_alterar.get('titulo')}'")
    chaves_protegidas = ["RPprofessor", "nomeProfessor"]
    chaves_disponiveis = [key for key in material_para_alterar.keys() if key not in chaves_protegidas]
    print("Campos disponíveis para alteração: " + ", ".join(chaves_disponiveis))
    
    while True: 
        chave_selecionada = input("\nDigite o nome EXATO do campo que você pretende modificar: ").strip()

        if chave_selecionada in chaves_protegidas:
            print(f"Erro: O campo '{chave_selecionada}' não pode ser alterado.")
        elif chave_selecionada not in material_para_alterar:
            print(f"Erro: O campo '{chave_selecionada}' não existe.")
        else:
            break
        
    # Etapa de validação do novo valor
    while True:
        novo_valor = input(f"\nDigite o novo valor para {chave_selecionada}: ").strip()
        
        if chave_selecionada in VALIDADORES:
            funcao_validacao, msg_erro = VALIDADORES[chave_selecionada]
            if funcao_validacao(novo_valor):
                break # Valor é válido, sai do loop
            else:
                print(msg_erro) # Valor inválido, pede novamente
        else:
            # Se não houver validador (ex: 'descricao'), aceita qualquer valor
            break

    # Atualiza o valor e salva
    material_para_alterar[chave_selecionada] = novo_valor
    # Como 'material_para_alterar' é uma referência a um item na lista 'todos_os_materiais',
    # a alteração já está refletida. Agora só precisamos salvar a lista inteira.
    salvarMaterial(todos_os_materiais)
    print("\n======================================================\n")
    input(f"Campo '{chave_selecionada}' atualizado com sucesso!\n\nPressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Alterar Material -------

# Menu das Atividades: Criar, Ver, Alterar e Deletar
def menuAtividade(professor):

    limpaTela()
    while True:
        print("====== Menu Atividade ======\n")
        print("1. Criar Atividade")
        print("2. Ver Atividade")
        print("3. Alterar Atividade")
        print("4. Deletar Atividade")
        print("5. Retornar a página anterior\n")
        print("======================================================\n")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            criarAtividade(professor)
        elif escolha == "2":
            verAtividade(professor)
        elif escolha == "3":
            alterarAtividade(professor)
        elif escolha == "4":
            deletarAtividade(professor)
        elif escolha == "5":
            limpaTela()
            return
        else:
            input("\nOpção inválida. Pressione enter para tentar novamente...")
            limpaTela()

# Criando Atividades
def criarAtividade(professor):

    atividades = carregar_atividade()
    todas_as_turmas = carregar_turmas()
    item_dados = {}

    limpaTela()
    print("====== Cadastrar uma Atividade ======\n")
    print("Turmas disponíveis:")
    for turma in todas_as_turmas:
        print(f"  - Código: {turma.get('codTurma')} ({turma.get('curso')})")

    # Inserindo codigo da turma
    while True:
        codigoTurma = input("\nDigite o codigo da turma que deseja criar esta atividade(digite 'cancelar' para sair): ").strip()

        if codigoTurma.lower() == 'cancelar':
            input("\nCriar atividade cancelada. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente
    
        if validar_turma(codigoTurma):
            item_dados["codTurma"] = codigoTurma
            break
        else:
            print("\nTurma não existe. Digite uma turma valida.")

    # Inserindo titulo atividade
    limpaTela()
    print("====== Cadastrar uma Atividade ======\n")
    print (f"Turma selecionada: {item_dados["codTurma"]}")
    while True: 
        titulo = input("\nDigite o titulo desta atividade: ")

        if not validar_titulo(titulo):
            print("\nO titulo precisa ter no minimo 5 caracteres.")
        else:
            item_dados["titulo"] = titulo
            break

    # Inserindo disciplina da atividade
    limpaTela()
    print("====== Cadastrar uma Atividade ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    while True:
        disciplina = input("\nDigite a disciplina na qual esta atividade pertence: ")

        if not validar_disciplina(disciplina):
            print("\nDisciplina precisa ter no minimo 5 caracteres.")
        else:
            item_dados["disciplina"] = disciplina
            break

    # Inserindo link da atividade
    limpaTela()
    print("====== Cadastrar uma Atividade ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    while True:
        link = input("\nCopie e cole aqui apenas 1 link para google drive, one drive ou afins: ")

        if not validar_link(link):
            print("\nDigite um link valido para prosseguir.")    
        else:
            item_dados["link"] = link
            break

    # Inserindo descrição da Atividade
    limpaTela()
    print("====== Cadastrar uma Atividade ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    print(f"Link: {item_dados["link"]}")
    item_dados["descricao"] = input("\nDigite uma descrição para sua atividade(pode deixar vazio também): ")

    # Inserindo rp e nome do professor a atividade
    item_dados["RPprofessor"] = professor["rP"]
    item_dados["nomeProfessor"] = professor["name"]

    atividades.append(item_dados)
    salvarAtividades(atividades)

    limpaTela()
    print("====== Atividadade Criada ======\n")
    print(f"Turma selecionada: {item_dados["codTurma"]}")
    print(f"Titulo: {item_dados["titulo"]}") 
    print(f"Disciplina: {item_dados["disciplina"]}")
    print(f"Link: {item_dados["link"]}")
    print(f"Descrição: {item_dados["descricao"]}\n")
    print("Para alterar qualquer informação, volte ao menu anterior\n")
    print("======================================================\n")
    input("Pressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Criar Atividade -------

# Ver atividades postadas pelo professor
def verAtividade(professor):
    
    # Usando uma variável de controle (flag).
    todas_as_atividades = carregar_atividade()
    encontrou_atividade = False # 1. A Flag começa como Falsa.
    i = 1

    limpaTela()
    print(f"====== Atividades Cadastradas por {professor['name']} ======")

    # Passamos por todos as atividades
    for atividade in todas_as_atividades:
        if atividade.get("RPprofessor") == professor['rP']:
            if not encontrou_atividade: # Se for a PRIMEIRA atividade encontrado
                encontrou_atividade = True # Envia um "aviso" para dizer que encontramos algo.

            # Exibimos a Atividade imediatamente
            print(f"\nAtividade: {i}\n")
            print(f"Turma(Codigo): {atividade.get('codTurma', 'N/A')}")
            print(f"Título: {atividade.get('titulo', 'N/A')}")
            print(f"Professor: {atividade.get('nomeProfessor', 'N/A')}")
            print(f"Disciplina: {atividade.get('disciplina', 'N/A')}")
            print(f"Link do conteúdo: {atividade.get('link', 'N/A')}")
            print(f"Descrição: {atividade.get('descricao', 'N/A')}")
            print("=========================================")
            i = i+1
    if not encontrou_atividade: # Se o aviso nunca foi recebido...
        print("\nVocê ainda não cadastrou nenhuma atividade.\n")
        print("=========================================")

    input("\nPressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Ver Atividade -------

# Deletar Atividade
def deletarAtividade(professor):
    
    # Exibe as Atividades do professor, pede para ele escolher um número e o deleta após confirmação.
    limpaTela()
    print("====== Deletar Atividade Cadastrada ======")
    todas_atividades = carregar_atividade()
    
    # Filtrar e encontrar apenas as atividades do professor logado
    minhas_atividades = [
        at for at in todas_atividades
        if at.get("RPprofessor") == professor['rP']
        ]
    
    if not minhas_atividades:
        input("Você não possui nenhuma atividade para deletar. Pressione enter para voltar ao menu anterior...")
        limpaTela()
        return

    # Exibir a lista numerada das atividades para o professor escolher
    print("\nEstes são as suas atividades cadastradas:")
    for i, atividades in enumerate(minhas_atividades, start=1):
        print(f"  {i}. Título: {atividades.get('titulo', 'N/A')} (Turma: {atividades.get('codTurma', 'N/A')})")
    print("\n======================================================\n")

    atividade_para_deletar = None

    # Loop para garantir que um número válido seja inserido
    while True:
        escolha = input("Digite o NÚMERO da atividade a ser deletada (ou 'cancelar' para voltar): ").strip()
        
        if escolha.lower() == 'cancelar':
            input("\nDeletar atividade cancelada. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return

        # Validação para garantir que a entrada é um número e está na faixa correta
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1 # O índice da lista é o número - 1
            if 0 <= escolha_idx < len(minhas_atividades):
                atividade_para_deletar = minhas_atividades[escolha_idx]
                break # Número válido, sai do loop
            else:
                print(f"Erro: Número '{escolha}' está fora do alcance. Escolha um número da lista.\n")
        else:
            print("Erro: Por favor, digite apenas o número correspondente a atividade.\n")

    # Confirmação final, como na função deletarProfessor
    confirmacao = input(f"\nATENÇÃO: Tem certeza que deseja deletar a atividade '{atividade_para_deletar.get('titulo')}'? (S/N): ").strip()
    
    if confirmacao.upper() == "S":
        # Recria a lista de 'todas_as_atividades' excluindo a atividade escolhida.
        # É importante comparar o objeto inteiro para garantir que o item certo seja removido.
        atividades_atualizadas = [at for at in todas_atividades if at != atividade_para_deletar]
        
        salvarAtividades(atividades_atualizadas)
        print("\n======================================================\n")
        input("Atividade deletada com sucesso. Pressione enter para voltar ao menu anterior...")
        limpaTela()
    else:
        print("\n======================================================\n")
        input("Deletar atividade cancelada. Pressione enter para voltar ao menu anterior...")
        limpaTela()
# ------- Fim do Deletar Atividade -------

# Alterar atividade
def alterarAtividade(professor):
    """
    Exibe as atividades, permite ao professor escolher um para alterar um campo específico,
    e valida a nova entrada usando os validadores fornecidos.
    """
    # O dicionário de validadores, adaptado para os campos da atividade
    VALIDADORES = {
        "codTurma": (validar_turma, "Código de turma inválido ou não encontrado."),
        "titulo": (validar_titulo, "Título inválido. Deve ter no mínimo 5 caracteres."),
        "disciplina": (validar_disciplina, "Disciplina inválida. Deve ter no mínimo 5 caracteres."),
        "link": (validar_link, "Link inválido. Insira uma URL completa (ex: http://www.site.com).")
    }
    limpaTela()
    print("====== Alterar Atividade Cadastrado ======\n")
    todas_as_atividades = carregar_atividade()
    minhas_atividades = [at for at in todas_as_atividades if at.get("RPprofessor") == professor['rP']]
    
    if not minhas_atividades:
        print("Você não possui nenhuma atividade para alterar.\n")
        print("======================================================\n")
        input("Pressione enter para voltar ao menu anterior...")
        limpaTela()        
        return

    # Etapa de seleção da atividade (idêntica à função de deletar)
    print("Estas são as suas atividades cadastradas:")
    for i, atividade in enumerate(minhas_atividades, start=1):
        print(f"  {i}. Título: {atividade.get('titulo', 'N/A')} (Turma: {atividade.get('codTurma', 'N/A')})")
    print("\n======================================================")
    atividade_para_alterar = None

    while True:
        escolha = input("\nDigite o NÚMERO da atividade a ser alterada (ou 'cancelar' para voltar): ").strip()
        if escolha.lower() == 'cancelar':
            input("\nAlterar atividade cancelada. Pressione enter para voltar ao menu anterior...")
            limpaTela() 
            return
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(minhas_atividades):
                atividade_para_alterar = minhas_atividades[escolha_idx]
                break
            else:
                print(f"Erro: Número '{escolha}' não corresponde a atividade.")
        else:
            print("Erro: Por favor, digite apenas o número presente na lista.")

    # Etapa de seleção do campo a ser alterado
    limpaTela()
    print("====== Alterando Atividade Cadastrada ======\n")
    print(f"Atividade: '{atividade_para_alterar.get('titulo')}'")
    chaves_protegidas = ["RPprofessor", "nomeProfessor"]
    chaves_disponiveis = [key for key in atividade_para_alterar.keys() if key not in chaves_protegidas]
    print("Campos disponíveis para alteração: " + ", ".join(chaves_disponiveis))
    
    while True:
        chave_selecionada = input("\nDigite o nome EXATO do campo que você pretende modificar: ").strip()

        if chave_selecionada in chaves_protegidas:
            print(f"Erro: O campo '{chave_selecionada}' não pode ser alterado.")
            return
        elif chave_selecionada not in atividade_para_alterar:
            print(f"Erro: O campo '{chave_selecionada}' não existe.")
            return
        else:
            break

    # Etapa de validação do novo valor
    while True:
        novo_valor = input(f"\nDigite o novo valor para {chave_selecionada}: ").strip()
        
        if chave_selecionada in VALIDADORES:
            funcao_validacao, msg_erro = VALIDADORES[chave_selecionada]
            if funcao_validacao(novo_valor):
                break # Valor é válido, sai do loop
            else:
                print(msg_erro) # Valor inválido, pede novamente
        else:
            # Se não houver validador (ex: 'descricao'), aceita qualquer valor
            break

    # Atualiza o valor e salva
    atividade_para_alterar[chave_selecionada] = novo_valor
    # Como 'atividade_para_alterar' é uma referência a um item na lista 'todas_as_atividades',
    # a alteração já está refletida. Agora só precisamos salvar a lista inteira.
    salvarAtividades(todas_as_atividades)
    print("\n======================================================\n")
    input(f"Campo '{chave_selecionada}' atualizado com sucesso!\n\nPressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Alterar Atividade -------

# Função Principal para Alterar a Nota
def alterarNotaAluno():
    """
    Permite selecionar uma turma, listar seus alunos, escolher um aluno
    e atribuir uma nova nota, validando a entrada.
    """
    limpaTela()
    print("====== Alterar Nota de Aluno ======\n")
    todas_as_turmas = carregar_turmas()
    todos_os_alunos = carregar_alunos()
    
    # Selecionar a turma
    print("Turmas disponíveis:")
    for turma in todas_as_turmas:
        print(f"  - Código: {turma.get('codTurma')} ({turma.get('curso')})")
        
    turma_selecionada_cod = None
    while True:
        cod_digitado = input("\nDigite o CÓDIGO da turma que deseja ver (ou 'cancelar' para voltar): ").strip()
        if cod_digitado.lower() == 'cancelar':
            input("\nAlterar nota aluno cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente
        
        # Verifica se o código da turma existe na lista de turmas carregada
        if any(turma['codTurma'] == cod_digitado for turma in todas_as_turmas):
            turma_selecionada_cod = cod_digitado
            break
        else:
            print(f"Erro: Código de turma '{cod_digitado}' não encontrado. Tente novamente.")

    # Filtrar e exibir os alunos daquela turma
    alunos_da_turma = [aluno for aluno in todos_os_alunos if aluno.get("codTurma") == turma_selecionada_cod]
    
    if not alunos_da_turma:
        print(f"\nNão há alunos cadastrados na turma '{turma_selecionada_cod}'.")
        input("Pressione enter para voltar ao menu anterior...")
        limpaTela()
        return
    
    limpaTela()
    print(f"====== Alunos da Turma: {turma_selecionada_cod} ======")
    for i, aluno in enumerate(alunos_da_turma, start=1):
        # Usamos .get('nota', 'N/A') para o caso de um aluno ainda não ter nota
        print(f"  {i}. {aluno.get('name')} (RA: {aluno.get('ra')}) - Nota Atual: {aluno.get('nota', 'N/A')}")
        
    # Escolher o aluno pelo número
    aluno_selecionado = None
    while True:
        escolha = input("\nDigite o NÚMERO do aluno que deseja alterar a nota (ou 'cancelar'): ").strip()
        if escolha.lower() == 'cancelar':
            input("\nAlterar nota aluno cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente

        if escolha.isdigit():
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(alunos_da_turma):
                aluno_selecionado = alunos_da_turma[escolha_idx]
                break
            else:
                print(f"Erro: Número '{escolha}' inválido. Escolha um número da lista.")
        else:
            print("Erro: Por favor, digite apenas o número correspondente ao aluno.")

    # Digitar e validar a nova nota
    nova_nota_str = None
    while True:
        nota_digitada = input(f"Digite a nova nota para {aluno_selecionado.get('name')} (de 0 a 10): ").strip()
        if nota_digitada.lower() == 'cancelar':
            input("\nAlterar nota aluno cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente
        
        if validar_nota(nota_digitada):
            nova_nota_str = nota_digitada
            break
        else:
            print("Erro: Nota inválida. Por favor, digite um número entre 0 e 10 (ex: 7.5).\n")
            
    # Atualizar o atributo e salvar o arquivo
    # Convertemos a nota para float antes de salvar
    aluno_selecionado['nota'] = float(nova_nota_str)
    
    # Como 'aluno_selecionado' é uma referência a um item na lista 'todos_os_alunos', a alteração já está refletida. Agora só precisamos salvar a lista inteira.
    salvar_alunos(todos_os_alunos)
    print("\n======================================================\n")
    print(f"Sucesso! A nota de {aluno_selecionado.get('name')} foi atualizada para {aluno_selecionado['nota']}.")
    input("Pressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim da Função Alterar Notas -------

# --- Loop Principal (O Cérebro do Programa) ---
def main():
    # Função principal refatorada para controlar os menus de acordo com o estado de login.
    professor_logado = None # A nossa variável de sessão começa vazia.

    while True:
        # Se ninguém estiver logado, mostra o menu principal para Login
        if professor_logado is None:
            print("====== Sistema v2.0 (Desconectado) ======\n")
            print("1. Fazer Login Professor")
            print("2. Sair do Sistema\n")
            print("=========================================\n")
            
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                # Aqui: `usuario_logado` recebe o resultado de `fazer_login()`
                professor_logado = fazer_login()
            elif escolha == '2':
                print("\nSaindo do sistema. Até mais!")
                break
            else:
                input("\nOpção inválida. Pressione enter para tentar novamente...")
                limpaTela()
        
        # Se alguém estiver logado, mostra o menu do usuario
        else:
            print(f"====== Bem vindo(a), {professor_logado['name']}! (Conectado) ======\n")
            print("1. Ver Meus Dados")
            print("2. Material")
            print("3. Atividades")
            print("4. Postar nota aluno")
            print("5. Fazer Logout")
            print("6. Sair do Sistema\n")
            print("======================================================\n")

            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                verMeusDados(professor_logado)
            elif escolha == '2':
                menuMaterial(professor_logado)
            elif escolha == '3':
                menuAtividade(professor_logado)
            elif escolha == '4':
                alterarNotaAluno()
            elif escolha == '5':
                input(f"\nAté logo, {professor_logado['name']}!\n\nPressione enter para voltar a tela principal...")
                professor_logado = None # Logout: limpamos a variável de sessão
                limpaTela()
            elif escolha == '6':
                input("\nSaindo do sistema. Até mais!\nPressione enter para sair...")
                break
            else:
                input("\nOpção inválida. Pressione enter para tentar novamente...")
                limpaTela()

# Inicia o programa
if __name__ == "__main__":
    main()