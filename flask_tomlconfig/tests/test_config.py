import tempfile
from flask_tomlconfig import ConfigEnvironment


class FakeApp(object):
    config = dict()
    root_path = '.'


class TestConfigEnvironment(object):

    def setup(self):
        self.config_file = tempfile.NamedTemporaryFile(suffix='.toml', dir='.')

    def teardown(self):
        self.config_file.close()

    def test_will_not_init_with_no_path(self):
        env = ConfigEnvironment()
        assert env._inited is False

    def test_init_sets_path_for_init_app(self):
        env = ConfigEnvironment(path=self.config_file.name)
        assert env._path == self.config_file.name

    def test_init_calls_init_app_with_app_object(self):
        self.config_file.file.write('var = "hello"')
        self.config_file.file.seek(0)

        app = FakeApp()
        env = ConfigEnvironment(app=app, path=self.config_file.name)
        assert env._inited is True
        assert app.config['VAR'] == 'hello'

    def test_throws_ioerror_when_no_file_exists(self):
        app = FakeApp()
        try:
            ConfigEnvironment(app=app, path='some/wierd/path/that/doesnt/exist')
        except ValueError, e:
            assert e.message == 'Could not load ./some/wierd/path/that/doesnt/exist. See logs for' \
                                ' details.'

    def test_throws_oserror_when_no_file_exists(self):
        app = FakeApp()
        try:
            ConfigEnvironment(app=app)
        except ValueError, e:
            assert e.message == 'Could not load ./config.toml. See logs for details.'
