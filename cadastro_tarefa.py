# Passo a passo
# 1. Crie um diretório do repositório, crie um arquivo:
# cadastro_tarefas.py

# 2. Escreva o cabeçalho de execução
# Apresente uma mensagem inicial para torna a interaçào clara:
print("=== CADASTRO DE TAREFAS ===")

# 3. Leia o título
# Como o título é texto, ele pode ser armazenado diretamente:
titulo = input("Digite o título da tarefa: ")

# 4. Leia e converta os dados numéricos
# Lembre-se de que input () retorna texto. Faça a conversão no momento da leitura:
prioridade = int(input("Prioridade (1 a 5): "))
prazo_horas = float(input("Prazo estimado em horas: "))

# 5. Registre a urgência
# Solicite uma resposta simples e gere um booleano por comparação:
resposta_urgencia = input ("A tarefa é urgente? ([sim] / [nao]): ")
urgente = resposta_urgencia == "sim"

# 6. Implemente o cálculo e as expressões
# Defina um fator de esforço e calcule a estimativa. em seguida, crie uma comparação e uma expressão lógica:
fator_esforco = 1.2
esforco_estimado = prazo_horas * fator_esforco

prioridade_alta = prioridade >= 4
prioritaria = prioridade_alta or urgente

# 7. Exiba o resumo da tarefa
# Use f- strings para mostrar os dados com clareza:
print("\n=== RESUMO DA TAREFA ===")
print(f"Título: {titulo}")
print(f"Prioridade: {prioridade}")
print(f"Prazo informado: {prazo_horas:.2f} horas")
print(f"Esforço estimado: {esforco_estimado:.2f} horas")
print(f"Urgente: {urgente}")
print(f"Prioridade alta: {prioridade_alta}")
print(f"Deve ser tratada como prioritária: {prioritaria}")

# 8. execute e teste
# Execute o programa no terminal
# python cadastro_tarefa.py
# Teste os cenários:

'''
-------------------------------------------------------------------------
    Cenário        |   Prioridade    | Prazo  | Urgente    | Resultado 
                                                            esperado para 
                                                            prioritaria 
-------------------------------------------------------------------------
Tarefa
planejada           |   2            | 6.5     | nao       | False
------------------------------------------------------------------------
Correção crítica    |   3            | 1.5     | sim       | True
-------------------------------------------------------------------------

'''

'''
Entregável
O repositório deve conter o arquivo cadastro_tarefa.py executável, com:

. Leitura de título, prioridade, prazo e urgência.
. Variáveis com nomes claros.
. Conversão de prioridade com int().
. Conversão de prazo com float().
. Pelo menos uma operação aritmética.
. Pelo menos uma comparação relacional.
. Pelo menos uma expressão lógica.
. Saída formatada com f-strings.    
. Commit descrito registrando a implamentação. 

'''


