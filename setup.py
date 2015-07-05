"""
Flask-TOMLConfig
-------------

Flask-TOMLConfg allows configuration of a Flask project with a toml file.
"""
from setuptools import setup


setup(
    name='Flask-TOMLConfig',
    version='1.0.0',
    url='http://github.com/nzac/flask-tomlconfig',
    license='BSD',
    author='Nick Zaccardi',
    author_email='nicholas.zaccardi@gmail.com',
    description='Configure a flask application with a TOML file',
    long_description=__doc__,
    packages=['flask_tomlconfig'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'toml'
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
