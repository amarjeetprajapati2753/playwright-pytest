import pytest

@pytest.fixture(autouse=True)
def setup():
    print("\nBrowser setup")
    yield
    print("\nBrowser teardown")
