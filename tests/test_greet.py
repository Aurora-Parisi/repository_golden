from lib.greet import greet

def test_name_return_greeting():
    result = greet("Aurora")
    assert result == "Hello, Aurora!"
