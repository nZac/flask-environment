"""
Flask-Config
-------------

Flask-Confg allows configuration of a Flask project with various serialization
formats.
"""

import sys
from setuptools import setup


VERSION = '0.1.0'

setup(
    name='Flask-Config',
    version=VERSION,
    url='http://github.com/teamskosh/flask-config',
    download_url='https://github.com/teamskosh/flask-config/tarball/' + VERSION,
    license='MIT',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='Configure a Flask application with various file formats.',
    long_description=__doc__,
    packages=['flask_config'],
    extras_require={
        'TOML': ['pytoml'],
    },
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
