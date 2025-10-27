def chatbot():
    print("= Bem-vindo ao Chatbot de Suporte =")

    while True:
        print("\n Digite 1 para iniciar o atendimento.")
        print("Digite 0 para sair.")

        escolha = input("Escolha uma opção: ")

        if escolha == "0":
            print("\n Encerrando o atendimento. Até logo! ")
            break

        elif escolha == "1":
            while True:
                print("\n Selecione o tipo de dúvida abaixo:")
                print("1 - Problemas com login")
                print("2 - Dúvidas sobre material")
                print("3 - erro ao enviar atividades")
                print("4 - Nenhuma das alternativas acima")
                print("0 - Voltar ao menu inicial")

                opcao = input("Digite o número da opção desejada: ")

                if opcao == "0":
                    break  # volta ao menu principal

                elif opcao == "1":
                    print("\n Resposta:")
                    print("Para corrigir problemas com login primeiro verifique se não digitou nenhum caractere errado.")
                    print("Caso o erro persista verifique se você está cadastrado no sistema.")

                elif opcao == "2":
                    print("\n Resposta:")
                    print("Para acessar o material de aulas é necessário que você tenha o código da sua turma.")
                    print("Se o código não funcionar verifique se você digitou ele corretamente.")

                elif opcao == "3":
                    print("\n Resposta:")
                    print("Caso esteja tendo problemas com o envio de atividades, verifique se a atividade ainda está válida")
                    print("Caso não esteja conseguindo acessar sua atividade, verifique com seu professor se o link da tarefa foi postado corretamente")

                elif opcao == "4":
                    print("\n Então entre em contato com um administrador pelo seguinte e-mail ou telefone:")
                    print("email: (email exemplo) telefone: (telefone exemplo)")
                    continue  # volta ao menu de dúvidas direto

                else:
                    print("\n Opção inválida. Tente novamente.")
                    continue  # repete o menu de dúvidas

                # Pergunta se a dúvida foi resolvida
                resolvido = input("\n Sua dúvida foi resolvida? (sim/não): ").strip().lower()

                if resolvido == "sim":
                    print("\n Que ótimo! Ficamos felizes em ajudar.")
                elif resolvido == "não":
                    print("\n Nesse caso, entre em contato com um administrador pelo seguinte e-mail ou telefone:")
                    print("email: (email exemplo) telefone: (telefone exemplo)")
                else:
                    print("\n Opção inválida. Retornando ao menu de dúvidas.")

        else:
            print("\n Opção inválida. Tente novamente.")

# Chamar o chatbot
chatbot()
