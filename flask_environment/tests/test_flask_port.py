import os

import pytest

from . import FlaskApp


def common_object_test(app):
    assert app.secret_key == 'devkey'
    assert app.config['TEST_KEY'] == 'foo'
    assert 'TestConfig' not in app.config


def test_config_from_json():
    app = FlaskApp(__name__)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app.config.from_json(os.path.join(current_dir, 'examples', 'config.json'))
    common_object_test(app)

def test_config_missing_json():
    app = FlaskApp(__name__)
    try:
        app.config.from_json('missing.json')
    except IOError as e:
        msg = str(e)
        assert msg.startswith('[Errno 2] Unable to load configuration '
                              'file (No such file or directory):')
        assert msg.endswith("missing.json'")
    else:
        assert 0, 'expected config'
    assert not app.config.from_json('missing.json', silent=True)

def test_config_from_mapping():
    app = FlaskApp(__name__)
    app.config.from_mapping({
        'SECRET_KEY': 'devkey',
        'TEST_KEY': 'foo'
    })
    common_object_test(app)

    app = FlaskApp(__name__)
    app.config.from_mapping([
        ('SECRET_KEY', 'devkey'),
        ('TEST_KEY', 'foo')
    ])
    common_object_test(app)

    app = FlaskApp(__name__)
    app.config.from_mapping(
        SECRET_KEY='devkey',
        TEST_KEY='foo'
    )
    common_object_test(app)

    app = FlaskApp(__name__)
    with pytest.raises(TypeError):
        app.config.from_mapping(
            {}, {}
        )

def test_get_namespace():
    app = FlaskApp(__name__)
    app.config['FOO_OPTION_1'] = 'foo option 1'
    app.config['FOO_OPTION_2'] = 'foo option 2'
    app.config['BAR_STUFF_1'] = 'bar stuff 1'
    app.config['BAR_STUFF_2'] = 'bar stuff 2'
    foo_options = app.config.get_namespace('FOO_')
    assert 2 == len(foo_options)
    assert 'foo option 1' == foo_options['option_1']
    assert 'foo option 2' == foo_options['option_2']
    bar_options = app.config.get_namespace('BAR_', lowercase=False)
    assert 2 == len(bar_options)
    assert 'bar stuff 1' == bar_options['STUFF_1']
    assert 'bar stuff 2' == bar_options['STUFF_2']
    foo_options = app.config.get_namespace('FOO_', trim_namespace=False)
    assert 2 == len(foo_options)
    assert 'foo option 1' == foo_options['foo_option_1']
    assert 'foo option 2' == foo_options['foo_option_2']
    bar_options = app.config.get_namespace('BAR_', lowercase=False, trim_namespace=False)
    assert 2 == len(bar_options)
    assert 'bar stuff 1' == bar_options['BAR_STUFF_1']
    assert 'bar stuff 2' == bar_options['BAR_STUFF_2']
