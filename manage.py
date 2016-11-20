from flask_script import Manager
from app import create_app
import os
import unittest

app = create_app(os.getenv('FLASK_CONFIG', 'default'))
manager = Manager(app)


@manager.command
def test():
    suite = unittest.TestLoader().loadTestsFromName('tests')
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    manager.run()
