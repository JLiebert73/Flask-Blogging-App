from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from test import app, db

# Initialize Flask-Migrate
migrate = Migrate(app, db)
manager = Manager(app)

# Add the MigrateCommand to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
