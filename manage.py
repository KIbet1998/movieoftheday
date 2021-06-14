from app import create_app
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app('development')

migrate = Migrate(app)
manager = Manager(app)
manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
  return dict(app = app)

if __name__ == '__main__':
  manager.run()