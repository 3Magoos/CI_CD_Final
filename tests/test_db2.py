from shop_app.db import get_db_config

def test_db_conf():
    assert isinstance(get_db_config(), dict)

def test_db_conf_info():
    assert get_db_config() != ""
