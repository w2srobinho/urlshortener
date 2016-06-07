import string

import settings
from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

ALPHA_NUMERIC_RANGE = string.digits + string.ascii_letters

app = Flask(__name__)
app.config.from_object(settings)
app.config.update()

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

from . import views, models
