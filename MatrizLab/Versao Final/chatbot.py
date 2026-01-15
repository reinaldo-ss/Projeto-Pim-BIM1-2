import utils

#Função que exibe o menu de dúvidas do usuário.
def _exibir_manual_usuario():
    while True:
        utils.limpaTela()
        print("--- Manual do Usuário ---")
        print("Selecione o tipo de dúvida abaixo:")
        print("1 - Problemas com login")
        print("2 - Dúvidas sobre material")
        print("3 - Erro ao enviar atividades")
        print("4 - Problemas com cadastro")
        print("5 - Problemas para deletar usuários")
        print("6 - Nenhuma das alternativas acima")
        print("0 - Voltar ao menu anterior")

        opcao = input("\nDigite o número da opção desejada: ")

        # Sai deste loop e volta para o menu principal do chatbot
        if opcao == "0":
            break

        elif opcao == "1":
            utils.limpaTela()
            print("\nResposta:")
            print("Claudio: Para corrigir problemas com login, primeiro verifique se não digitou nenhum caractere errado.")
            print("Caso o erro persista, verifique se você está cadastrado no sistema.")

        elif opcao == "2":
            utils.limpaTela()
            print("\nResposta:")
            print("Claudio: Para acessar o material de aulas é necessário que você tenha o código da sua turma.")
            print("Se o código não funcionar, verifique se você digitou ele corretamente.")

        elif opcao == "3":
            utils.limpaTela()
            print("\nResposta:")
            print("Claudio: Caso esteja tendo problemas com o envio de atividades, verifique se a atividade ainda está válida.")
            print("Caso não esteja conseguindo acessar sua atividade, verifique com seu professor se o link da tarefa foi postado corretamente.")

        elif opcao == "4":
            utils.limpaTela()
            print("\nResposta:")
            print("Claudio: Caso esteja tendo problemas para cadastrar um usuário, verifique se todos os campos obrigatórios foram preenchidos.")
            print("Caso o problema persista, verifique se algum campo possui um caractere inválido.")


        elif opcao == "5":
            utils.limpaTela()
            print("\nResposta:")
            print("Claudio: Caso esteja com problemas para deletar um usuário, verifique se o mesmo está cadastrado no sistema.")
            print("Caso o problema persista, verifique se os dados do cadastro foram inseridos corretamente para deletá-lo.")

        elif opcao == "6":
            utils.limpaTela()
            print("\nClaudio: Nesse caso, entre em contato com um administrador pelos seguintes meios de contato:")
            print("Email: MatrizLab@gmail.com | Telefone: 11 4002-8922")
            input("\nPressione 'Enter' para voltar ao menu de dúvidas.")
            continue # Volta para o início do menu de dúvidas

        else:
            utils.limpaTela()
            input("\nClaudio: Opção inválida. Pressione 'Enter' e tente novamente.")
            continue # Volta para o início do menu de dúvidas

        # Esta parte só é executada se a opção for de 1 a 5
        resolvido = input("\nClaudio: Sua dúvida foi resolvida? (sim/não): ").strip().lower()

        if resolvido == "sim":
            print("\nClaudio: Que ótimo! Ficamos felizes em ajudar.")
        else: # Trata 'não' e qualquer outra resposta inválida da mesma forma
            print("\nClaudio: Entendido. Se o problema persistir, entre em contato com um administrador:")
            print("Email: MatrizLab@gmail.com | Telefone: 11 4002-8922")
        
        input("\nPressione 'Enter' para voltar ao menu de dúvidas.")

# Função Principal
def chatbot():
    while True:
        utils.limpaTela()
        print("===== Bem-vindo ao Chatbot de Suporte =====")
        print("""\nClaudio: Olá! Eu me chamo Claudio! E eu sou o bot assistente do sistema MatrizLab!
Se tiver alguma dúvida, digite '1' para conferir nosso manual do usuário.
Se deseja voltar ao menu principal do sistema, digite '0'""")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            utils.limpaTela()
            input("\nClaudio: Atendimento encerrado. Pressione 'Enter' para retornar ao menu principal do sistema...")
            utils.limpaTela()
            return

        elif escolha == "1":
            _exibir_manual_usuario()

        else:
            utils.limpaTela()
            input("\nClaudio: Opção inválida. Pressione 'Enter' e tente novamente.")

if __name__ == "__main__":
    chatbot()
