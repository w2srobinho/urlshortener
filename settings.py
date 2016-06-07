import os
basedir = os.path.abspath(os.path.dirname(__file__))

HOSTNAME = ''

SQLALCHEMY_DATABASE_URI = os.environ['POSTGRESQL_DATABASE']
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
