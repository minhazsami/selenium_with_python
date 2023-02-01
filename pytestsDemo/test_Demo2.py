import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello! Good Morning")


def test_seconProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition doesn't match"
