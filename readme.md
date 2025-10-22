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

Então resolvi usá-lo, e tambem decidi não criar um app Users por não tratar nada por ele, iria ficar um app atoa, então optei por usar o sistema do Django e mais nada, assim deixando menos poluído, minha API não ia necessitar disso, talvez se houvesse outras necessidades eu iria criar um app destinado apenas para isso. Então caso se pergunte onde está guardado o código dos Usuários, ele está na pasta apiUsers, dentro da pasta principal do projeto. O sistema conta com authenticação por token, então é interessante colocar esse token em um header do postman(ou outro) para fazer esse cookie, este token vai ser importante para a relações entre tabelas. Pode ser acessado pela rota **_api/auth/algumafunção_**, contendo login(para logar e obter o token), logout(para sair) e cadaster(para se cadastrar).
### cadastre-se com:
    {
        "username": "your_username",
        "password": "your_password"  // Se lembre dela!
    }
### faça login com:
    {
        "username": "your_username",
        "password": "your_password"
    }
### faça logout apenas entrando.
O Logout conta com uma forma simples, apenas deletando o Token do usuário, então para logout basta acessar a url.
# Sistema de Rooms - Como Funciona?
Bom, o sistema de salas conta com um modelo Room que recebe um nome, uma capacidade e o objetivo da sala (sobre o que será feito) com o intuito de manter a organização, a API conta com um sistema de criação(não relacionado à usuários), de editar, e deletar salas, pode ser acessado pela rota **_api/rooms/algumafunção_** sendo elas as citadas anteriormente.

### Crie uma sala com:
    {
    "name": "Room Name",
    "capacity": 20,
    "objective": "Test Room"
    }
### Delete apenas acessando:
    api/rooms/delete/Room%20Name/
### Edite uma sala com:
    {
    "name": "New Name",
    "capacity": 20,
    "objective": "New Objective"
    }

#### Observação:
Para a filtragem de salas/reservas será usado por uma API separada, com o intuito de manter a organização e preserver os princípios SOLID onde cada coisa tem sua função assim como requisitado pelo mesmo.
# Sistema de Schedules - Como Funciona?
O sistema de Schedules/Reserves serve para agendar uma sala, tendo o banco Room como relacionado, o agendamento recebe horário de início e horário de término, recebe um nome e também recebe o banco User relacionado por quem criou a reserva, caso o usúario ou a sala sejam deletados, os agendamentos se vão com eles e serão desfeitos/deletados.

### Como Agendar:
    {
        "room": "RoomName",
        "start_time": "2025-10-12T12:00:00Z",
        "end_time": "2025-10-12T14:00:00Z"
    }

E estando logado ele cria o agendamento com a sala e o usuário.
### Como Remover:
    na url:
    api/schedules/remove/ScheduleId/

E apenas acessando ele já remove.
# Sistema de Filtering - Como Funciona?
O sistema de Filtering serve para ser uma API para filtragem e listagem de todos os quesitos dessa aplicação, desdê salas até reservas, sendo elas listas ou apenas uma sala/reserva específica, funciona a base de GET na url com querysets usando o nome, ou pedindo a lista da tabela específica.
### Exemplo:
    Método: PUT
    api//filter/DbName/RoomName/
ou

    Método: PUT
    api//list/DbName/

usando o nome de uma sala ou de uma reserva para obter as especificações dela ou usando o nome **rooms** seja ela Room ou **schedules** para Schedule para obter dados da tabela(todas as salas, ou todos os agendamentos).
## Por Quê?
Prefiri fazer uma listagem separada para que possa globalizar essa função de modo com que caso outros bancos sejam criados eles possam ter uma filtragem com fácil manutenção, e para que não dependam de uma própria filtragem ou listagem de seus objetos, também prezando pela organização e pela otimização da API, deixando-a mais eficiente.
# Sistema de Logs - Como Funciona?
A API conta com um sistema de logs para que possa saber quem criou, editou, deletou tal coisa, foram inclementados alguns logs com nomes específicos para funções específicas, os nomes podem sem vistos na pasta Logs no arquivo logs, onde tem o dicionário de LOGS_MESSAGES. Caso haja dúvida lá estará guardado, o sistema de logs foi feito na intenção de que não de para apagar-los e também com o intuito de ser fácil de usar, organizado e que possa receber atualizações de logs caso seja preciso, se houver algo a mais por exemplo, uma criação de uma função extra, esse log pode ser incrementado fácil e rápido apenas o adicionando no nosso dicionário.
# Inplementação do PyTest
## como usar a lib pytest?
Começare-mos instalando a lib usando o pipinstall do python, em nosso terminal, utilizando o comando:

    python -m pip install pytest

Como pode ver acima, para sistemas de tests unitários foram criadas algumas pastas em cada app do projeto para que possa receber essa atualização de testes depois, por enquanto a parte de testes está em **_desenvolvimento_**, espero trazer-lo da melhor forma possível para que os teste unitários sejam eficazes e úteis quando necessário.
# Interface de Teste com Bruno
Foi adicionada a pasta _MagazineAPI_JSON_tests_ na raíz do projeto, esta pasta pode ser aberta usando o Bruno Client (não sei se funciona com outra interface de testes de API's), o íntuito desta pasta é facilitar os testes em JSON já com urls prontas e organizadas para que o teste seja feito.
## Como baixar o Bruno Client?
Para baixar basta acessar o link abaixo:
+ [Bruno Client - www.usebruno.com](https://www.usebruno.com/pricing)

Clique no botão de download da versão Open Source do projeto, após instalação você pode notar que a interface é bem amigável e que lembra muito o postman.
# Fixed bugs
Alguns bugs foram identificados com o desenvolvimento do projeto, e resolvidos para a melhor experiencia da API, outros não, foram arrumados:
+ Edit Room - A sala podia ser renomeada com o mesmo nome que outra.
+ Filter Room - Caso houvesse 2 salas com mesmo nome, não retornava um objeto.
# bugs
+ Login - O **principal** bug deste projeto está sendo a authenticação de um login usando o token, estou tentando encontrar este erro para arrumar e fazer com que nosso usuário possa ser logado e não retornar um erro de token. Por enquanto peço que quando for criar uma **sala** user _**created_by:**_ _user_name_ , para que possa ser criada, caso contrário se o bug ainda estiver ativo ele retornará que está faltando um campo obrigátorio: **created_by**.
# Notas
Foram adicionadas algumas mensagens em json para retornar um erro mais amigável caso haja algum, estes **erros** são apenas erros que provávelmente vieram do teste e não erros do sistema em sí, como quando retorna um 404 (Page Not Found) ou alguns outros, caso apareça um erro do próprio sistema do django, então muito provávelmente este erro passou **despercebido**.
#### Agradeço a atenção.
<hr>
