# URLShortener
É um encurtador que permite gerar estatísticas das urls cadastradas no sistema.

## Desenvolvimento

### Tecnologias

#### Back-End

O back-end é Python + Flask e tem uma camada de banco de dados usando Postgres.
A aplicação disponibiliza uma API REST para uso do encurtador.

* Git.
* Python 3.4+
* PostgreSQL 9
* Flask: Fornecer interface de acesso (endpoints)
* Flask-SQLAlchemy: ORM para gerenciar o acesso ao banco de dados
* Flask-Migrate: Para gerar as tabelas do banco de dados


### Ambiente

#### Database

O lsistema usa o PostgreSQL como banco de dados. É necessário instalar e criar o banco, as tabelas são criadas usando comandos do Flask.

* Instalar a ultimas versão do PostgreSQL 9 para seu sistema operacional, [Aqui](http://www.postgresql.org/download/).
* Para usuários Debian/Ubuntu: Instalar a [libpq-dev package](http://packages.debian.org/sid/libpq-dev). Comando: `sudo apt-get install libpq-dev`
* Criar um banco de dados: ex. Command: `createdb -U postgres <bd_name>`.

#### Ambiente e Dependências

##### Ubuntu

* Definir a variavel de ambiente com o endereço do banco de dados:
    `export POSTGRESQL_DATABASE="postgresql://<username>:<password>@<host>:<port>/<database_name>`

* Rodar o script `install.sh` para baixar as dependencias: `$ sudo sh install.sh`
* Rodar o script `start.sh` para iniciar o serviço: `$ sh start.sh`

##### Outros Unix like

* Definir a variavel de ambiente com o endereço do banco de dados:
    `export POSTGRESQL_DATABASE=\"postgresql://<username>:<password>@<host>:<port>/<database_name>`

* Instalar o Python 3.4+, [Aqui](https://www.python.org/downloads/)
* Criar um ambiete virtual com pyvenv: `$ pyvenv ENV` [Mais informaçẽo aqui](https://docs.python.org/3/library/venv.html)
* No Linux, para habilitar o uso do ambiente virtual criado acima é só rodar o comando: `source ENV/bin/activate`.
* Rodar o comando: `$ python manager.py db upgrade`, para gerar as tabelas do banco de dados

* Instalar as dependências usando o pip: `pip install requirements.txt`
* Rodar o script `start.sh` para iniciar o serviço: `$ sh start.sh`

#### Test

* Para rodar os tests use o comando: `python -m unittest`, com o ambiente virtual habilitado
