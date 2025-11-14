# StudyTasks — Sistema Web de Gestão de Tarefas de Estudo

**Discente:** Pedro Henrique  
**Docente:** Dr. Nécio Veras

## Sobre o projeto
StudyTasks é um sistema web em Django para auxiliar estudantes a organizar tarefas de estudo.
O projeto aplica os padrões **Front Controller** e **MVT** conforme solicitado na atividade II — Desenvolvimento Web III.

## Estrutura do repositório
```
studytasks_project/
├── manage.py
├── requirements.txt
├── studytasks_project/
│   └── settings.py, urls.py, wsgi.py, asgi.py
└── sistema/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── templates/sistema/
```

## Como executar (resumo)
1. Crie e ative um ambiente virtual (Python 3.11 recomendado).
2. Instale dependências: `pip install -r requirements.txt`
3. Crie o banco: `python manage.py migrate`
4. Crie superuser (opcional): `python manage.py createsuperuser`
5. Execute: `python manage.py runserver`
6. Acesse: http://127.0.0.1:8000/

## Padrões aplicados
- **Front Controller:** `studytasks_project/urls.py` centraliza o roteamento.
- **MVT:** `sistema/models.py` (Model), `sistema/views.py` (Views), `templates/sistema/*.html` (Templates).

## Rotas principais
- `/` — Página inicial (listar e criar tarefas)
- `/problema/` — Descrição do problema
- `/solucao/` — Descrição da solução
- `/autor/` — Informações do autor

## Git (branch e merge)
Recomenda-se criar uma branch `organizacao`, commitar as alterações e, após testes, mesclar na branch principal (`main` ou `master`).

## Créditos
Projeto desenvolvido como atividade prática da disciplina Desenvolvimento Web III.
