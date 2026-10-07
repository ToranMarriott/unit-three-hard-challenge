from lib.age_checker import *
import pytest

def test_access_granted():
    assert check_age("2000-01-01") == "Access Granted!"

def test_access_denied():
    assert check_age("2020-01-01") == "Access Denied, You are 6, Access is restricted for under 16s!"

def test_empty_string_throws_error():
    with pytest.raises(Exception) as e:
        check_age("")
    error_message = str(e.value)
    assert error_message == "No date of birth inputted"

def test_incorrectly_formatted_date():
    with pytest.raises(Exception) as e:
        check_age("20/20/2019")
    error_message = str(e.value)
    assert error_message == "Date of birth incorrectly formatted (YYYY-MM-DD)"