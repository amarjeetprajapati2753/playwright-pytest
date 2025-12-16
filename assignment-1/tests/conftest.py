import pytest

@pytest.fixture
def setup():
    print("\nBrowser setup")
    yield
    print("\nBrowser teardown")
