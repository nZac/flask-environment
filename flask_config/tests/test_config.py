import os
import flask

import pytest
import pytoml as toml

from flask_config import Config
from . import FlaskApp


class FileTypeTest(object):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    def basic_test(self, config):
        assert config['TEST_KEY'] == 'foo'
        assert config['SECRET_KEY'] == 'devkey'
        assert 'ignored' not in config

    def advanced_test(self, config):
        assert config['TEST_KEY'] == 'foo'
        assert config['SECRET_KEY'] == 'devkey'
        assert 'ignored' not in config

        assert config['DATABASE'] == {
            'HOST': 'something',
            'PORT': 2345,
            'ignored': 'no'
        }

    def environment_test(self, filename):
        config = Config('')
        config.from_toml(filename, environment='dev')

        assert config['TEST_KEY'] == 'foo'
        assert config['SECRET_KEY'] == 'devkey'
        assert config['DEBUG'] == True
        assert 'TESTING' not in config
        assert 'ignored' not in config

        config = Config('')
        config.from_toml(filename, environment='testing')
        assert config['TEST_KEY'] == 'foo'
        assert config['SECRET_KEY'] == 'devkey'
        assert config['TESTING'] == True
        assert 'DEBUG' not in config
        assert 'ignored' not in config


    def example_prefix(self, name):
        return os.path.join(self.current_dir, 'examples', name)


class TestConfig(object):

    def test_create_of_config_object(self):
        app = FlaskApp('name')
        assert isinstance(app.config, Config)

    def test_get_environment_returns_part_of_dict(self):
        config = Config('')
        test = {
            'KEY': False,
            'environments': {
                'debug': {
                    'DEBUG': True
                },
                'testing': {
                    'TESTING': True
                }
            }
        }
        assert config._get_environment('debug', test) == {
            'DEBUG': True,
            'KEY': False
        }


class TestConfigToml(FileTypeTest):

    def test_toml_format_error(self):
        with pytest.raises(toml.TomlError):
            example = self.example_prefix('format_err.toml')
            config = Config('')
            config.from_toml(example)

    def test_toml_basic(self):
        config = Config('')
        config.from_toml(self.example_prefix('basic.toml'))
        self.basic_test(config)

    def test_toml_advanced(self):
        config = Config('')
        config.from_toml(self.example_prefix('advanced.toml'))
        self.advanced_test(config)

    def test_toml_environment(self):
        self.environment_test(self.example_prefix('environments.toml'))
