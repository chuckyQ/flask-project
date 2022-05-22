"""
Usage:
  flask-project [options] <appname>

Options:
  -h, --help     Show this help screen and exit
  --version      Show tool version
  -R, --restful  Create a Flask REST API
"""

import os
from importlib import resources

from docopt import docopt

from flask_project import (__version__,
                           templates,
                           )


def write_template(tmpl: str, filepath: str, **kwargs):

    dirpath = os.path.dirname(filepath)
    os.makedirs(dirpath, exist_ok=True)

    t = resources.open_text(templates, tmpl)
    with open(filepath, 'w') as f:
        tmpl = t.read()
        tmpl = tmpl.format(**kwargs)
        f.write(tmpl)
    t.close()


def main():

    options = docopt(__doc__, version=__version__.__version__)

    appname = options['<appname>']
    os.makedirs(appname)

    join = os.path.join

    p = join(appname, appname, 'models')

    p = join(appname, appname, 'models', '__init__.py')
    write_template('models__init__.py.tmpl', p, APP_NAME=appname)

    p = join(appname, appname, 'models', 'models.py')
    write_template('models.py.tmpl', p, APP_NAME=appname)

    p = join(appname, '.env')
    write_template('.env.tmpl', p, APP_NAME=appname)

    if options['--restful']:
        p = join(appname, 'app.py')
        write_template('app-restful.py.tmpl', p, APP_NAME=appname)

        p = join(appname, appname, 'resources', '__init__.py')
        write_template('resource__init__.py.tmpl', p, APP_NAME=appname)

        p = join(appname, appname, 'resources', 'resource.py')
        write_template('resource.py.tmpl', p, APP_NAME=appname)
        return

    p = join(appname, 'app.py')
    write_template('app.py.tmpl', p, APP_NAME=appname)

    for each in ['templates', 'static']:
        p = join(appname, each)
        os.makedirs(p)

    p = join(appname, appname, '__init__.py')
    write_template('app__init__.py.tmpl', p, APP_NAME=appname)

    p = join(appname, appname, 'blueprints', '__init__.py')
    write_template('blueprint__init__.py.tmpl', p, APP_NAME=appname)

    p = join(appname, appname, 'blueprints', 'blueprint.py')
    write_template('blueprint.py.tmpl', p, APP_NAME=appname)
