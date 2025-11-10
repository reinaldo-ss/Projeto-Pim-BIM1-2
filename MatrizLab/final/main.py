import interface_admin
import interface_professores
import interface_alunos
import utils

def menu_principal():
    """
    Menu Principal do Sistema, responsável por ser o ponto de entrada
    de todos os tipos de usuários do sistema.
    """
    while True:
        utils.limpaTela()
        print("==== Bem-vindo(a) ao sistema MatrizLab ====")
        print("\n Selecione seu tipo de Usuário:")
        print("1. Administrador")
        print("2. Professor")
        print("3. Aluno")
        print("4. Fechar o Sistema\n")

        opcao = input("\n Escolha uma opção: ")

        if opcao == "1":
            # chama a função principal do módulo de administrador
            interface_admin.iniciar_menu()
        elif opcao == "2":
            # chama a função principal do módulo de professor
            interface_professores.iniciar_menu()
        elif opcao == "3":
            # chama a função principal do módulo de aluno
            interface_alunos.iniciar_menu()
        elif opcao == "4":
            utils.limpaTela()
            print("Encerrando Sistema...")
            break
        else:
            # Mensagem de erro caso seja inserida uma resposta inválida
            utils.limpaTela()
            input("Opção Inválida! Pressione Enter para tentar novamente")

# Comando que inicializa o programa
if __name__ == "__main__":
    menu_principal()
