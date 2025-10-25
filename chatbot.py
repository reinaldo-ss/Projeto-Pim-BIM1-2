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
                print("\nSelecione o tipo de dúvida abaixo:")
                print("1 - Problemas com cadastro")
                print("2 - Dúvidas sobre pagamentos")
                print("3 - Erros no aplicativo")
                print("4 - Nenhuma das alternativas acima")
                print("0 - Voltar ao menu inicial")

                opcao = input("Digite o número da opção desejada: ")

                if opcao == "0":
                    break  # volta ao menu principal

                elif opcao == "1":
                    print("\n Resposta:")
                    print("Para corrigir problemas de cadastro, verifique se todos os campos foram preenchidos corretamente.")
                    print("Caso o erro persista, limpe o cache do navegador e tente novamente.")

                elif opcao == "2":
                    print("\n Resposta:")
                    print("Os pagamentos podem demorar até 24 horas para serem confirmados.")
                    print("Se o valor já foi debitado e não consta no sistema, entre em contato com o suporte.")

                elif opcao == "3":
                    print("\n Resposta:")
                    print("Erros no aplicativo podem ocorrer por causa de versões desatualizadas.")
                    print("Reinstale o app e tente novamente.")

                elif opcao == "4":
                    print("\n Contato com o suporte humano:")
                    print("Envie um e-mail para: suporte@empresa.com")
                    continue  # volta ao menu de dúvidas direto

                else:
                    print("\n Opção inválida. Tente novamente.")
                    continue  # repete o menu de dúvidas

                # Pergunta se a dúvida foi resolvida
                resolvido = input("\nSua dúvida foi resolvida? (sim/não): ").strip().lower()

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
