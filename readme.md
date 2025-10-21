# Início do Projeto - Magazine API
Requisitos para rodar a API (o que eu usei):
## Requiriments
+ [Python 3.12.7](https://www.python.org/downloads)
+ [Django 5.2.7](https://www.djangoproject.com/download)
+ Postman/Bruno (ou uma plataforma de testes para API's)
    
Libs:
+ <span style="color: #00ff6aff">django rest_framework</span>

How to install:

    python -m pip install djangorestframework
+ SQLite Viewer (VSCode Extensions)
+ VSCode (Ou Outro IDLE)
## Como Rodar o projeto?
No terminal do projeto:

    python manage.py runserver
## Como funciona?
Essa API foi feita para um Desafio Backend da Magazine Luiza, onde eles solicitam uma API REST para a criação, edição e remoção de salas, com um sistema de agendamento, onde poderia fazer o mesmo que as salas, contando com um banco de dados para isso, eu quis fazer para este projeto um sistema de login também onde conta com o úsuario poder criar salas e agendamentos. Estou usando no banco de dados de Agendamentos que recebe uma tabela relacional à <span style="color: #f0b000ff">Salas</span> e aos <span style="color: #f0b000ff">Usuários</span>, porém para a tabela de <span style="color: #f0b000ff">Usuários</span> estou usando o próprio <span style="color: #00f078ff">Auth</span> do <span style="color: #00f078ff">Django 5.2.7</span>.
## Sistema de Auth do Django - Como Funciona?
O sistema de auth do django conta com:
+ Model User
+ Login e logout
+ Troca de senha
+ Permissões e grupos
+ Middleware de autenticação

Então resolvi usá-lo, e tambem decidi não criar um app Users por não tratar nada por ele, iria ficar um app atoa, então optei por usar o sistema do Django e mais nada, assim deixando menos poluído, minha API não ia necessitar disso, talvez se houvesse outras necessidades eu iria criar um app destinado apenas para isso. Então caso se pergunte onde está guardado o código dos Usuários, ele está na pasta apiUsers, dentro da pasta principal do projeto. O sistema conta com authenticação por token, então é interessante colocar esse token em um header do postman(ou outro) para fazer esse cookie, este token vai ser importante para a relações entre tabelas.