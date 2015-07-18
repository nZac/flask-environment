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
    ConfigEnvironment(app, path='config.toml')

    # config.toml
    debug = true
"""
import os
import toml
import logging


__VERSION__ = '1.1.0'
logger = logging.getLogger('flask_tomlconfig')


class ConfigEnvironment(object):
    """The main object to load the configuration into the flask object."""

    _inited = False
    _path = 'config.toml'

    def __init__(self, app=None, path=None):
        """Create the configuration setup

        :param app: A flask application
        """

        if path is not None:
            self._path = path

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Instantiate the application with the configuration information

        :param app: A Flask application object
        """
        # Set the default config dict
        toml_config = {}

        try:
            # Construct the path to the configuration object
            config_file_path = os.path.join(app.root_path, self._path)

            # Load the configuration file
            with open(config_file_path) as conf_file:
                toml_config = toml.load(conf_file)
        except (IOError, OSError), err:
            logger.error('Flask-TOMLConfig load error: {}'.format(err.strerror))
            raise ValueError('Could not load {}. See logs for details.'.format(config_file_path))
        else:
            # Flask expects the config vars to be uppercase
            config = {k.upper(): v for k, v in toml_config.items()}

            # Update the Flask Configuration
            app.config.update(config)

        # Let us know we have _inited
        logger.info('Flask-TOMLConfig loaded {}.'.format(config_file_path))
        self._inited = True
