import flask
from flask_environment import Config


class FlaskApp(flask.Flask):
    def make_config(self, instance_relative=False):
        root_path = self.root_path

        if instance_relative:
            root_path = self.instance_path
        return Config(root_path, self.default_config)
