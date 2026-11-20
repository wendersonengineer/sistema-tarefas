# Sistema Web de Gestão de Tarefas

Projeto desenvolvido na disciplina de **Laboratório de Programação Back-End**, com evolução progressiva de um programa Python executado no terminal para uma aplicação web com Django e banco de dados SQLite.

**Objetivo geral:** desenvolver, a cada atividade, novas funcionalidades de cadastro, organização, consulta e atualização de tarefas e chamados, aplicando os conceitos estudados na disciplina.

---

## 🛠️ Pré-requisitos

- Python 3 instalado;
- Git instalado e configurado;
- Editor de código, como Visual Studio Code;
- Navegador web para acessar a aplicação Django.

## 🚀 Instalação e execução da versão atual

Abra o terminal na pasta `sistema-tarefas` e execute os comandos abaixo.

### 1. Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 2. Ativar o ambiente virtual

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
```

**Linux ou macOS:**

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```powershell
pip install -r requirements.txt
```

### 4. Preparar o banco de dados

```powershell
python manage.py migrate
```

### 5. Iniciar a aplicação

```powershell
python manage.py runserver
```

Acesse:

- **Página principal:** http://127.0.0.1:8000/
- **Página de apresentação:** http://127.0.0.1:8000/inicio/
- **Listagem de tarefas:** http://127.0.0.1:8000/tarefas/
- **Painel administrativo:** http://127.0.0.1:8000/admin/

> Para acessar o painel administrativo em uma instalação nova, crie um usuário com `python manage.py createsuperuser`. As atividades antigas em terminal podem ser executadas separadamente a partir dos arquivos correspondentes na pasta `exercicios_python/`.

---

## 📁 Estrutura atual do repositório

```text
sistema-tarefas/
├── .gitignore                    # Arquivos e pastas ignorados pelo Git
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação e histórico das atividades
├── manage.py                     # Gerenciamento da aplicação Django
├── db.sqlite3                    # Banco local, ignorado pelo Git
├── gestao_tarefas/               # Configurações do projeto Django
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── tarefas/                      # Aplicação de gestão de tarefas
│   ├── __init__.py
│   ├── admin.py                   # Registro dos modelos no Django Admin
│   ├── apps.py
│   ├── models.py                  # Modelos Categoria e Tarefa
│   ├── tests.py
│   ├── urls.py                    # Rotas da aplicação
│   ├── views.py                   # Views das páginas
│   ├── migrations/
│   │   └── 0001_initial.py       # Criação das tabelas iniciais
│   └── templates/
│       └── tarefas/
│           ├── home.html         # Página principal
│           ├── inicio.html       # Página de apresentação
│           └── lista.html        # Listagem de tarefas
└── exercicios_python/            # Histórico das atividades em terminal
    ├── main.py
    ├── cadastro_tarefa.py
    ├── menu_tarefas_simples.py
    ├── menu_tarefas.py
    ├── gerenciador_chamados_simples.py
    ├── gerenciador_chamados.py
    ├── chamados.py
    └── servicos.py
