import os
import copy
import errno

from flask.config import Config as FlaskConfig
from flask._compat import iteritems
from flask import json


class ConfigError(Exception):
    pass


class Config(FlaskConfig):

    def __init__(self, root_path=None, defaults=None, app=None):
        dict.__init__(self, defaults or {})
        self.root_path = root_path

        if app:
            import pdb; pdb.set_trace()
            self.init_app(app)

    def init_app(self, app):
        self.from_mapping(app.config)
        app.config = self
        return self

    def _get_environment(self, env, config):
        """Return a dictionary containing the top level values updated with
        those from the environment.

        :param env: The name of the environment as a string
        :param config: the configuration mapping
        :return: a dictionary
        """
        # Get the top level keys
        defaults = {k: v for k, v in iteritems(config) if k != 'environments'}

        try:
            defaults.update(config['environments'][env])
            return defaults
        except KeyError as e:
            msg = 'Unable to find %s environment in configuration file' % env
            raise ConfigError(msg)

    def from_toml(self, filename, silent=False, environment=None):
        """Updates the values in the config from a TOML file. This function
        behaves as if the TOML object was a dictionary and passed to the
        :meth:`from_mapping` function.

        :param filename: the filename of the JSON file.  This can either be an
                         absolute filename or a filename relative to the
                         root path.
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        """
        try:
            import pytoml as toml
        except ImportError as e:
            if silent:
                return False
            e.strerror = 'Unable to load pytoml, is the packaged installed?'
            raise

        # Prepeend the root path is we don't have an absolute path
        filename = (os.path.join(self.root_path, filename)
                    if filename.startswith(os.sep)
                    else filename)

        try:
            with open(filename) as toml_file:
                obj = toml.load(toml_file)
        except IOError as e:
            if silent and e.errno in (errno.ENOENT, errno.EISDIR):
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise

        env = self._get_environment(environment, obj) if environment else obj
        obj.update(env)

        return self.from_mapping(obj)

    def from_json(self, filename, silent=False, environment=None):
        """Updates the values in the config from a JSON file. This function
        behaves as if the JSON object was a dictionary and passed to the
        :meth:`from_mapping` function.

        :param filename: the filename of the JSON file.  This can either be an
                         absolute filename or a filename relative to the
                         root path.
        :param silent: set to ``True`` if you want silent failure for missing
                       files.
        .. versionadded:: 1.0
        """
        filename = os.path.join(self.root_path, filename)

        try:
            with open(filename) as json_file:
                obj = json.loads(json_file.read())
        except IOError as e:
            if silent and e.errno in (errno.ENOENT, errno.EISDIR):
                return False
            e.strerror = 'Unable to load configuration file (%s)' % e.strerror
            raise

        env = self._get_environment(environment, obj) if environment else obj
        obj.update(env)

        return self.from_mapping(obj)

    def from_mapping(self, *mapping, **kwargs):
        """Updates the config like :meth:`update` ignoring items with non-upper
        keys.
        .. versionadded:: 1.0
        """
        mappings = []
        if len(mapping) == 1:
            if hasattr(mapping[0], 'items'):
                mappings.append(mapping[0].items())
            else:
                mappings.append(mapping[0])
        elif len(mapping) > 1:
            raise TypeError(
                'expected at most 1 positional argument, got %d' % len(mapping)
            )
        mappings.append(kwargs.items())
        for mapping in mappings:
            for (key, value) in mapping:
                if key.isupper():
                    self[key] = value
        return True

    def get_namespace(self, namespace, lowercase=True, trim_namespace=True):
        """Returns a dictionary containing a subset of configuration options
        that match the specified namespace/prefix. Example usage::
            app.config['IMAGE_STORE_TYPE'] = 'fs'
            app.config['IMAGE_STORE_PATH'] = '/var/app/images'
            app.config['IMAGE_STORE_BASE_URL'] = 'http://img.website.com'
            image_store_config = app.config.get_namespace('IMAGE_STORE_')
        The resulting dictionary `image_store` would look like::
            {
                'type': 'fs',
                'path': '/var/app/images',
                'base_url': 'http://img.website.com'
            }
        This is often useful when configuration options map directly to
        keyword arguments in functions or class constructors.
        :param namespace: a configuration namespace
        :param lowercase: a flag indicating if the keys of the resulting
                          dictionary should be lowercase
        :param trim_namespace: a flag indicating if the keys of the resulting
                          dictionary should not include the namespace
        .. versionadded:: 1.0
        """
        rv = {}
        for k, v in iteritems(self):
            if not k.startswith(namespace):
                continue
            if trim_namespace:
                key = k[len(namespace):]
            else:
                key = k
            if lowercase:
                key = key.lower()
            rv[key] = v
        return rv
