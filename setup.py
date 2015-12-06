"""
Flask-Environment
-------------

Flask-Environment allows configuration of a Flask project with various
serialization formats.
"""

import sys
from setuptools import setup


VERSION = '0.2.0'

setup(
    name='Flask-Environment',
    version=VERSION,
    url='http://github.com/teamskosh/flask-environment',
    download_url='https://github.com/teamskosh/flask-environment/tarball/' + VERSION,
    license='MIT',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='Configure a Flask application with various file formats.',
    long_description=__doc__,
    packages=['flask_environment'],
    extras_require={
        'TOML': ['pytoml'],
    },
    zip_safe=False,
    platforms='any',
    install_requires=[
        'flask'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
