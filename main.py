from servicos import (
    cadastrar_chamado,
    filtrar_por_situacao,
    listar_chamados,
    obter_categorias_unicas,
    atualizar_situacao_chamado,
    busca_chamado_por_id,
    filtrar_por_prioridade,
    excluir_chamado,
    gerar_relatorios_estatistico
)

def main():
    chamados = []

    # Carga inicial com 3 chamados para testes/demonstração
    cadastrar_chamado(
        chamados, "Sem acesso ao sistema", "Erro de login no portal", "Alta", "Acesso", "Carlos Silva"
    )
    cadastrar_chamado(
        chamados, "Impressora offline", "Impressora do setor B não responde", "Média", "Hardware", "Ana Souza"
    )
    cadastrar_chamado(
        chamados, "Atualizar software", "Instalar nova versão do editor", "Baixa", "Software", "Mariana Lima"
    )

    while True:
        print("\n" + "=" * 40)
        print("    GERENCIADOR DE CHAMADOS INTERNOS")
        print("=" * 40)
        print("1 - Cadastrar novo chamado")
        print("2 - Listar todos os chamados")
        print("3 - Buscar chamado por ID")
        print("4 - Filtrar chamados por situação")
        print("5 - Filtrar chamados por prioridade")
        print("6 - Atualizar situação de um chamado")
        print("7 - Ver categorias atendidas")
        print("8 - Painel estatístico / Relatório")
        print("9 - Excluir um chamado")
        print("0 - Sair do sistema")
        print("=" * 40)

        opcao = input("Escolha uma opção (0-9): ").strip()

        if not opcao.isdigit():
            print("\nErro: Digite apenas números válidos de 0 a 9!")
            continue

        elif opcao == "1":
            print("\n--- CADASTRAR NOVO CHAMADO ---")
            titulo = input("Título: ").strip()
            descricao = input("Descrição: ").strip()
            prioridade = input("Prioridade [Baixa / Média / Alta / Crítica]: ").strip()
            categoria = input("Categoria [Acesso / Hardware / Software / Outros]: ").strip()
            solicitante = input("Nome do Solicitante: ").strip()

            if not titulo or not descricao or not solicitante:
                print("\nErro: Título, Descrição e Solicitante são campos obrigatórios!")
                continue

            novo = cadastrar_chamado(chamados, titulo, descricao, prioridade, categoria, solicitante)
            print(f"\nChamado #{novo.id} registrado com sucesso!")

        elif opcao == "2":
            listar_chamados(chamados)

      
        elif opcao == "3":
            id_input = input("\nDigite o ID do chamado: ").strip()
            if id_input.isdigit():
                chamado = busca_chamado_por_id(chamados, int(id_input))
                if chamado:
                    print("\n--- DETALHES DO CHAMADO ---")
                    print(chamado)
                else:
                    print("\nChamado não encontrado!")
            else:
                print("\nErro: O ID deve ser um valor numérico!")

       
        elif opcao == "4":
            while True:
                print("\nEscolha a situação desejada:")
                print("1 - Aberto | 2 - Em Atendimento | 3 - Concluído | 4 - Fechado | 5 - Reaberto")
                opcao_situacao = input("Opção (1-5): ").strip()

                if opcao_situacao.isdigit() and 1 <= int(opcao_situacao) <= 5:
                    filtrar_por_situacao(chamados, opcao_situacao)
                else:
                    print("Opção inválida! Digite um número de 1 a 5.")
                    continue

                # Validação de repetição s/n
                while True:
                    menu = input("\nDeseja realizar outro filtro de situação? [s] Sim / [n] Não: ").strip().lower()
                    if menu in ["s", "n"]:
                        break
                    print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

                if menu == "n":
                    print("Retornando ao menu principal...")
                    break

      
        elif opcao == "5":
            while True:
                prioridade_desejada = input("\nDigite a prioridade [Baixa / Média / Alta / Crítica]: ").strip().lower()

                if prioridade_desejada:
                    filtrar_por_prioridade(chamados, prioridade_desejada)
                else:
                    print("Erro: A prioridade não pode ficar em branco!")
                    continue

                # Validação de repetição s/n
                while True:
                    menu = input("\nDeseja realizar outro filtro de prioridade? [s] Sim / [n] Não: ").strip().lower()
                    if menu in ["s", "n"]:
                        break
                    print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

                if menu == "n":
                    print("Retornando ao menu principal...")
                    break

        # --- OPÇÃO 6: ATUALIZAR SITUAÇÃO ---
        elif opcao == "6":
            while True:
                print("\n--- ATUALIZAR SITUAÇÃO DE UM CHAMADO ---")
                id_input = input("Digite o ID do chamado: ").strip()

                if not id_input.isdigit():
                    print("Erro: O ID deve ser um valor numérico!")
                    continue

                id_chamado = int(id_input)
                chamado = busca_chamado_por_id(chamados, id_chamado)

                if not chamado:
                    print(f"Chamado com ID {id_chamado} não foi encontrado!")
                else:
                    print(f"\nChamado: {chamado.titulo} | Situação atual: {chamado.situacao}")
                    print("\nEscolha a nova situação:")
                    print("1 - Em Atendimento | 2 - Concluído | 3 - Fechado | 4 - Reaberto")
                    nova_opcao = input("Opção desejada (1-4): ").strip()

                    if nova_opcao in ["1", "2", "3", "4"]:
                        dado_extra = ""
                        if nova_opcao == "1":
                            dado_extra = input("Digite o nome do técnico responsável: ").strip()
                        elif nova_opcao == "2":
                            dado_extra = input("Digite a descrição da solução técnica: ").strip()

                        if atualizar_situacao_chamado(chamado, nova_opcao, dado_extra):
                            print(f"\nSituação atualizada com sucesso para: {chamado.situacao}")
                    else:
                        print("Opção de situação inválida!")

                # Validação de repetição s/n
                while True:
                    resposta = input("\nDeseja atualizar outro chamado? [s] Sim / [n] Não: ").strip().lower()
                    if resposta in ["s", "n"]:
                        break
                    print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")

                if resposta == "n":
                    print("Retornando ao menu principal...")
                    break

        
        elif opcao == "7":
            obter_categorias_unicas(chamados)

      
        elif opcao == "8":
            gerar_relatorios_estatistico(chamados)

       
        elif opcao == "9":
            id_input = input("\nDigite o ID do chamado que deseja excluir: ").strip()
            if id_input.isdigit():
                if excluir_chamado(chamados, int(id_input)):
                    print(f"\nChamado #{id_input} excluído com sucesso!")
                else:
                    print("\nChamado não encontrado!")
            else:
                print("\nErro: Digite um ID numérico válido!")

       
        elif opcao == "0":
            print("\nEncerrando o Gerenciador de Chamados... Até logo!")
            break

        else:
            print("\nOpção inválida! Escolha um número de 0 a 9.")

if __name__ == "__main__":
    main()