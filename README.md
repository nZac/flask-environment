# Flask-Environment
[![Circle CI](https://circleci.com/gh/nZac/flask-environment.svg?style=svg)](https://circleci.com/gh/nZac/flask-environment)

Configure a Flask applications with various configuration formats.

## Version
0.1.0

## Description

Flask 0.10 support loading configuration from an environment variable and a
Python module.  This plugin extends that to include TOML and a backport of the
JSON implementation expected in 1.0 (or 0.11, whatever the release after 0.10).


Supports Python 2.7, 3.4, 3.5.

## Installation

```sh
$ pip install flask-environment
```

```sh
# With TOML support
$ pip install flask-environment[TOML]
```


## Usage Flask<=0.10

Flask 0.10 doesn't allow overriding the configuration class whereas 1.0 will.
Flask-Environment is build with 1.0 in mind and expects <=0.10 to override
`make_config` on the application object.

```python
import flask
from flask_environment import Config

class MyApp(flask.Flask):

    # Backport the logic of Flask.make_config replacing the default config
    # class with Flask-Environments
    def make_config(self, instance_relative=False):
        root_path = self.root_path

        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)

app = MyApp(__name__)
app.config.from_toml('config.toml')
```

## Usage Flask>0.10 (unreleased as of writing 12/5/2015)

```python
import flask
from flask_environment import Config

class MyApp(flask.Flask):
    config_class = Config

app = MyApp(__name__)
app.config.from_toml('config.toml')
```


## Environments

Flask-Environment adds the idea of environments to a configuration file. For
different situations you might change the configuration even when the
application is deployed to the same machine, this is most helpful with testing.
You probably want to use a different database for testing than what you do for
regular development.

Flask-Environment solves this problem with the concept of environments. Within a
configuration file, create a new dict called `environments` with the keys being
the name of the different environments you intend to declare.

Activate an environment like this:

```python
app.config.from_toml('config.toml', environment='testing')
```

This will load all the default settings (everything not in an environment)
and then the specified environment. Here is a sample TOML file demonstrating the
idea.

```toml
SUPER_COOL_FEATURE = true
DEBUG = false

[environments.dev]
DEBUG = true

[environments.testing]
TESTING = true
```

If we loaded the `dev` environment, the application debug flag would be set to
`True` and `SUPER_COOL_FEATURE` would be available.

While you could use this to provision different logical environments in the same
file (beta, production) there really isn't a point. Environments are for
changing configurations within the same logical environments. Maybe you have a
production environment that spawns two apps that need two diverging
configurations, environments fill that need.

## Licence

MIT
