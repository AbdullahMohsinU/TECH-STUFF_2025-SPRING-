import pytest

@pytest.fixture
def setup_data():
    print("setup string start here")
    text = "Pytest is awesome!"
    yield text
    print("tearing down here")

def test_text(setup_data):
    assert setup_data.find("is") != -1
def test_length(setup_data):
    assert len(setup_data) == 18