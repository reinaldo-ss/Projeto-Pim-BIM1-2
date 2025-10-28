import json
import os
import re
import random
import string

# Diretório base (onde o script atual está salvo)
base_dir = os.path.dirname(os.path.abspath(__file__))

# Caminhos absolutos baseados na localização do script
caminhoProfessor = os.path.join(base_dir, "professor", "dadosProfessor.json")

# Função que tira os dados anteriores, pra não ficar poluido a tela
def limpaTela():
    os.system("cls")

# Salva a lista de usuários no arquivo JSON
def salvarProfessores(professores):
    with open(caminhoProfessor, "w", encoding="utf-8") as f:
        json.dump(professores, f, indent=4)

# Carrega os dados do arquivo JSON.
def carregar_dados():
    if not os.path.exists(caminhoProfessor):
        return []
    with open(caminhoProfessor, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

# Validando nome para que não tenha numeros ou caracter especial
def validar_nome(nome):
    nome = nome.strip()
    # Permite letras (inclusive acentuadas) e espaços
    return bool(re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome))

# Função para validar se o CPF possui letras ou caracter especial
def validar_cpf(cpf):
    cpf = re.sub(r"[^0-9]", "", cpf)

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    return True

# Validando formato básico de e-mail
def validar_email(email):
    padrao = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(padrao, email))

# Lógica de validação da senha agora exige exatamente 8 caracteres.
def validar_senha(senha):
    # Valida se a senha tem exatamente 8 caracteres, ignorando espaços.
    senha_formatada = re.sub(r'\s+', '', senha)
    return len(senha_formatada) == 8 # Mudamos de >= para ==

# Validando se o numero de telefone possui 11 ou 13 digitos e nenhuma letra
def validar_numTelefone(numTelefone):
    numTelefone_formatado = re.sub(r"[^0-9]", "", numTelefone)
    return len(numTelefone_formatado) in [11, 13]

# Gera um RP único de 7 caracteres (letras e números).
def gerar_rP_unico():
    dados = carregar_dados()
    caracteres = string.ascii_uppercase + string.digits

    while True:
        rP = "".join(random.choices(caracteres, k=7))
        if not any(p.get("rP") == rP for p in dados):
            return rP
#-----------------------------------------------------------------------

# Função para exibir os dados
def verDados():
    dados = carregar_dados()
    encontrou_dados = False

    limpaTela()
    print ("====== Professores Cadastrados ======\n")
    for entrada in dados:
        if not encontrou_dados:
            encontrou_dados = True

        name = entrada["name"]
        rP = entrada["rP"]
        cpf = entrada["cpf"]
        numTelefone = entrada["numTelefone"]
        email = entrada["email"]
        senha = entrada["senha"]

        print (f"Nome: {name}")
        print (f"RP(Registro do Professor): {rP}")
        print (f"Email: {email}")
        print (f"Senha: {senha}")
        print (f"CPF: {cpf}")
        print (f"Numero de Telefone: {numTelefone}\n")
        print ("======================================================\n")

    if not encontrou_dados:
        print("Você ainda não cadastrou nenhum professor.\n")
        print("=========================================")

    input("\nPressione enter para voltar ao menu anterior...")
    limpaTela()

