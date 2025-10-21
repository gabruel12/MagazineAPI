# Início do Projeto - Magazine API
Requisitos para rodar a API (o que eu usei):
## Requiriments
+ [Python 3.12.7](https://www.python.org/downloads)
+ [Django 5.2.7](https://www.djangoproject.com/download)
+ Postman/Bruno (ou uma plataforma de testes para API's)
    
Libs:
+ <span style="color: #00ff6aff">django rest_framework</span>

How to install:

    in cmd
    python -m pip install djangorestframework
+ SQLite Viewer (VSCode Extensions)
+ VSCode (Ou Outro IDLE)
## Como funciona?
Essa API foi feita para um Desafio Backend da Magazine Luiza, onde eles solicitam uma API REST para a criação, edição e remoção de salas, com um sistema de agendamento, onde poderia fazer o mesmo que as salas, contando com um banco de dados para isso, eu quis fazer para este projeto um sistema de login também onde conta com o úsuario poder criar salas e agendamentos. Estou usando no banco de dados de Agendamentos que recebe uma tabela relacional à <span style="color: #f0b000ff">Salas</span> e aos <span style="color: #f0b000ff">Usuários</span>, porém para a tabela de <span style="color: #f0b000ff">Usuários</span> estou usando o próprio <span style="color: #00f078ff">Auth</span> do <span style="color: #00f078ff">Django 5.2.7</span>.