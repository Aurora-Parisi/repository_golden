import pytest
from lib.present import Present

#when we wrap an item. we get it back when unwrapping

def test_wrap_and_then_unwrap():
    present = Present()
    present.wrap(33)
    assert present.unwrap() == 33

#if we unwrap before wrapping, we get error message

def test_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

# if we try to wrap twice
#an already wrapped present, we get error message

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

# we need to preserve the first wrap thing
