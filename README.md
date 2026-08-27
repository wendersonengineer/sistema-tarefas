# Sistema Web de Gestão de Tarefas

Projeto desenvolvido na disciplina de Back-End.
**Objetivo:** Criar um sistema simples de tarefas em Python, evoluindo em etapas.

---

## 🛠️ Pré-requisitos
* Python 3 instalado
* Git configurado localmente

---

## 🚀 Fluxo de Execução (Passo a Passo)

Siga as etapas abaixo no terminal para inicializar e rodar a aplicação:

### 1. Ambiente Virtual (venv)
Crie o ambiente isolado para o projeto:
```bash
python -m venv .venv
```

### 2. Ative o ambiente conforme o seu sistema operacional:
* **Linux / MacOS:** 
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell):** 
  ```bash
  .venv\Scripts\Activate.ps1
  ```

### 3. Instalar as dependências
```bash
pip install requests
pip freeze > requirements.txt
```

### 4. Executar o script principal
Execute o script principal do sistema:
```bash
python main.py
```

---

## 📁 Estrutura do Repositório

```text

sistema-tarefas/
|
├── .venv/
├── .gitignore
├── main.py
├── cadastro_tarefa.py
├── menu_tarefas_simples.py
├── menu_tarefas.py
├── gerenciador_chamados_simples.py
├── gerenciador_chamados.py
├── requirements.txt
└── README.md

```

---

## 📝 Histórico de Atividades

### Atividade 1 - Estrutura Inicial
* **Arquivo:** `main.py`
* **Função:** Exibir mensagem inicial do sistema.

## 👥 Identificação de Autoria
* **Desenvolvedor:** Wenderson Luís dos Santos
* **RA:** 202422912

---

### Atividade 2 - Cadastro de Tarefas
* **Arquivo:** `cadastro_tarefa.py`
* **Função:** Permitir o registro de tarefas com título e prioridade. Inclui validações básicas para evitar campos vazios ou valores inválidos.

## 👥 Identificação de Autoria
* **Desenvolvedor:** Wenderson Luís dos Santos
* **RA:** 202422912

---

### Atividade 3 - Menu de Tarefas

#### Versão Simples (Sem Funções)
* **Arquivo:** `menu_tarefas_simples.py`
* **Descrição:** 
  * Menu implementado diretamente no loop `while True`.
  * Lógicas separadas para cadastrar, listar e atualizar tarefas.

#### Versão Avançada (Com Funções)
* **Arquivo:** `menu_tarefas.py`
* **Descrição:**
  * Menu principal chama cada função conforme a opção escolhida.
  * Estrutura mais organizada e fácil de manter.

## 👥 Identificação de Autoria
* **Desenvolvedor:** Wenderson Luís dos Santos
* **RA:** 202422912

---

#### Atividade 4 - Gerenciador de Chamados Internos

# Gerenciador de Chamados Internos
#### Versão Simples (Sem Funções)
* **Arquivo:** `gerenciador_chamados_simples.py`
* **Descrição:** 
  * Protótipo interativo de suporte técnico focado em conceitos de back-end.
  * Menu estruturado diretamente no laço de repetição `while True`.
  * Lógicas completas para listagem, filtragem por situação e atualização por ID.
  * Mapeamento de categorias exclusivas sem duplicações utilizando conjuntos (`set`).

#### Versão Avançada (Com Funções)
* **Arquivo:** `gerenciador_chamados.py`
* **Descrição:**
  * Refatoração completa modularizando as operações de backend.
  * Cada funcionalidade (listar, filtrar, atualizar e mapear) isolada em funções (`def`) dedicadas.
  * Uso de conjunto (`set`) para extrair e exibir categorias únicas sem duplicações.


## 🎯 Objetivo do Programa
Desenvolver um protótipo em terminal focado em sistemas back-end para gerenciar chamados de suporte técnico de uma empresa. O sistema armazena os registros em uma lista de dicionários e implementa de forma linear (sem o uso de funções) as operações de listagem geral estruturada, filtragem por situação com validação de buscas vazias ou sem resultado, atualização de status por ID único (com proteção contra entrada de letras) e mapeamento de categorias exclusivas utilizando conjuntos (`set`).

---

## 🚀 Comando para Execução

Certifique-se de estar com o seu ambiente virtual ativo no terminal e execute o script principal do projeto:

```bash
python gerenciador_chamados.py
```

---

## 📊 Exemplos de Uso e Saída do Terminal

### Menu Principal
```text
=============================================
       GERENCIADOR DE CHAMADOS     
=============================================
1 - Listar Todos os Chamados
2 - Filtrar Chamados por Situação
3 - Atualizar Situação por ID
4 - Visualizar Categorias Atendidas (Set)
0 - Sair do Sistema
=============================================
Escolha uma opção:
```

### Opção 1: Listagem Geral
```text
=============================================
          LISTAGEM GERAL DE CHAMADOS
=============================================
ID: 1
Título: Sem acesso ao sistema interno
Prioridade: alta
Situação: aberto
Categoria: acesso
=============================================
ID: 2
Título: Impressora sem conexão
Prioridade: média
Situação: em atendimento
Categoria: hardware
=============================================
```

### Opção 2: Filtro por Situação (Com resultados)
```text
Digite a situação desejada - Ex: aberto, fechado, cancelado: aberto

Buscando chamados com status: 'aberto'

CHAMADO N° : 1 => Sem acesso ao sistema interno
CHAMADO N° : 3 => Internet instável no setor comercial
CHAMADO N° : 5 => Troca de mouse quebrado
```

### Opção 2: Filtro por Situação (Sem resultados)
```text
Digite a situação desejada - Ex: aberto, fechado, cancelado: reaberto

Buscando chamados com status: 'reaberto'

Nenhum chamado encontrado com a situação informada.
```

### Opção 3: Atualizar Situação por ID (ID existente)
```text
=============================================
         ATUALIZAÇÃO DE SITUAÇÃO        
=============================================
Digite o ID do chamado que deseja atualizar: 3
Digite a nova situação: fechado

Sucesso: O chamado ID 3 mudou para 'fechado'.
```

### Opção 3: Atualizar Situação por ID (ID inexistente)
```text
=============================================
         ATUALIZAÇÃO DE SITUAÇÃO        
=============================================
Digite o ID do chamado que deseja atualizar: 99
Digite a nova situação: fechado

X Erro: Chamado ID 99 não encontrado.
```

### Opção 4: Visualizar Categorias Atendidas (Uso do `set()`)
```text
=============================================
         CATEGORIAS ATENDIDAS          
=============================================
Categorias mapeadas no sistema (sem duplicações):
- rede
- acesso
- hardware
```

---

## 👥 Identificação de Autoria
* **Desenvolvedor:** Wenderson Luís dos Santos
* **RA:** 202422912
