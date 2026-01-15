import utils

def chatbot():
    print("= Bem-vindo ao Chatbot de Suporte =")
    utils.limpaTela()

    while True:
        print("Digite 1 para iniciar o atendimento.")
        print("Digite 0 para sair.")

        escolha = input("\nEscolha uma opção: ")

        if escolha == "0":
            utils.limpaTela()
            input("\nEncerrando o atendimento. Pressione 'Enter' para retornar ao menu")
            return

        elif escolha == "1":
            utils.limpaTela()
            while True:
                print("Selecione o tipo de dúvida abaixo:")
                print("1 - Problemas com login")
                print("2 - Dúvidas sobre material")
                print("3 - Erro ao enviar atividades")
                print("4 - Problemas com cadastro")
                print("5 - Problemas para deletar usuários")
                print("6 - Nenhuma das alternativas acima")
                print("0 - Voltar ao menu inicial")

                opcao = input("Digite o número da opção desejada: ")

                if opcao == "0":
                    return  # volta ao menu principal

                elif opcao == "1":
                    print("\nResposta:")
                    print("Para corrigir problemas com login primeiro verifique se não digitou nenhum caractere errado.")
                    print("Caso o erro persista verifique se você está cadastrado no sistema.")

                elif opcao == "2":
                    print("\nResposta:")
                    print("Para acessar o material de aulas é necessário que você tenha o código da sua turma.")
                    print("Se o código não funcionar verifique se você digitou ele corretamente.")

                elif opcao == "3":
                    print("\nResposta:")
                    print("Caso esteja tendo problemas com o envio de atividades, verifique se a atividade ainda está válida")
                    print("Caso não esteja conseguindo acessar sua atividade, verifique com seu professor se o link da tarefa foi postado corretamente")

                elif opcao == "4":
                    print("\nResposta:")
                    print(" caso esteja tendo problemas para cadastrar um usuário, verifique se todos os campos obrigatórios foram preenchidos.")
                    print("caso o problema persista, verifique se algum campo possui um caractere inválido.")

                elif opcao == "5":
                    print("\nResposta:")
                    print(" caso esteja com problemas para deletar um usuário, verifique se o mesmo esta cadastrado no sistema.")
                    print(" caso o problema persista, verifique se os dados do cadastro foram inseridos corretamente para deleta-lo")
                        

                elif opcao == "6":
                    print("\nEntão entre em contato com um administrador pelo seguinte e-mail ou telefone:")
                    print("Email: MatrizLab@gmail.com telefone: 11 4002-8922")
                    continue  # volta ao menu de dúvidas direto

                else:
                    print("\nOpção inválida. Tente novamente.")
                    continue  # repete o menu de dúvidas

                # Pergunta se a dúvida foi resolvida
                resolvido = input("\n Sua dúvida foi resolvida? (sim/não): ").strip().lower()

                if resolvido == "sim":
                    print("\n Que ótimo! Ficamos felizes em ajudar.")
                elif resolvido == "não":
                    print("\n Nesse caso, entre em contato com um administrador pelo seguinte e-mail ou telefone:")
                    print("Email: MatrizLab@gmail.com telefone: 11 4002-8922")
                else:
                    print("\n Opção inválida. Retornando ao menu de dúvidas.")

        else:
            print("\n Opção inválida. Tente novamente.")

if __name__ == "__main__":
    chatbot()
