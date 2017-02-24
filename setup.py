"""
Flask-Environment
------------------

Flask-Environment allows configuration of a Flask project with various
serialization formats.
"""

import sys
from setuptools import setup


setup(
    name='Flask-Environment',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    url='http://github.com/teamskosh/flask-environment',
    license='MIT',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='Configure a Flask application with various file formats.',
    long_description=__doc__,
    packages=['flask_environment'],
    extras_require={
        'toml': ['pytoml==0.1.11'],
        'dev': ['tox', 'pytest', 'pytoml']
    },
    zip_safe=True,
    platforms='any',
    install_requires=[
        'flask>=0.11'
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
