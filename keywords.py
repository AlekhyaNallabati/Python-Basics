"""
Conditionals and comparators
In this file, we got know about and & or keywords
The conditionals evaluate left to right

The "and" keyword works as below
    1.True and True     -   True
    2.True and False    -   False
    3.False and False   -   False
    4.False and True    -   False
--If any of the condition in the statement is False, the result will be False
--If the result of the first condition is false, the "and" keyword will give the result of the first condition
--If the result of the first condition is true, the "and" keyword will give the result of the second condition

The "or" keyword works as below
    1.True or True     -   True
    2.True or False    -   True
    3.False or False   -   False
    4.False or True    -   True
--If any of the condition in the statement is True, the result will be True
--If the result of the first condition is True, the "or" keyword will give the result of the first condition
--If the result of the first condition is False, the "or" keyword will give the result of the second condition
"""

age = 25

and_result = age > 18 and age < 65
print(and_result)

or_result = age > 18 or age > 65
print(or_result)


bool(0)  # False, Zero
bool(13)    # True

bool("")  # False, empty string
bool("Hello")   # True

bool([])  # False, empty list
bool([1, 3, 5])   # True

default_age = 30
age = 0
user_age = age or default_age  # false or true = true
user_age_1 = age and default_age  # false or true = false(0) bool(0)  # False, Zero
print(user_age)
print(user_age_1)