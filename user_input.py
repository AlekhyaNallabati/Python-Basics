"""
This file shows how to use input function
"""
my_name = "kushi"
users_name = input("Enter your name : ")
users_age = int(input("Enter your age : "))    # converting a str into int
age_in_months = users_age * 12
output = f"""Users Info :
            Hello {users_name}.
            your age is {age_in_months} months.
            My name is {my_name}."""
print(output)