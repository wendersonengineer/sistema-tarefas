# Sistema simples de cadastro
# Versão monolítica

registros = []

while True:

    print("\n===== MENU =====")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1 - CADASTRAR
    if opcao == "1":

        nome = input("Digite o nome para cadastro: ")

        registros.append(nome)

        print("Registro cadastrado com sucesso!")


    # OPÇÃO 2 - LISTAR
    elif opcao == "2":

        if len(registros) == 0:
            print("Nenhum registro cadastrado.")

        else:
            print("\nRegistros cadastrados:")

            for i in range(len(registros)):
                print(i, "-", registros[i])


    # OPÇÃO 3 - ATUALIZAR
    elif opcao == "3":

        if len(registros) == 0:
            print("Nenhum registro disponível para atualização.")

        else:
            print("\nRegistros cadastrados:")

            for i in range(len(registros)):
                print(i, "-", registros[i])

            indice = int(input("Digite o número do registro que deseja atualizar: "))

            if indice >= 0 and indice < len(registros):

                novo_nome = input("Digite o novo nome: ")

                registros[indice] = novo_nome

                print("Registro atualizado com sucesso!")

            else:
                print("Registro inválido.")


    # OPÇÃO 4 - SAIR
    elif opcao == "4":

        print("Encerrando o sistema...")

        break


    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Tente novamente.")