from setuptools import find_packages, setup

from flask_project.__version__ import __version__

setup(
    name='flask_project',
    version=__version__,
    packages=find_packages(),
    install_requires=[
        'docopt',
        'flask_script',
        'flask_migrate',
    ],
    package_data={
        'flask_project.templates' : ['*.tmpl'],
    },
    entry_points={
        'console_scripts' : ['flask-project=flask_project.main:main']
    }
)
