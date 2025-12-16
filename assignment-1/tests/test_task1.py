import pytest

# Task 1: Fixture with yield
# @pytest.fixture
# def setup():
#     print("Browser setup")
#     yield
#     print("Browser teardown")

# Task 2: Grouping and Skip

@pytest.mark.smoke
def test_smoke_case(setup):
    print("running test_smoke_case")
    # assert True

@pytest.mark.regression
def test_regression_case1(setup):
    print("running test_regression_case")
    # assert True


@pytest.mark.skip(reason="Not required now")
def test_skip_case(setup):
    print("skip test case")
    # assert True
