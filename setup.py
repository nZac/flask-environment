"""
Flask-Config
-------------

Flask-Confg allows configuration of a Flask project with various serialization
formats.

"""

import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand

from flask_config import __VERSION__ as VERSION


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

testing_requirements = ['pytoml', 'pytest']


setup(
    name='Flask-Config',
    version=VERSION,
    url='http://github.com/teamskosh/flask-config',
    license='BSD',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='Configure a Flask application with various file formats.',
    long_description=__doc__,
    packages=['flask_config'],
    tests_require=testing_requirements,
    extras_require={
        'TOML': ['pytoml'],
    },
    cmdclass={'test': PyTest},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
