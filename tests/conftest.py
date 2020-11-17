import pytest
from restapi import app


@pytest.yield_fixture(scope='function')
def test_client():
    return app.test_client()
