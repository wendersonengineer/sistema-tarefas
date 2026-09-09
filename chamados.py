from datetime import datetime

class Chamado:
    # Contador de classe para gerar IDs automáticos e sequenciais
    _proximo_id = 1

    def __init__(self, titulo, descricao, prioridade, categoria, solicitante):
        self.id = Chamado._proximo_id
        Chamado._proximo_id += 1

        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade  # Baixa, Média, Alta, Crítica
        self.categoria = categoria    # Hardware, Redes, Software, etc.
        self.solicitante = solicitante

        # Controle de estado do chamado
        self.situacao = "Aberto"
        self.tecnico = "Não atribuído"
        self.solucao = "Pendente"
        self.data_abertura = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.data_fechamento = "-"

    # --- MÉTODOS DE TRANSIÇÃO DE ESTADO ---

    def atender(self, nome_tecnico):
        """Atribui o chamado a um técnico e altera a situação."""
        self.tecnico = nome_tecnico if nome_tecnico else "Não atribuído"
        self.situacao = "Em Atendimento"

    def concluir(self, descricao_solucao):
        """Registra a solução técnica e marca como concluído."""
        self.solucao = descricao_solucao if descricao_solucao else "Solução não detalhada"
        self.situacao = "Concluído"

    def fechar(self):
        """Encerra o chamado e registra a data/hora final."""
        self.situacao = "Fechado"
        self.data_fechamento = datetime.now().strftime("%d/%m/%Y %H:%M")

    def reabrir(self):
        """Reabre um chamado encerrado para novo atendimento."""
        self.situacao = "Reaberto"
        self.data_fechamento = "-"

    # --- MÉTODOS DE FORMATAÇÃO E EXIBIÇÃO ---

    def resumo_linha(self):
        """Formatação compacta de 1 linha para listagens/tabelas."""
        return f"[#{self.id:03d}] [{self.prioridade.upper():^7}] [{self.situacao:^15}] - {self.titulo} (Solicitante: {self.solicitante})"

    def __str__(self):
        """Formatação detalhada para exibição individual do chamado."""
        return (
            f"==========================================\n"
            f" CHAMADO #{self.id:03d} - {self.titulo.upper()}\n"
            f"==========================================\n"
            f" Situação         : {self.situacao}\n"
            f" Prioridade       : {self.prioridade}\n"
            f" Categoria        : {self.categoria}\n"
            f" Solicitante      : {self.solicitante}\n"
            f" Técnico Resp.    : {self.tecnico}\n"
            f" Data Abertura    : {self.data_abertura}\n"
            f" Data Fechamento  : {self.data_fechamento}\n"
            f"------------------------------------------\n"
            f" Descrição        : {self.descricao}\n"
            f" Solução          : {self.solucao}\n"
            f"=========================================="
        )