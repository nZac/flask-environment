"""Flask-TOMLConfig

Description:
    Add a file called config.toml to you root project directory or pass a path to the configuration
    object to use a custom location.  All paths are relative to the Flask `app_root`.

Usage (config.toml in root):

    # app.py
    import flask
    from flask.ext.tomlconfig import ConfigEnvironment

    app = flask.Flask(__name__)
    ConfigEnvironment(app)

    # config.toml
    debug = true

Usage (custom path):

    # app.py
    import flask
    from flask.ext.tomlconfig import ConfigEnvironment

    app = flask.Flask(__name__)
    ConfigEnvironment(app)

    # config.toml
    debug = true
"""
import os
import toml
import logging


logger = logging.getLogger('flask_tomlconfig')


class ConfigEnvironment(object):
    """The main object to load the configuration into the flask object."""

    def __init__(self, app=None, path='config.toml'):
        """Create the configuration setup

        :param app: A flask application
        """

        if app is not None:
            self.init_app(app, path)

    def init_app(self, app, path='config.toml'):
        """Instantiate the application with the configuration information

        :param app: A Flask application object
        """

        # Construct the path to the configuration object
        config_file_path = os.path.join(app.root_path, path)

        # Set the default config dict
        toml_config = {}

        try:
            # Load the configuration file
            with open(config_file_path) as conf_file:
                toml_config = toml.loads(conf_file.read())
        except OSError as err:
            logging.error(err.message)
        else:
            # Flask expects the config vars to be uppercase
            config = {k.upper(): v for k, v in toml_config.items()}

            # Update the Flask Configuration
            app.config.update(config)
