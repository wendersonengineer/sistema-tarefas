
def cadastrar_tarefa(tarefas):
    titulo = input("Título da tarefa: ").strip()
    prioridade = input("Prioridade (baixa, média, alta): ").lower()

    # validações
    if not titulo:
        print("X Título não pode ser vazio.")
        return
    if prioridade not in ["baixa", "media", "alta"]:
        print("X Prioridade inválida. Use: baixa, média ou alta.")
        return

    # Estrutura da terefa
    tarefa = {
        "titulo": titulo,
        "prioridade": prioridade,
        "situacao": "pendente"
    }

    tarefas.append(tarefa)
    print("Tarefa cadastrada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i} - {tarefa['titulo']} | prioridade: {tarefa['prioridade']} | situção: {tarefa['situacao']}")



def atualizar_tarefa(tarefas):
    if not tarefas:
        print("Nenhuma tarefa para atualizar.")
        return
    numero = input("Digite o número da tarefa a concluir: ")

    # Validação
    if not numero.isdigit():
        print("X Entrada inválida. Digite apenas números.")
        return

    indice = int(numero) - 1 # Ajusta para  indice interno (começa em 0)

    if 0 <= indice <len(tarefas):
        tarefas[indice]["situacao"] = "concluída"
        print("Tarefa concluíoda com sucesso!")
    else:
        print("X Tarefa inexistente.")


def mostar_menu():
    print("\n1 - Cadatsrar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar situação")
    print("4 - Encerrar sistema")
    return input("Escolha uma opcao: ")


# ---------------------------------
#       PROGRAMA PRINCIPAL
# ---------------------------------

tarefas = []
while True:
    opcao = mostar_menu()

    if opcao == "1":
        cadastrar_tarefa(tarefas)
    elif opcao == "2":
        listar_tarefas(tarefas)
    elif opcao == "3":
        atualizar_tarefa(tarefas)
    elif opcao == "4":
        print("Sistema encerrado.")
        break
    else:
        print("X Opção inválida. Escolha um número de 1 a 4.")



