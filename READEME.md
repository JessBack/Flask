Tutorial Flask Python Brasil 13
Aprenda Flask criando um CMS e suas extensões

Objetivos
Tutorial mão na massa onde os participantes irão aprender a configurar a arquitetar um aplicativo Flask para gestão de conteúdo (BLOG, Site, Portal etc)

CMS?
CMS é Content Management System, é o nome a qualquer sistema que permita gerenciamento dinâmico de conteúdo e a apresentação e controle de seu acesso.

Serve para criarção de blogs, sites, portais etc.. (ex: Quokka CMS, Django CMS, Wordpress)

O aplicativo em funcionamento esté em http://pybrflask.pythonanywhere.com/

O admin em http://pybrflask.pythonanywhere.com/admin (usuario: admin senha: admin)

O código final deste tutorial está na branch cms_9_deploy: https://github.com/cursodepythonoficial/flask_tutorial_pybr13/tree/cms_9_deploy

TL;DR: Comece aqui -> Parte 0
Tópicos
Flask 101
(teórico + demos ~ 1h periodo da manhã)

Hello world e o ambiente web
App e configurações
Views e Rotas
Responses
Requests
session
Templates
Extensões
Arquitetura e boas práticas
(teórico + demo ~ 1h periodo da manhã)

12 factor: configurações dinâmicas
The Factory pattern
(evitando problemas com circular imports)
Extensões e blueprints
(criando módulos/plugins reusaveis)
Testing
Servindo a app
Mão na massa
Construindo o CMS
(Prática - Mão na Massa - step by step ~4hrs periodo da tarde)

Ambiente - Branch
Arquitetura do Projeto e dicas de estrutura e qualidade - Branch
CLI (tudo começa na linha de comando) - Branch
Factories
Application factory - Branch
Configuration factory - Branch
Extension factory - Branch
Autenticação
Banco de dados NoSQL
(neste tutorial não abordaremos SQL nem ORMs)
Flask-Admin, AdminViews & WTForms - Branch
Jinja - Branch
Jinja Extensions - Branch
Arquivos estáticos - Branch
WSGI - Branch
test - Branch
Bonus Deploy na PythonAnywhere.com

deploy - Branch
Requisitos
Parte 1 - manhã
Para participar da parte teórica (periodo da manhã) não tem nenhum requisito, todas as pessoas de qualquer nivel de conhecimento em Python mesmo sem um computador pode participar.

parte 2 - tarde
Conhecimento
Para a parte prática é necessário conhecimento básico iniciante em Python, o foco será na explicação das funcionalidade do Flask e não serão explicados conceitos da linguagem como por exemplo o que são classes, funções, métodos, decorators, módulos etc..

Contudo será apresentado snippets de código para serem replicados portanto não é necessário entendimento complexo de Python para conseguir participar.

Técnicos
Computador com Python 3.6+ instalado, não será abordado a instalação do Python3.6 portanto aconselho estar com esta versão já disponivel. (recomendo a ferramenta pyenv para automatizar a instalação e aproveite os dias que antecedem o tutorial para conseguir ajuda durante o evento para instalar, tutorial de como usar o pyenv)

Sistema operacional de sua preferencia desde que tenha dominio do uso de seu console/terminal, recomendo o uso de Linux

Editor de códigos de sua preferencia, não será preciso funcionalidades avançadas de IDEs, portanto qualquer editor básico é suficiente. (recomendo: Gedit, Notepad++, Sublime, Atom, VSCode, Vim)

Browser atualizado (Chrome ou Firefox)

Se tiver acesso a internet no local do tutorial será excelente para instalar as dependencias. Porém recomendo clonar este repositório:

Preparando o ambiente e instalando as dependencias (faça isso antes do dia do tutorial em um local com acesso a internet)

git clone git@github.com:cursodepythonoficial/flask_tutorial_pybr13.git flask_pybr
cd flask_pybr
python3.6 -m venv venv
. venv/bin/activate
venv/bin/pip3 install -r requirements.txt  
Advanced
Se você quiser clonar de uma só vez todas as branches deste repositório execute:

mkdir flask_pybr;cd flask_pybr;git clone --bare git@github.com:cursodepythonoficial/flask_tutorial_pybr13.git .git;git config --unset core.bare;git reset --hard

# Criando e ativando a virtualenv
python3.6 -m venv venv; . venv/bin/activate

# agora pode mudar para a ultima branch (projeto completo)
git checkout cms_9_deploy
pip install -r requirements.txt
python setup.py develop
cms adduser
cms runserver
Info
Data: 09/10
Horário: 8:30 (é bom chegar mais cedo também!)
Local: UNA Barro Preto (https://goo.gl/maps/82tiKzTvMzC2)
Detalhes: http://2017.pythonbrasil.org.br/#schedule
Inscrição: Tutoriais são treinamentos de 3 a 6 horas totalmente gratuitos para você se tornar um Jedi. A menos que informado do contrário, a entrada aos tutoriais são abertas, por ordem de chegada, sem necessidade de inscrição.