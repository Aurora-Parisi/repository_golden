import pytest 
from lib.password_checker import PasswordChecker

#check if password is exaclty 8 char = valid
#def your test
def test_password_length_is_eight_char():
    #create an instance of the class PasswordChecker
    checker = PasswordChecker()
    #define a password that meets the criteria
    #in this case 'password' is 8 characters so it's valid
    password = "password"
    #call the check method on the checker object
    result = checker.check(password)
    #expect the function to return true 
    assert result is True

def test_password_is_over_eight_char():
    checker = PasswordChecker()
    password = "long_password"

    result = checker.check(password)
    assert result is True 

def test_password_is_less_than_eight_char():
    checker = PasswordChecker()
    password = "short"
    with pytest.raises(Exception) as e:
        checker.check(password)
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."

   