```

> A pasta `.venv/` é criada localmente e não deve ser versionada. A organização acima representa a estrutura desenvolvida ao longo das atividades; alguns arquivos auxiliares padrão do Django não foram detalhados.

---

# 📝 Histórico de atividades

## Atividade 1 — Estrutura inicial do projeto

### 🎯 Objetivo

Preparar o ambiente de desenvolvimento Python e iniciar a construção do Sistema de Gestão de Tarefas, organizando os primeiros arquivos e utilizando o Git para acompanhar a evolução do projeto.

### 🛠️ Desenvolvimento

Foi criado o repositório do projeto e configurado um ambiente virtual Python para isolar as dependências. O arquivo `main.py` foi utilizado como ponto de entrada inicial, apresentando uma mensagem de execução do sistema.

Essa primeira etapa permitiu conhecer a organização básica de um projeto Python, a execução de scripts pelo terminal e o registro de alterações no repositório.

### 📌 Resultado

O ambiente inicial ficou preparado para receber as funcionalidades das atividades seguintes.

---

## Atividade 2 — Cadastro de tarefas com variáveis e validações

### 🎯 Objetivo

Desenvolver um cadastro simples de tarefas, aplicando variáveis, operadores, entrada de dados e formatação de mensagens com *f-strings*.

### 🛠️ Desenvolvimento

O arquivo `cadastro_tarefa.py` foi desenvolvido para receber informações como o título e a prioridade de uma tarefa. Foram adicionadas validações básicas para evitar campos vazios e valores de prioridade inválidos.

A atividade trabalhou o recebimento de informações digitadas pelo usuário, a verificação de condições e a apresentação organizada dos dados no terminal.

### 📌 Resultado

Foi criado um cadastro inicial que demonstra como coletar, validar e exibir informações de uma tarefa em Python.

---

## Atividade 3 — Menu de tarefas e organização em funções

### 🎯 Objetivo

Criar um menu interativo para gerenciar tarefas e compreender a diferença entre uma implementação procedural e outra organizada em funções.

### 🛠️ Desenvolvimento

Foram desenvolvidas duas versões do programa:

**Versão simples — `menu_tarefas_simples.py`:** utiliza um laço `while True` para manter o menu em execução e estruturas condicionais para identificar a opção selecionada. As operações de cadastro, listagem e atualização foram implementadas diretamente no fluxo principal.

**Versão modular — `menu_tarefas.py`:** separa as operações em funções, tornando o código mais organizado e facilitando sua leitura, manutenção e reutilização.

### 📌 Resultado

As duas versões permitiram comparar formas diferentes de estruturar um programa, demonstrando a importância da modularização à medida que o sistema cresce.

---

## Atividade 4 — Gerenciador de chamados internos

### 🎯 Objetivo

Desenvolver um protótipo de gerenciamento de chamados de suporte técnico, utilizando listas, dicionários, estruturas condicionais, funções e conjuntos (`set`).

### 🛠️ Desenvolvimento

A atividade foi realizada em duas versões:

**Versão simples — `gerenciador_chamados_simples.py`:** implementa as operações diretamente no menu principal, com cadastro e listagem de chamados, filtro por situação, atualização por identificador e visualização de categorias.

**Versão modular — `gerenciador_chamados.py`:** reorganiza essas operações em funções, separando a lógica de cada funcionalidade.

Os chamados são representados por dicionários armazenados em uma lista. Cada registro contém informações como identificador, título, prioridade, situação e categoria. O conjunto `set` é utilizado para apresentar categorias sem repetição.

### 🚀 Execução

Na pasta que contém os exercícios, execute:

```powershell
python gerenciador_chamados.py
```

### 📊 Exemplos de uso e saída do terminal

**Menu principal:**

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

**Listagem de chamados:**

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

**Filtro por situação — com resultados:**

```text
Digite a situação desejada - Ex: aberto, fechado, cancelado: aberto
Buscando chamados com status: 'aberto'
CHAMADO N° : 1 => Sem acesso ao sistema interno
CHAMADO N° : 3 => Internet instável no setor comercial
CHAMADO N° : 5 => Troca de mouse quebrado
```

**Filtro por situação — sem resultados:**

```text
Digite a situação desejada - Ex: aberto, fechado, cancelado: reaberto
Buscando chamados com status: 'reaberto'
Nenhum chamado encontrado com a situação informada.
```

**Atualização de um chamado existente:**

```text
Digite o ID do chamado que deseja atualizar: 3
Digite a nova situação: fechado
Sucesso: O chamado ID 3 mudou para 'fechado'.
```

**Tentativa de atualização de um ID inexistente:**

```text
Digite o ID do chamado que deseja atualizar: 99
Digite a nova situação: fechado
X Erro: Chamado ID 99 não encontrado.
```

**Categorias sem duplicações:**

```text
=============================================
          CATEGORIAS ATENDIDAS
