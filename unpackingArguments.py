"""
*args =  *args in function definitions in Python is used to pass a variable number of arguments to a function.
        It is used to pass a non-keyworded(positional arguments), variable-length argument list.
**kwargs = *kwargs in function definitions in Python is used to pass a keyworded, variable-length argument list.
            We use the name kwargs with the double star.
            The reason is that the double star allows us to pass through keyword arguments.
**kwargs stands for keyword arguments.
  The only difference from args is that it uses keywords and returns the values in the form of a dictionary.
"""


def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total *= arg
    return total


print(multiply(1, 3, 5, 7, 9))


def add(x, y):
    return x + y


nums = [3, 4]
print(add(*nums))

nums = {"x": 3, "y": 4}
print(add(**nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 5, 7, operator="*"))


def named(**kwargs):
    print(kwargs)


# passing keyword arguments will return dictionary by using kwargs
named(name="Bob", age=25)

details = {"name": "Bob", "age": 25}
named(**details)


def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg} : {value}")


print_nicely(**details)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 3, 4, 5, name="Kushi", age=2)
