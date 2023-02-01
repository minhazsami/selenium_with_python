import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello world")


@pytest.mark.skip
def test_seconProgram():
    msg = "hello"
    assert msg == "hi", "Test failed because msg should be Hello"