# Cadastrando professor 
def addDados():
    item_dados = {}
    dados = carregar_dados()

    limpaTela()
    print("====== Cadastrar um Professor ======\n")    
    while True:
        nome = input("Digite o nome do professor(ou 'cancelar' para voltar): ").strip()

        if nome.lower() == 'cancelar':
            input("\nCriar professor cancelado. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return # Sai da função imediatamente
        
        if validar_nome(nome):
            item_dados["name"] = nome.title()
            break
        else:
            print("\nNome inválido. Digite apenas letras e espaços.\n")

    # Verificando se CPF esta correto e se não possui letras
    limpaTela()
    print("====== Cadastrar um Professor ======\n") 
    print (f"Nome do Professor: {item_dados["name"]}")
    while True:
        cpf = input("\nDigite seu CPF com 11 dígitos (apenas números): ").strip()

        if not validar_cpf(cpf):
            print("\nCPF inválido. Tente novamente.")

        elif any(p.get("cpf") == cpf for p in dados):
            print("\nCPF já cadastrado. Digite outro.")

        else:
            item_dados["cpf"] = cpf
            break
    
    # Verificando se o e-mail atende aos requisitos para ser cadastrado
    limpaTela()
    print("====== Cadastrar um Professor ======\n") 
    print (f"Nome do Professor: {item_dados["name"]}")
    print (f"CPF: {item_dados["cpf"]}")
    while True:
        email = input("\nDigite seu email: ").strip()
        if not validar_email(email):
            print("\nE-mail inválido. Digite novamente (exemplo: usuario@email.com)")
        elif any(p.get("email") == email for p in dados):
            print("\nE-mail já cadastrado. Digite outro.")
        else:
            item_dados["email"] = email
            break    

    # Validação/salvamento de senha (aceita qualquer caractere, remove espaços)
    limpaTela()
    print("====== Cadastrar um Professor ======\n") 
    print (f"Nome do Professor: {item_dados["name"]}")
    print (f"CPF: {item_dados["cpf"]}")
    print (f"E-mail: {item_dados["email"]}")
    while True:
        senha = input("\nDigite sua senha (mínimo 8 caracteres): ")
        if not validar_senha(senha):
            print("\nSenha inválida. Sua deve conter 8 caracteres.")
        else:
            item_dados["senha"] = re.sub(r'\s+', '', senha)
            break

    # Verificando telefone e duplicidade
    limpaTela()
    print("====== Cadastrar um Professor ======\n") 
    print (f"Nome do Professor: {item_dados["name"]}")
    print (f"CPF: {item_dados["cpf"]}")
    print (f"E-mail: {item_dados["email"]}")
    print (f"Senha: {item_dados["senha"]}")
    while True:
        # Instrução no input esta mais clara.
        numTelefone = input("\nDigite seu telefone com DDD (11 ou 13 dígitos): ").strip()
        
        if not validar_numTelefone(numTelefone):
            # A mensagem de erro já estava correta.
            print("\nNúmero inválido. O telefone deve ter 11 dígitos (celular) ou 13 dígitos (internacional).")

        elif any(p.get("numTelefone") == re.sub(r'[^0-9]','',numTelefone) for p in dados):
            print("\nNúmero de telefone já cadastrado.")

        else:
            item_dados["numTelefone"] = re.sub(r'[^0-9]','',numTelefone)
            break
        
    # Gera RP automático e único
    item_dados["rP"] = gerar_rP_unico()
    print (f"RP gerado: {item_dados["rP"]}")

    # Envia os dados para o JSON
    dados.append(item_dados)
    with open(caminhoProfessor, "w") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

    # Menu de exibição
    limpaTela()
    print ("====== Professor Criado ======\n") 
    print (f"Nome do Professor: {item_dados["name"]}")
    print (f"CPF: {item_dados["cpf"]}")
    print (f"E-mail: {item_dados["email"]}")
    print (f"Senha: {item_dados["senha"]}")
    print (f"Telefone: {item_dados["numTelefone"]}")
    print (f"RP(Registro do Professor): {item_dados["rP"]}\n")
    print ("======================================================\n")
    print ("Para efetuar Login utilize:\n")
    print (f"RP: {item_dados['rP']}\nSenha: {item_dados["senha"]}\n")
    print ("Para alterar qualquer informação, volte ao menu anterior\n")

    print("======================================================\n")
    input("Pressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Criando Professor -------

# Deletar professor
def deletarProfessor():
    """
    Esta função gerencia a exclusão de um professor. Ela exibe uma lista
    de todos os professores cadastrados, permite ao usuário escolher um
    pelo número correspondente e, após uma confirmação, o remove do sistema.
    """
    limpaTela()
    print("====== Deletar Professor ======")
    
    # Carregar todos os professores
    todos_os_professores = carregar_dados()
    
    # Verificar se existem professores para deletar
    if not todos_os_professores:
        input("\nNão há nenhum professor cadastrado para deletar. Pressione enter para voltar...")
        limpaTela()
        return

    # Exibir a lista numerada de professores para o usuário escolher
    print("\nEstes são os professores cadastrados no sistema:")
    for i, professor in enumerate(todos_os_professores, start=1):
        print(f"  {i}. Nome: {professor.get('name', 'N/A')} (RP: {professor.get('rP', 'N/A')})")
    print("\n======================================================\n")

    professor_para_deletar = None
    
    # Loop para garantir que um número válido seja inserido
    while True:
        escolha = input("Digite o NÚMERO do professor a ser deletado (ou 'cancelar' para voltar): ").strip()
        
        if escolha.lower() == 'cancelar':
            input("\nOperação cancelada. Pressione enter para voltar ao menu anterior...")
            limpaTela()
            return

        # Validação para garantir que a entrada é um número e está na faixa correta
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1 # O índice da lista é o número - 1
            if 0 <= escolha_idx < len(todos_os_professores):
                professor_para_deletar = todos_os_professores[escolha_idx]
                break # Número válido, sai do loop
            else:
                print(f"Erro: Número '{escolha}' está fora do alcance. Escolha um número da lista.\n")
        else:
            print("Erro: Por favor, digite apenas o número correspondente ao professor.\n")

    # Confirmação da exclusão
    confirmacao = input(f"\nATENÇÃO: Tem certeza que deseja deletar o professor '{professor_para_deletar.get('name')}'? (S/N): ").strip()
    
    if confirmacao.upper() == "S":
        # Recria a lista de 'todos_os_professores' excluindo o professor escolhido.
        professores_atualizados = [prof for prof in todos_os_professores if prof != professor_para_deletar]
        
        salvarProfessores(professores_atualizados) # Salva a nova lista sem o professor
        
        print("\n======================================================\n")
        input("Professor deletado com sucesso. Pressione enter para voltar ao menu anterior...")
        limpaTela()
    else:
        print("\n======================================================\n")
        input("Operação cancelada. Pressione enter para voltar ao menu anterior...")
        limpaTela()
# ------- Fim do Deletar Professor -------

# Alterando professor
def alterarProfessor():
    """
    Gerencia a alteração dos dados de um professor. O processo é dividido em etapas:
    1. Exibe uma lista de todos os professores para seleção por número.
    2. Pede ao usuário para escolher qual campo deseja alterar.
    3. Solicita o novo valor e o valida antes de salvar.
    """
    # Dicionário que conecta o nome do campo à sua função de validação e mensagem de erro.
    VALIDADORES = {
        "name": (validar_nome, "Nome inválido. Digite apenas letras e espaços."),
        "cpf": (validar_cpf, "CPF inválido."),
        "email": (validar_email, "E-mail inválido. (ex: usuario@email.com)"),
        "senha": (validar_senha, "Senha inválida. Precisa ter no máximo 8 caracteres."),
        "numTelefone": (validar_numTelefone, "Número inválido. Deve ter 11 ou 13 dígitos.")
    }
    
    limpaTela()
    print("====== Alterar Cadastro de Professor ======\n")
    
    dados_professores = carregar_dados()
    
    if not dados_professores:
        input("Não há nenhum professor cadastrado para alterar. Pressione enter para voltar...")
        limpaTela()
        return

    # Seleção do Professor
    print("Estes são os professores cadastrados:")
    for i, prof in enumerate(dados_professores, start=1):
        print(f"  {i}. Nome: {prof.get('name', 'N/A')} (RP: {prof.get('rP', 'N/A')})")
    print("\n======================================================")
    
    professor_para_alterar = None
    while True:
        escolha = input("\nDigite o NÚMERO do professor a ser alterado (ou 'cancelar' para voltar): ").strip()
        if escolha.lower() == 'cancelar':
            input("\nOperação cancelada. Pressione enter para voltar ao menu anterior...")
            limpaTela() 
            return
        
        if escolha.isdigit():
            escolha_idx = int(escolha) - 1
            if 0 <= escolha_idx < len(dados_professores):
                professor_para_alterar = dados_professores[escolha_idx]
                break
            else:
                print(f"Erro: Número '{escolha}' está fora da lista.")
        else:
            print("Erro: Por favor, digite apenas o número correspondente ao professor.")

    # Seleção do Campo a ser Alterado
    limpaTela()
    print("====== Alterar Cadastro de Professor ======\n")
    print(f"Alterando dados de: '{professor_para_alterar.get('name')}'")
    
    chaves_protegidas = ["rP"] 
    chaves_disponiveis = [key for key in professor_para_alterar.keys() if key not in chaves_protegidas]
    print("Campos disponíveis para alteração: " + ", ".join(chaves_disponiveis))
    
    chave_selecionada = ""
    while True: 
        chave_selecionada = input("\nDigite o nome EXATO do campo que você pretende modificar: ").strip()
        if chave_selecionada in chaves_protegidas:
            print(f"Erro: O campo '{chave_selecionada}' não pode ser alterado.")
        elif chave_selecionada not in professor_para_alterar:
            print(f"Erro: O campo '{chave_selecionada}' não existe.")
        else:
            break
            
    # Entrada e Validação do Novo Valor
    while True:
        novo_valor = input(f"\nDigite o novo valor para '{chave_selecionada}': ").strip()
        
        if chave_selecionada in VALIDADORES:
            funcao_validacao, msg_erro = VALIDADORES[chave_selecionada]
            if funcao_validacao(novo_valor):
                # Formatações pós-validação podem ser adicionadas aqui, se necessário
                if chave_selecionada == "name":
                    novo_valor = novo_valor.title()
                break # Valor é válido, sai do loop
            else:
                print(msg_erro) # Valor inválido, mostra o erro e pede novamente
        else:
            # Se não houver validador específico para o campo, aceita o valor
            break

    # Atualização e Salvamento
    professor_para_alterar[chave_selecionada] = novo_valor
    
    salvarProfessores(dados_professores) # Salva a lista inteira com o item já modificado
    
    print("\n======================================================\n")
    input(f"Campo '{chave_selecionada}' atualizado com sucesso!\n\nPressione enter para voltar ao menu anterior...")
    limpaTela()
# ------- Fim do Alterar Professor -------

# Função principal de Escolhas existentes no programa
def main():

    while True:
        print ("====== Bem Vindo! (Conectado): ======\n")
        print ("(1) Ver Dados")
        print ("(2) Adicionar professor")
        print ("(3) Deletar professor")
        print ("(4) Alterar dado professor")
        print ("(5) Sair\n")
        print("=========================================\n")

        escolha = input("Escolha uma das opções: ")

        if escolha == "1":
            verDados()
        elif escolha == "2":
            addDados()
        elif escolha == "3":
            deletarProfessor()
        elif escolha == "4":
            alterarProfessor()
        elif escolha == "5":
            break
        else:
            input("\nOpção inválida.\nPressione enter para tentar novamente...")
            limpaTela()

# Inicia o programa
if __name__ == "__main__":
    main()