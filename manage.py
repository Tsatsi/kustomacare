from flask.ext.script import Manager
import os
import subprocess
from app import app

manager = Manager(app)
if not os.getenv('KC_ENV'):
    os.environ['KC_ENV'] = "config.Testing"


@manager.command
def test():
    os.environ['KC_ENV'] = "config.Testing"
    subprocess.call(["nosetests"])


if __name__ == '__main__':
    manager.run()
