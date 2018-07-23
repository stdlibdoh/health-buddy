from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_migrate import upgrade as upgrade_database
from app import app, db, parsers, prepare_app

prepare_app(environment='development')
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def dbseed():
    with open('onboarding.json') as onboard_file:
        db.save(parsers.onboard_from_json(onboard_file.read()))

if __name__ == "__main__":
    manager.run()