=============================================
Categorias mapeadas no sistema (sem duplicações):
- rede
- acesso
- hardware
```

### 📌 Resultado

O programa passou a oferecer funcionalidades de consulta e atualização de chamados, além de demonstrar a utilização de diferentes coleções de dados e a organização das operações em funções.

---

## Atividade 5 — Refatoração com POO, módulos e arquitetura em camadas

### 🎯 Objetivo

Refatorar o gerenciador de chamados desenvolvido anteriormente, aplicando os conceitos de Programação Orientada a Objetos (POO) e separação de responsabilidades entre módulos.

### 🛠️ Desenvolvimento

O sistema foi reorganizado em três arquivos principais:

- **`chamados.py` — Modelo:** contém a classe `Chamado`, responsável por representar os dados e os estados do chamado. Foram utilizados métodos de transição de situação, como `atender()`, `concluir()`, `fechar()` e `reabrir()`, além de métodos de apresentação como `__str__()` e `resumo_linha()`.
- **`servicos.py` — Regras de negócio:** reúne as operações de cadastro, busca por ID, atualização, listagem, filtros por situação e prioridade, levantamento de categorias e estatísticas.
- **`main.py` — Interface de terminal:** apresenta o menu interativo, recebe as entradas do usuário e utiliza os demais módulos para executar as funcionalidades. Também realiza a inicialização de chamados de demonstração.

A divisão do código permitiu reduzir a concentração de responsabilidades em um único arquivo e tornar a aplicação mais fácil de compreender e manter.

### 📌 Resultado

O projeto passou de uma estrutura procedural para uma organização modular, com representação dos chamados por objetos e separação entre interface e regras de negócio.

---

## Atividade 6 — Hands-on: primeira interface web com Django

### 🎯 Objetivo

Transformar o Sistema de Gestão de Tarefas, anteriormente executado pelo terminal, em uma aplicação web utilizando Django. A atividade teve como foco compreender a arquitetura MVT (*Model-View-Template*), o roteamento de URLs, as views e a renderização de templates HTML.

### 🛠️ Desenvolvimento

Inicialmente, o framework Django foi instalado e configurado. Foram criados o projeto `gestao_tarefas` e a aplicação `tarefas`, que concentra as funcionalidades do sistema.

No arquivo `gestao_tarefas/settings.py`, a aplicação foi registrada em `INSTALLED_APPS`. As URLs foram organizadas em `gestao_tarefas/urls.py` e `tarefas/urls.py`, permitindo separar o roteamento geral das rotas específicas da aplicação.

No arquivo `tarefas/views.py`, foram implementadas as funções `home`, `inicio` e `lista_tarefas`. Cada view recebe uma requisição e utiliza `render()` para apresentar a página correspondente no navegador.

### 🖥️ Páginas desenvolvidas

**1. Página principal — `home.html`**

É a entrada do sistema, acessada pelo endereço `/`. Apresenta a identidade visual da aplicação e oferece caminhos para acessar as demais páginas.

**2. Página de apresentação — `inicio.html`**

É acessada por `/inicio/`. Apresenta informações introdutórias sobre o sistema e opções de navegação para a página principal e a listagem de tarefas.

**3. Página de listagem — `lista.html`**

É acessada por `/tarefas/`. Exibe o título, a prioridade e a situação das tarefas. Na Atividade 6, os dados eram definidos temporariamente em uma lista de dicionários Python na view, sem gravação no banco de dados.

As três páginas receberam uma identidade visual padronizada, com tons suaves de azul, cartões informativos e elementos de navegação, buscando oferecer uma interface organizada e agradável.

### 🏗️ Organização MVT

- **Model:** representa a estrutura dos dados; sua implementação com persistência foi desenvolvida na atividade seguinte.
- **View:** recebe a requisição, prepara as informações e escolhe o template que será apresentado.
- **Template:** organiza a apresentação visual dos dados em páginas HTML.

Essa separação ajuda a manter as responsabilidades da aplicação organizadas.

### 🚀 Execução e testes

O servidor de desenvolvimento foi iniciado com:

```powershell
python manage.py runserver
```

As páginas foram verificadas no navegador pelos endereços `/`, `/inicio/` e `/tarefas/`, observando o funcionamento das rotas, a navegação e a apresentação dos dados.

### 📌 Resultado

A atividade marcou a passagem do projeto em terminal para uma aplicação web com Django. Foram implementadas três páginas integradas por rotas e views, criando a base necessária para adicionar persistência de dados na Semana 7.

---

## Atividade 7 — Hands-on: persistindo tarefas e categorias com Django

### 🎯 Objetivo

Implementar o armazenamento permanente de categorias e tarefas utilizando os models do Django e o banco de dados SQLite. Também foram previstos o gerenciamento dos registros pelo Django Admin e a realização de consultas e atualizações por meio do ORM (*Object-Relational Mapper*).

### 🛠️ Desenvolvimento

**1. Criação dos models**

No arquivo `tarefas/models.py`, foram criados dois modelos:

- **`Categoria`:** possui o campo `nome`, utilizado para identificar e organizar as categorias disponíveis.
- **`Tarefa`:** possui os campos `titulo`, `descricao`, `prioridade`, `data_prevista`, `situacao` e `categoria`.

A prioridade utiliza opções como **Baixa**, **Média** e **Alta**, enquanto a situação pode ser **Pendente** ou **Concluída**. O relacionamento entre `Tarefa` e `Categoria` foi implementado com uma chave estrangeira (`ForeignKey`), utilizando `on_delete=models.PROTECT` para impedir a exclusão de uma categoria vinculada a tarefas.

**2. Criação e aplicação das migrações**

Após definir os modelos, foram executados os comandos:

```powershell
python manage.py makemigrations
python manage.py migrate
```

O primeiro comando gerou a migração `tarefas/migrations/0001_initial.py`, responsável pela criação dos modelos `Categoria` e `Tarefa`. O segundo aplicou a migração ao SQLite, com a confirmação `Applying tarefas.0001_initial... OK`.

**3. Configuração do Django Admin**

Os dois modelos foram registrados no arquivo `tarefas/admin.py`, permitindo o gerenciamento dos registros pela interface administrativa do Django.

Foi utilizado um usuário administrador para acessar o painel. As categorias **Estudos** e **Pessoal** foram cadastradas pelo Django Admin.

**4. Cadastro de tarefas**

A atividade prevê o cadastro de pelo menos duas tarefas associadas às categorias, incluindo uma tarefa com situação pendente. Esse cadastro deve ser conferido no painel administrativo antes de registrar sua conclusão.

### 🔎 Consultas e atualizações com ORM

Para acessar o ambiente interativo do Django, utiliza-se:

```powershell
python manage.py shell
```

Em seguida, os modelos podem ser importados:

```python
from tarefas.models import Categoria, Tarefa
```

**Listar todas as tarefas:**

```python
Tarefa.objects.all()
```

**Filtrar tarefas pendentes:**

```python
Tarefa.objects.filter(situacao="PENDENTE")
```

**Ordenar pela data prevista:**

```python
Tarefa.objects.order_by("data_prevista")
```

**Atualizar uma tarefa pendente para concluída:**

```python
tarefa = Tarefa.objects.filter(situacao="PENDENTE").first()
if tarefa is not None:
    tarefa.situacao = "CONCLUIDA"
    tarefa.save()
