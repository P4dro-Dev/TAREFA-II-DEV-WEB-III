# 💻📊 StudyTasks — Sistema Web de Gestão de Tarefas de Estudo  

### 📚 Projeto de Desenvolvimento Web III  
**Autor:** Pedro Henrique  
**Curso:** Técnico em Informática para Internet  

---

## 💡 Sobre o Projeto  

O **StudyTasks** é um sistema web desenvolvido com **Django** que tem como objetivo auxiliar estudantes na **organização de suas tarefas de estudo**.  

O projeto foi desenvolvido aplicando os **padrões de software Front Controller e MVT (Model-View-Template)**, exigidos na disciplina **Desenvolvimento Web III**, como parte da Tarefa II.  

---

## 🧩 Estrutura do Projeto  

```
studytasks_project/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── README.md
├── studytasks_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── sistema/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── templates/
    │   └── sistema/
    │       ├── index.html
    │       ├── problema.html
    │       ├── solucao.html
    │       └── autor.html
    └── tests.py
```


---

## 🧠 Problema Identificado  

Muitos estudantes enfrentam dificuldades para **gerenciar suas tarefas e estudos**, o que pode resultar em atrasos e baixa produtividade.  
Faltava uma ferramenta simples e acessível para **organizar, visualizar e acompanhar** o progresso das atividades acadêmicas.  

---

## 💻 Solução Proposta  

O **StudyTasks** surge como uma solução para facilitar a vida do estudante, permitindo:  

✅ Listar tarefas pendentes e concluídas  
✅ Registrar novas atividades  
✅ Ter uma visão organizada do progresso dos estudos  
✅ Utilizar um sistema leve e intuitivo, acessível via navegador  

---

## ⚙️ Tecnologias Utilizadas  

| Tecnologia | Função |
|-------------|--------|
| 🐍 **Python 3.11** | Linguagem de programação principal |
| 🌐 **Django 5.0** | Framework web usado para desenvolvimento |
| 🗃️ **SQLite3** | Banco de dados leve, padrão do Django |
| 🧱 **HTML5 / CSS3** | Estrutura e estilização das páginas |
| 🔧 **Git / GitHub** | Controle de versão e hospedagem do projeto |

---

## 🧭 Padrões de Software Aplicados  

### 🔸 **Front Controller**  
Todas as requisições passam por um **único ponto de entrada**, o arquivo `studytasks_project/urls.py`, responsável por direcionar o fluxo do sistema.  

### 🔸 **MVT (Model - View - Template)**  
O sistema foi estruturado seguindo o padrão **MVT**, que separa as responsabilidades da aplicação:  

| Componente | Arquivo | Função |
|-------------|----------|--------|
| **Model** | `models.py` | Representa os dados e a lógica de negócios (classe `Tarefa`) |
| **View** | `views.py` | Processa requisições e retorna respostas usando os templates |
| **Template** | `/templates/sistema/` | Define a camada de apresentação (HTML) |

---

## 🧱 Modelagem do Sistema  

### 📄 Modelo: `Tarefa`  

| Campo | Tipo | Descrição |
|--------|------|------------|
| `titulo` | CharField | Nome da tarefa |
| `descricao` | TextField | Detalhes da tarefa |
| `concluida` | BooleanField | Indica se foi concluída ou não |

Exemplo de criação no Django Shell:  
```python
from sistema.models import Tarefa
Tarefa.objects.create(
    titulo="Estudar Django",
    descricao="Revisar o padrão MVT e criar templates.",
    concluida=False
)

