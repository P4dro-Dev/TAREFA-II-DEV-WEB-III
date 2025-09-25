 ## Projeto API Django
# Sobre o Projeto
Este é um projeto simples de API desenvolvido com o framework Django para demonstrar a criação e organização de código web. Ele implementa um único endpoint que aceita uma requisição POST e retorna uma saudação personalizada em formato JSON.
 
 # O projeto foi construído seguindo os padrões de software MVT (Model-View-Template) e FrontController para garantir uma estrutura organizada e escalável.

# Funcionalidades
Endpoint /api/hello/ que processa dados enviados no corpo da requisição.

# Recebe um nome (em JSON) e retorna uma saudação no formato: {"message": "Hello, [Nome]!"}.

# Verifica se o método da requisição é POST e se o JSON é válido.

# Padrões de Projeto
MVT (Model-View-Template): A arquitetura do projeto separa as responsabilidades.

# Model: Não utilizado neste projeto simples, mas a estrutura está pronta para futuros modelos de dados.

# View: O arquivo hello/views.py contém a lógica que processa a requisição.

# Template: Não utilizado, pois a resposta é em JSON.

# FrontController: O arquivo meu_projeto_django_api/urls.py atua como um controlador central, direcionando as requisições para o aplicativo (app) correto (hello), que então lida com a lógica específica.

# Estrutura de Pastas
meu_projeto_django_api/
├── manage.py
├── meu_projeto_django_api/
│   ├── settings.py
│   ├── urls.py  # FrontController
│   └── ...
├── hello/ # Aplicativo 'hello'
│   ├── migrations/
│   ├── views.py  # Lógica da API
│   └── ...
└── db.sqlite3

# Como Executar o Projeto
Pré-requisitos: Certifique-se de ter o Python e o Django instalados.

# Abra o terminal na pasta raiz do projeto.

Aplique as migrações para criar o banco de dados inicial:

Bash

python manage.py migrate
Inicie o servidor de desenvolvimento:

Bash

python manage.py runserver
O servidor estará disponível em http://127.0.0.1:8000/.

# Como Testar a API
Com o servidor rodando, abra um novo terminal e use o comando curl para enviar uma requisição POST para o endpoint da API:

Bash

curl -X POST http://127.0.0.1:8000/api/hello/ \
-H "Content-Type: application/json" \
-d '{"name": "SeuNome"}'
A resposta esperada será um JSON com a mensagem de saudação 
