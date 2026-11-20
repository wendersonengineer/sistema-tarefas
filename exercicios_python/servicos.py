from chamados import Chamado

# --- CADASTRO E BUSCA ---

def cadastrar_chamado(chamados, titulo, descricao, prioridade, categoria, solicitante):
    """Cria uma nova instância de Chamado e adiciona à lista."""
    novo_chamado = Chamado(titulo, descricao, prioridade, categoria, solicitante)
    chamados.append(novo_chamado)
    return novo_chamado


def busca_chamado_por_id(chamados, id_procurado):
    """Busca um chamado pelo ID. Retorna o objeto Chamado ou None."""
    for c in chamados:
        if c.id == id_procurado:
            return c
    return None


# --- ATUALIZAÇÃO E EXCLUSÃO ---

def atualizar_situacao_chamado(chamado, nova_opcao, dado_extra=""):
    """
    Atualiza a situação do chamado com base na opção selecionada.
    dado_extra: Nome do técnico (opção 1) ou Descrição da solução (opção 2).
    """
    if nova_opcao == "1":
        chamado.atender(dado_extra if dado_extra else "Técnico Não Informado")
        return True
    elif nova_opcao == "2":
        chamado.concluir(dado_extra if dado_extra else "Solução Não Detalhada")
        return True
    elif nova_opcao == "3":
        chamado.fechar()
        return True
    elif nova_opcao == "4":
        chamado.reabrir()
        return True
    return False  # Opção inválida


def excluir_chamado(chamados, id_procurado):
    """Remove um chamado da lista pelo ID."""
    chamado = busca_chamado_por_id(chamados, id_procurado)
    if chamado:
        chamados.remove(chamado)
        return True
    return False


# --- LISTAGENS E FILTROS ---

def listar_chamados(chamados):
    """Exibe todos os chamados em formato de lista simplificada."""
    if not chamados:
        print("\nNenhum chamado cadastrado no sistema.")
        return

    print("\n-------------------------------- LISTA DE CHAMADOS --------------------------------\n")
    for c in chamados:
        print(c.resumo_linha())
    print("\n-----------------------------------------------------------------------------------")


def filtrar_por_situacao(chamados, opcao_situacao):
    """Filtra chamados com base no código da situação."""
    situacoes = {
        "1": "Aberto",
        "2": "Em Atendimento",
        "3": "Concluído",
        "4": "Fechado",
        "5": "Reaberto"
    }

    status = situacoes.get(opcao_situacao)
    if not status:
        print("\nOpção inválida! Escolha um número de 1 a 5.")
        return

    encontrou = False
    print(f"\n--- CHAMADOS COM SITUAÇÃO: {status} ---")

    for c in chamados:
        if c.situacao == status:
            print(c.resumo_linha())
            encontrou = True

    if not encontrou:
        print(f"Nenhum chamado encontrado como '{status}'.")


def filtrar_por_prioridade(chamados, prioridade_desejada):
    """Filtra chamados pela prioridade (Baixa, Média, Alta, Crítica)."""
    encontrou = False
    print(f"\n--- CHAMADOS COM PRIORIDADE: {prioridade_desejada.upper()} ---")

    for c in chamados:
        if c.prioridade.lower() == prioridade_desejada.lower():
            print(c.resumo_linha())
            encontrou = True

    if not encontrou:
        print(f"Nenhum chamado encontrado com a prioridade '{prioridade_desejada}'.")


def obter_categorias_unicas(chamados):
    """Exibe todas as categorias cadastradas sem duplicatas."""
    if not chamados:
        print("\nNenhum chamado cadastrado.")
        return

    categorias = set(c.categoria for c in chamados)
    print("\n--- CATEGORIAS ATENDIDAS NO SISTEMA ---")
    for cat in sorted(categorias):
        print(f". {cat}")


# --- RELATÓRIOS ---

def gerar_relatorios_estatistico(chamados):
    """Gera um resumo quantitativo do sistema."""
    if not chamados:
        print("\nNão há dados suficientes para gerar relatório.")
        return

    total = len(chamados)
    abertos = sum(1 for c in chamados if c.situacao == "Aberto")
    em_atendimento = sum(1 for c in chamados if c.situacao == "Em Atendimento")
    concluidos = sum(1 for c in chamados if c.situacao == "Concluído")
    fechados = sum(1 for c in chamados if c.situacao == "Fechado")
    reabertos = sum(1 for c in chamados if c.situacao == "Reaberto")

    criticos = sum(1 for c in chamados if c.prioridade.lower() in ["alta", "crítica", "critica"])

    print("\n=========================================")
    print("      PAINEL ESTATÍSTICO DE CHAMADOS     ")
    print("=========================================")
    print(f" Total de Chamados Registrados : {total}")
    print(f" • Abertos                    : {abertos}")
    print(f" • Em Atendimento             : {em_atendimento}")
    print(f" • Concluídos                 : {concluidos}")
    print(f" • Fechados                   : {fechados}")
    print(f" • Reabertos                  : {reabertos}")
    print("-----------------------------------------")
    print(f" Chamados de Alta/Crítica Urgência: {criticos}")
    print("=========================================")