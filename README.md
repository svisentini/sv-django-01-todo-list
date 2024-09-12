# sv-django-01-todo-list
Todo list with Django


DJANGO
Framework para Desenvolvimento Python


Video Youtube
	https://www.youtube.com/watch?v=MsUL3Pgofl4&t=28s
Configuração do Ambiente
https://github.com/treinaweb/treinaweb-youtube-introducao-ao-django/blob/main/.github/SETUP.md
Instalar uma extensão no VSCode para facilitar a visualização dos dados no SQLite
	SQLite Viewer

PIP >> Gerenciador de pacotes do python
Ambientes Virtuais >> Para nao ocorrer problemas de conflito de versoes das dependencias entre um projeto e outro >> Quando instaladas de forma global.
Cada projeto tera suas proprias dependencias.
	
--------------------------------------------------------
Passos para rodar a aplicação:
--------------------------------------------------------
- Git clone
- sudo apt install python3-venv			>> Pacote para criar Ambientes Virtuais
- VSCode
  
	Extensões (Ctrl + P)

		ext install ms-python.python
  
		ext install batisteo.vscode-django
  
		SQLite Viewer
  
- python3 -m venv .venv 				>> Criar Ambiente Virtual
- source .venv/bin/activate 			>> Entrar no Ambiente Virtual
- pip install django
- pip install python-decouple
- pip install dj-database-url
Verificar se os arquivos .env e db.sqlite3 existem
- python manage.py makemigrations		>> Criar os arquivos de migração
- python manage.py migrate				>> Rodar as migrações
- python manage.py runserver			>> Rodar a aplicação

--------------------------------------------------------


1) Criar ambiente virtual e ativar
Linux:
		python3 -m venv .venv         >> Cria um Ambiente Virtual
		source .venv/bin/activate     >> Entra no Ambiente Virtual

2) Instalar o Django (dentro do ambiente virtual >> criado e ATIVADO no passo 1)
	pip install django

Para saber que esta dentro do ambiente virtual, verificar no inicio da linha de comando (.venv)

	
3) Criar um projeto (Projeto é um conjunto de app >> app seria cada funcionalidade)
	django-admin startproject setup .
Será criada uma pasta com alguns arquivos de configuração, por isso, por convensão essa pasta é chamada de setup, mas não é obrigatório.
	
4) Rodar aplicacao
	python manage.py runserver

5) Criar um APP (deve estar com o Ambiente Virtual ativo)
	python manage.py startapp todos

6) Precisa relacionar a APP com o projeto
“settings.py” tem os INSTALLED_APPS
Adicionar o APP recém criado
‘todos.apps.TodosConfig’

7) Criar arquivos de migrações a partir das classes de models.py
	python manage.py makemigrations

8) Rodar as migrações
	python manage.py migrate

    No arquivo “db.sqlite3”, é possível ver as tabelas criadas






Em “settings.py” tem algumas configurações para alterar:
- LANGUAGE_CODE para ‘pt-br’
- TIME_ZONE para 'America/Sao_Paulo'


Django trabalha com a arquitetura MTV

Model = É a camada relacionada com o Banco de Dados. Classes python que representam as entidades que a aplicação trabalha.

Template = Camada de visualização dos dados. Onde o usuário interage com a aplicação. São os arquivos HTML.

View = É a camada que faz o relacionamento entre as duas outras camadas.


Cada função declarara em views.py tem que ter um parametro “request”

No arquivo urls.py definimos a url e qual função será executada.

No models.py cada classe representa uma tabela no banco de dados.
Para isso, a classe precisa extender “models.Model”
Cada coluna do banco, será representado por um atributo nessa classe.


45:00 do video

Isolar as configurações para não ficarem "expostas"
    Instalar uma biblioteca para isso
        pip install python-decouple
    Criar um arquivo ".env" na raiz do projeto
        SECRET_KEY=django-insecure-gy$h5(78bb-cufrww@^o9b%b&d9r0!#4mr(kx27*wcrg!crod-
        DEBUG=True
        ALLOWED_HOSTS=*
    settings.py >> from decouple import config
    config("SECRET_KEY")
    Para a String de conexão, sera necessario outra biblioteca
        pip install dj-database-url
    from dj_database_url import parse as db_url

52:00 do video

--------------------------

11/09/2024