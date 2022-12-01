from shop_app.db import get_db_config

def test_db_conf():
    assert isinstance(get_db_config(), dict)

def test_db_conf_info():
    assert get_db_config() != ""

def test_db_conf_values():
    values = ["127.0.0.1", "username", None, "example"]
    assert list(get_db_config().values()) == values

def test_db_conf_keys():
    keys = ["host", "user", "password", "database"]
    assert list(get_db_config().keys()) == keys
