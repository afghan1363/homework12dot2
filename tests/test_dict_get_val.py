import pytest
from utils.dict import get_val
@pytest.fixture
def dict_for_test():
    return {"lang": "Python", "version": "3.11"}
# dict_for_test = {"lang": "Python", "version": "3.11"}


def test_get_val(dict_for_test):
    assert get_val(dict_for_test, "lang") == "Python"
    assert get_val(dict_for_test, "version") == "3.11"
    assert get_val(dict_for_test, "weather on monday") == "git"
    assert get_val(dict_for_test, "weather on monday", "are you crazy?") == "are you crazy?"
