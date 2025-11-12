# 💻📊 StudyTasks — Sistema Web de Gestão de Tarefas de Estudo  

### 📚 Projeto de Desenvolvimento Web III  
**Discente:** Pedro Henrique  
""Docente"" Dr. Nécio 
**Curso** Técnico em Informática para Internet  

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
```
Rotas do Sistema

```
URL	Página	Descrição
/	index.html	Página inicial com as tarefas
/problema/	problema.html	Descrição do problema enfrentado
/solucao/	solucao.html	Explicação da solução proposta
/autor/	autor.html	Informações sobre o autor
```

🧰 Como Executar o Projeto
```
1️⃣ Clonar o repositório
git clone https://github.com/P4dro-Dev/TAREFA-II-DEV-WEB-III.git
cd TAREFA-II-DEV-WEB-III/studytasks_project

2️⃣ Criar o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/Mac

3️⃣ Instalar dependências
pip install -r requirements.txt

4️⃣ Criar o banco de dados
python manage.py makemigrations
python manage.py migrate

5️⃣ (Opcional) Inserir tarefa de exemplo
python manage.py shell

from sistema.models import Tarefa
Tarefa.objects.create(
    titulo="Estudar Python - Capítulo 1",
    descricao="Praticar listas e dicionários",
    concluida=False
)
exit()

6️⃣ Executar o servidor
python manage.py runserver
```

Acesse no navegador:

👉 http://127.0.0.1:8000/

🧩 Estrutura dos Padrões Implementados

Padrão	Arquivo	Responsabilidade
```
Front Controller	studytasks_project/urls.py	Centraliza o roteamento de requisições
Model (M)	sistema/models.py	Estrutura e manipula os dados
View (V)	sistema/views.py	Processa as requisições e controla o fluxo
Template (T)	sistema/templates/sistema/	Renderiza as páginas para o usuário
```

🧪 Testes

O projeto inclui um arquivo tests.py com base para futuros testes de integração e validação de modelos e views.

👨‍💻 Autor

Pedro Henrique
🎓 Estudante do curso Técnico em Informática para Internet
💼 Desenvolvedor iniciante com interesse em Web, IA e automação
📍 IFCE — Instituto Federal do Ceará

📧 E-mail acadêmico: henrique.pedro62@aluno.ifce.edu.br

🔗 Repositório do Projeto

🏆 Créditos e Licença

Projeto desenvolvido para fins educacionais, como atividade prática da disciplina Desenvolvimento Web III.

🔓 Licença livre para uso acadêmico e estudos.
