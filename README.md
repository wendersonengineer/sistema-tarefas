# Sistema Web de Gestão de Tarefas

Projeto desenvolvido na disciplina de Back-End.
Objetivo: criar um sistema simples de tarefas em python, evoluindo em etapas.

---

## Pré-requisito
* Python 3 instalado
* Git configurado localmente

## Fluxo de Execução (Passo a Passo)

Siga as etapas abaixo no terminal para inicializar e rodar a aplicação:

### 1. Ambiente Virtual (venv)
Crie o ambiente isolado para o projeto:
```bash
python -m venv .venv
```


### 2. Ative o ambiente conforme o seu sistema operacional:
* **Linux / MacOS:** `source .venv/bin/activate`
* **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`


### 3. Instalar as dependências
```bash
pip install requests
pip freezer > requirements.txt
```


### 4. Executar o script principal
Execute o script principal do sistema:
```bash
python main.py
```

---

## Estrutura do Repositório

```
sistema-tarefas/
|
|____ .venv/                        # local - não versionada (omitida pelo .gitignore)
|____ main.py                       # Atividade 1 - mensagem inicial
|____ cadastro_tarefa.py            # Atividade 2 - cadastroo simples
|____ cadastro_tarefas_simples.py   # Atividade 3 - menu sem funções
|____ cadastro_tarefas.py           # Atividade 3 - menu com funções
|____ requirements.txt              # Listagem de dependências
|____ .gitignore                    # Filtro de arquivos do Git
|____ README.md                     # Documentação completa

```
---

## Atividade 1 - estrutura inicial
Arquivo: `main.py`
Função: exibir mensagem inicial do sistema.

---

## Atividade 2 - Cadastro de tarefas
Arquivo: cadastro_tarefa.py
Função: permitir o registro de tarefas com título e prioridade.
Incluir validações ásicas para evitar campos vazios ou valores inválidos.

---

## Atividade 3 - Menu de tarefas

### Versão simples (sem funções)
Arquivo: `menu_tarefas_simples.py`
- Menu impplementado diretamente no loop 'while True'.
- Lógica separadas para cadastrar, listar e atualizar tarefas.
- Menu principal chama cada função conforme a opção escolhida.
- Estrutura mais organizada e fácil de manter.

---

## Execução
Noterminal:
```bash
python main.py




