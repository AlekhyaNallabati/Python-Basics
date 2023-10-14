"""
This file will talk about strings and formatting the strings
"""

String_with_quotes = "Hello, it's me."
mutltiline_string = """Hello world.

My name is kriti. I'm a good girl
"""
print(mutltiline_string)

name = "kriti Nayana"
age = 2

myAge = f"My age is {age}yrs"  # f-string
print(myAge)

greeting = "How are you," + name  # concatenation
my_age = "My age is " + str(2) + "yrs"  # concatenating str and num is not possible
print(my_age)

greeting = "How are you,{} ?"

my_greeting = "How are you,{}".format(name)  # formatting using variables
print(my_greeting)

my_greet = "How are you,{}".format("Kushi")  # customised formatting
print(my_greet)

final_greeting = greeting.format(name)  # formatting using template(greeting)
print(final_greeting)

name = "Kushi"
user_name = input("Please enter your name: ")
print(name.title())
print(name.lower())
print(name.upper())
if user_name.title() == name.title():
    print("Got you!")


