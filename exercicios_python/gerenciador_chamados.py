# Gerenciador de chamados com funções:
# 1. Criando arquivo e os dados iniciais
chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão", 
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hadware"
    },
    {
        "id": 3,
        "titulo": "Internet instável no setor comercial", 
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "rede" 
    },
    {
        "id": 4,
        "titulo": "Configuração de e-mail corporativo", 
        "prioridade": "baixa",
        "situacao": "fechado",
        "categoria": "hadware"
    },
    {
        "id": 5,
        "titulo": "Troca de mouse quebrado", 
        "prioridade": "baixa",
        "situacao": "aberto",
        "categoria": "hadware"
    },
    {
        "id": 6,
        "titulo": "Troca de Monitor", 
        "prioridade": "alta",
        "situacao": "cancelado",
        "categoria": "hadware"
    }
]

#---------------------------------------------------------------------------------------------------------------

def listar_chamados():
    print("=" * 45)
    print("          LISTAGEM GERAL DE CHAMDOS")
    print("=" * 45)

    for chamado in chamados:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Situação: {chamado['situacao']}")
        print(f"Categoria: {chamado['categoria']}")
        print("=" * 45)

#---------------------------------------------------------------------------------------------------------------

def filtar_por_situacao():
    print("=" * 45)
    print("         FILTRO POR SITUAÇÃO        ")
    print("=" * 45)

    while True:
        situacao_desejada = input("Digite a situação desejada - Ex: aberto, fechado, cancelado: ").strip().lower()

        # Condição obrigatória: Se a string estiver vazia, retorna ao input principal
        if not situacao_desejada:
            print("X Erro: O termo de busca não pode ser vazio! Tente novamente!\n")
            continue
        break

    encontrou_chamado = False
    print(f"\nBuscando chamados com status: '{situacao_desejada}'\n")

    for chamado in chamados:

        if chamado["situacao"] == situacao_desejada:
            print(f"CHAMADO N° : {chamado['id']} => {chamado['titulo']}")
            encontrou_chamado = True

    if not encontrou_chamado:
        print("Nenhum chamado encontrado com a situação informada. ")

#---------------------------------------------------------------------------------------------------------------

def atualizar_situacao():
    print("=" * 45)
    print("         ATUALIZAÇÃO DE SITUAÇÃO        ")
    print("=" * 45)

    while True:
        id_procurado = input("Digite o ID do chamado que deseja atulizar: ").strip()
        if not id_procurado.isdigit():
            print("X Erro: O campo ID não pode ficar vazio!\n")
            continue
        break
    
    while True:
        nova_situacao = input("Digite a nova situação: ").strip().lower()
        if not nova_situacao:
            print("X Erro, A situação não pode ficar vazia!\n")
            continue
        break
    
    encontrou_id = False
    for chamado in chamados:
        if chamado["id"] == int(id_procurado):
            chamado["situacao"] = nova_situacao
            encontrou_id = True
            print(f"\n Sucesso: O chamado ID {id_procurado} mudou para '{nova_situacao}'.")
            break
    if not encontrou_id:
        print(f"\nX Erro, Chamado ID {id_procurado} não encontrado.")

#---------------------------------------------------------------------------------------------------------------

def exibir_categoria():
    print("\n" + "=" * 45)
    print("         CATEGORIAS ATENDIDAS          ")
    print("=" * 45)
    
    categorias_unicas = set()
    for chamado in chamados:
        categorias_unicas.add(chamado["categoria"])

    print("Categorias mapeadas no sistema (sem duplicações): ")
    for cat in categorias_unicas:
        print(f"- {cat}")

#---------------------------------------------------------------------------------------------------------------
    
# MENU PRINCIPAL DO SISTEMA
while True:
    print("\n" + "=" * 45)
    print("       GERENCIADOR DE CHAMADOS     ")  
    print("=" * 45)
    print("1 - Listar Todos os Chamados")
    print("2 - Filtrar Chamados por Situação")
    print("3 - Atualizar Situação por ID")
    print("4 - Visualizar Categorias Atendidas (Set)")
    print("0 - Sair do Sistema")
    print("=" * 45)
    
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        listar_chamados()
    elif opcao == "2":
        filtar_por_situacao()
    elif opcao == "3":
        atualizar_situacao()
    elif opcao == "4":
        exibir_categoria()
    elif opcao == "0":
        print("\nEncerrando o istema. até logo!")
        break
    else:
        print("Opção inválida!")




