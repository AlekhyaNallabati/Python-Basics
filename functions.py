"""
Function : A function is a block of code that you can run at any point after it has been defined,
            and that produces an output or performs an action.
            Sometimes it can take inputs as well.
Argument : value we pass in to the function
Parameter : Variable that accepts a value inside the function
"""


def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")


greet()

# calculating mpg normally
car = {
    "make": "Ford",
    "model": "Fiesta",
    "Mileage": 23000,
    "fuel_consumed": 460

}

mpg = car["Mileage"] / car["fuel_consumed"]
name = f"{car['make']} {car['model']}"
print(f"{name} does {mpg} miles per gallon")

# calculating mpg using functions

cars = [
    {"make": "Ford", "model": "Fiesta", "Mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "Mileage": 17000, "fuel_consumed": 350},
    {"make": "Ford", "model": "Mazda", "Mileage": 49000, "fuel_consumed": 900},
    {"make": "Ford", "model": "Mini", "Mileage": 31000, "fuel_consumed": 230}
]


def calculate_mpg(car):
    mpg = car["Mileage"] / car["fuel_consumed"]
    return mpg


def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name


def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    print(f"{name} does {mpg} miles per gallon")


for car in cars:
    print_car_info(car)
