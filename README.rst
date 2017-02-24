Flask-Environment
#################

.. image:: https://circleci.com/gh/nZac/flask-environment/tree/master.svg?style=svg
    :target: https://circleci.com/gh/nZac/flask-environment/tree/master

Configure a Flask applications with various configuration formats.

Version
-------

0.1.0

Description
-----------

Configure Flask applications with other file formats like TOML. The killer
feature of Flask-Environment is the ability to adjust settings without multiple
configuration files.

Supports Python 2.7, 3.4, 3.5.

Installation
------------

.. code::

  $ pip install flask-environment


.. code::

  $ pip install flask-environment[TOML]


Usage Flask>0.10
----------------

.. code::

  import flask
  from flask_environment import Config

  class MyApp(flask.Flask):
      config_class = Config

  app = MyApp(__name__)
  app.config.from_toml('config.toml')


Environments
------------

Flask-Environment adds the idea of environments to a configuration file. For
different situations you might change the configuration even when the
application is deployed to the same machine, this is most helpful with testing.
You probably want to use a different database for testing than what you do for
regular development.

Flask-Environment solves this problem with the concept of environments. Within a
configuration file, create a new dict called ``environments`` with the keys being
the name of the different environments you intend to declare.

Activate an environment like this:


.. code::

  app.config.from_toml('config.toml', environment='testing')

This will load all the default settings (everything not in an environment)
and then the specified environment. Here is a sample TOML file demonstrating the
idea.

.. code::

  SUPER_COOL_FEATURE = true
  DEBUG = false

  [environments.dev]
  DEBUG = true

  [environments.testing]
  TESTING = true

If we loaded the ``dev``` environment, the application debug flag would be set to
``True`` and ``SUPER_COOL_FEATURE`` would be available.

While you could use this to provision different logical environments in the same
file (beta, production) there really isn't a point. Environments are for
changing configurations within the same logical environments. Maybe you have a
production environment that spawns two apps that need two diverging
configurations, environments fill that need.

Licence
-------

MIT
