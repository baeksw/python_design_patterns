from models import Url

import pytest


@pytest.fixture
def instance():
    return Url()


def test_increment_string(instance):

    instance.shorten("abcdefg")

    assert False, "test_increment_string"