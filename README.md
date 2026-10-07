# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

>>> age_checker("1960-10-21")
"Access granted!"


## 2. Design the Function Signature

Name: check_age()
Params: string containing date
Returns: message as string allowing or denying access
Side effects: None

Name: get_age()
Params: string containing date
Returns: age as integer
Side effects: None


## 3. Create Examples as Tests


```python
# EXAMPLE

"""
Given a date as a string, returns a message granting access if over 16 y/o
"""
check_age("2000-01-01") => "Access Granted!"

"""
Given a date as a string, returns a message denying access if under 16 y/o
"""
check_age("2020-01-01") => "Access Denied, You are 6, Access is restricted for under 16s!"

"""
Given a empty string, returns a error message
"""
check_age("") => error message

"""
Given a incorrectly formatted string, returns a error message
"""
check_age("20/20/2019") => error message

```


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
