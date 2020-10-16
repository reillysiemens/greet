from greet import greet


def test_greet():
    assert greet(name="Tucker") == "Hello, Tucker!"
