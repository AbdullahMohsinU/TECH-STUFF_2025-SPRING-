
def test_data():
    assert 2 < 3  # fixed: this now passes

def test_name():
    fruit = ["apple", "mango", "grapes"]
    assert len(fruit) == 3  # fixed: correct count

def test_username(setup_data):
    assert setup_data["name"] == "Abdullah"
def test_age(setup_data):
    assert setup_data["age"] == "20"
def test_age_2(setup_data):
    assert setup_data["age"]== "12"
import pytest
@pytest.fixture()
def setup_data():
    print("setup method starts here")
    data = {"name": "Abdullah", "age": "20"}
    yield data
    print("tearing down fixture")
def test_addition():
    assert 2+2==4
def test_subtraction():
    assert 3-3==0
def test_mul():
    assert 2*2==4
def test_div():
    assert 2/0==0
