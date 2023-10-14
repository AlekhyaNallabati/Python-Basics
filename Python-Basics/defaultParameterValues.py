# default argument should go last
def add(x, y=3):
    total = x + y
    return total


print(add(5))  # takes y = 3 as default
print(add(6, 6))
print(add(x=5, y=2))  # here x and y are named arguments