```

Os comandos acima estão documentados como roteiro de execução. **Os resultados dessas consultas e da atualização ainda precisam ser confirmados e registrados.**

### 💾 Verificação da persistência

Após cadastrar e atualizar os registros, o servidor deverá ser reiniciado e os dados conferidos novamente no Django Admin ou no shell. Esse procedimento permite verificar se as informações foram realmente gravadas no banco SQLite.

**Situação:** validação final pendente de confirmação.

### ⚠️ Dificuldade encontrada e solução

Durante a configuração do acesso ao Django Admin, foi necessário redefinir a senha do usuário `admin`, pois a senha anterior não estava disponível. A primeira tentativa de alteração apresentou avisos relacionados aos requisitos de segurança da senha.

A situação foi resolvida executando:

```powershell
python manage.py changepassword admin
```

Após informar uma senha que atendesse às exigências de segurança do Django, a alteração foi concluída.

### 📌 Resultado parcial

Os modelos `Categoria` e `Tarefa` foram criados, a migração inicial foi aplicada com sucesso e os modelos foram registrados no Django Admin. As categorias iniciais foram cadastradas. Permanecem para conferência final o cadastro das tarefas, a execução documentada das consultas ORM, a atualização de uma situação e a verificação da persistência após reiniciar o servidor.

## 📌 Evidência de Entrega

A entrega da Atividade 7 será realizada por meio de um commit no repositório GitHub, contendo as implementações desenvolvidas no projeto Django.

O commit incluirá os models `Categoria` e `Tarefa`, os arquivos de migração, o registro dos modelos no Django Admin e a documentação atualizada.

**Repositório:** https://github.com/wendersonengineer/sistema-tarefas

**Mensagem prevista para o commit:**

`feat: implementa persistencia de tarefas e categorias com Django ORM`
> O arquivo `db.sqlite3` está ignorado pelo Git. Por isso, os registros locais não são enviados ao repositório; as migrações e a documentação permitem reproduzir a estrutura do banco em outro ambiente.

---

## 📌 Controle da evolução do projeto

| Atividade | Conteúdo principal | Situação |
|---|---|---|
| 1 | Configuração inicial do projeto Python | Desenvolvida |
| 2 | Cadastro e validação de tarefas | Desenvolvida |
| 3 | Menu interativo e funções | Desenvolvida |
| 4 | Gerenciador de chamados e coleções | Desenvolvida |
| 5 | POO e separação em módulos | Desenvolvida |
| 6 | Interface web com Django e templates | Desenvolvida |
| 7 | Models, migrações, Admin e ORM | Implementação principal realizada; validações finais pendentes |

---

## 👥 Identificação de autoria

- **Desenvolvedor:** Wenderson Luís dos Santos
- **RA:** 202422912
- **Curso:** Engenharia de Software
- **Disciplina:** Laboratório de Programação Back-End

---

*Este README registra a evolução das atividades da disciplina. As funcionalidades e os testes são descritos conforme as etapas efetivamente desenvolvidas e confirmadas.*
