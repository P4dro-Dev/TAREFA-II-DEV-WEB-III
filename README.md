
## 📚| StudyTasks — Sistema Web de Gestão de Tarefas de Estudo

## 📝| Descrição Geral

O StudyTasks é um sistema web desenvolvido em Django, projetado para auxiliar estudantes na gestão de suas tarefas de estudo.
O sistema foi construído seguindo rigorosamente os padrões de software:

Front Controller

MVT (Model–View–Template)

Ele permite que o usuário visualize tarefas, registre novas, marque como concluídas e entenda o problema e a solução apresentada dentro do contexto do projeto.

## 🎯| Objetivo do Projeto

A proposta da Tarefa II foi criar:

```
✔ Uma aplicação Django organizada com padrões de software
✔ Estrutura completa de pastas com models, views e templates
✔ Documentação do problema, solução e autor
✔ Branch no GitHub chamada organizacao
✔ Commits e merge
✔ Relatório em PDF contendo prints e explicações
```

Este repositório contém toda a implementação do sistema StudyTasks, totalmente funcional e organizada.

## 🧩| Problema Identificado

Muitos estudantes têm dificuldades em organizar suas tarefas diárias, o que provoca:

```
Acúmulo de atividades

Esquecimento de prazos

Baixa produtividade e falta de controle dos estudos

Não havia uma ferramenta simples, prática e acessível para ajudar no acompanhamento dessas tarefas.
```

## 💡| Solução Proposta

O StudyTasks foi criado como uma solução acessível, leve e intuitiva, permitindo:

```
Registro de tarefas de estudo

Marcação de tarefas como concluídas

Remoção de tarefas

Visualização de tarefas pendentes

Documentação clara do problema, solução e autor

O sistema funciona diretamente no navegador, sem necessidade de instalação complexa.
```

## 🧭| Padrões de Software Aplicados

## 🔸 📌| Front Controller
```

Todas as requisições são encaminhadas por um único ponto de entrada:
studytasks_project/urls.py
Isso organiza o fluxo, podendo futuramente incluir autenticação, logs, tratamentos globais etc.

```

## 🔸 📌 MVT – Model, View e Template

O projeto segue a separação:

```
✔ Model (M)

Arquivo: sistema/models.py
Responsável por estruturar e manipular os dados (classe Tarefa).

✔ View (V)

Arquivo: sistema/views.py
Controla o fluxo do sistema, trata requisições e seleciona os templates corretos.

✔ Template (T)

Local: sistema/templates/sistema/
Exibe as páginas HTML renderizadas dinamicamente.

```

## 🗂️| Arquitetura do Projeto

```
studytasks_project/
│──
│── manage.py
│── db.sqlite3
│── requirements.txt
│── README.md
│
├── studytasks_project/
│   ├── settings.py
│   ├── urls.py     ← Front Controller
│   ├── wsgi.py
│   └── asgi.py
│
└── sistema/
    ├── models.py    ← Model
    ├── views.py     ← Views
    ├── urls.py
    ├── templates/
    │   └── sistema/
    │       ├── index.html
    │       ├── problema.html
    │       ├── solucao.html
    │       └── autor.html
```

## 📄 Modelagem do Sistema

```
🗃 Modelo: Tarefa
Campo	Tipo	Descrição
titulo	CharField	Nome da tarefa
descricao	TextField	Detalhes da tarefa
concluida	BooleanField	Indica se a tarefa foi concluída

```


## 🔗| Rotas do Sistema

```
URL	Template	Função
/	index.html	Lista tarefas e permite criar novas
/problema/	problema.html	Explica o problema do estudo
/solucao/	solucao.html	Mostra a solução proposta
/autor/	autor.html	Exibe nome e minicurrículo do autor
```

⚙️ Tecnologias Utilizadas

```
Tecnologia	Função
Python 3.11	Linguagem principal
Django 5.0	Framework Web
SQLite	Banco de dados
HTML5/CSS3	Interface
Git / GitHub	Controle de versão

```

🛠 Como Executar o Projeto Localmente

```
1️⃣ Clonar o repositório
git clone https://github.com/P4dro-Dev/TAREFA-II-DEV-WEB-III.git
cd TAREFA-II-DEV-WEB-III/studytasks_project
```
```
2️⃣ Criar ambiente virtual
python -m venv venv
```
```
Ativar no Windows:
venv\Scripts\activate
```
Ativar no Linux/macOS:
source venv/bin/activate
```
3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar banco de dados
python manage.py migrate

5️⃣ (Opcional) Criar superusuário
python manage.py createsuperuser

6️⃣ Executar o servidor
python manage.py runserver
```

Acesse no navegador:

👉 http://127.0.0.1:8000/

## 🧪| Testes

O projeto possui um arquivo básico:

sistema/tests.py

Que pode ser expandido futuramente com testes de modelo, requisição e validação.

🔧 Controle de Versão (Git/GitHub)

Requisitos cumpridos:

```
✔ Criação da branch organizacao
✔ Commits e push do desenvolvimento
✔ Mesclagem da branch para a principal
✔ Relatório com prints do processo
```

## 📄 Licença

```
Projeto desenvolvido exclusivamente para fins educacionais.
Livre para estudo, modificação e evolução.
```
