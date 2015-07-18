# Flask-TOML

Configure Flask applications with a TOML file.

## Version
1.1.0

## Description:
Add a file called config.toml to you root project directory or pass a path to the configuration
object to use a custom location.  All paths are relative to the Flask `app_root`.

## Usage

Some example uses.

### config.toml in root of project

```python
import flask
from flask.ext.tomlconfig import ConfigEnvironment

app = flask.Flask(__name__)
ConfigEnvironment(app)
```

### config.toml up a directory

```python
# app.py
import flask
from flask.ext.tomlconfig import ConfigEnvironment

app = flask.Flask(__name__)
ConfigEnvironment(app, path='../config.toml')
```
