# Sistema Web de Gestão de Tarefas

Projeto inicial para organização de tarefas.

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
|____ .gitignore        # Filtro de arquivos do Git
|____ README.md         # Instruções de execução
|____ main.py           # Script principal do sistema
|____ requirements.txt  # Listagem de dependências
|____ .venv/ # local;   # Local; não versionada (omitida pelo .gitignore)

```
