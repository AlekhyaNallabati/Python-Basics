"""
    ***In this file, we got to know about lists and their functions***

Lists -  list is used to store collections of data in a single variable
-- To create a list we use square brackets, and inside the list we put different values separated by comas
-- Lists are heterogeneous in nature, we can store different data types in list
-- we can also have lists in a list
-- Best practice is to be sure that the variable name and elements of the list should be relevant
"""

friends = ["Rolf", "Bob", "Anne"]
# Indices:    0       1        2

# Accesing the elements using their indices #
print(friends[0])  # Rolf (0 --> first element)
print(friends[1])  # Bob (1 --> Second element)
print(friends[2])  # Anne (2 --> Third element)

friends_age = [["Rolf", 23], ["Bob", 24], ["Anne", 25]]

print(friends_age[1])
print(friends_age[0][1])  # 23
print(friends_age[1][0])  # Bob
print(friends_age[2][1])  # 25

# operation in lists #
print(len(friends))  # gives length of the list

friends.append("Charlie")  # add the element at the end of the list
print(friends)  # ['Rolf', 'Bob', 'Anne', 'Charlie']

friends.remove("Bob")  # removes the element from the list
print(friends)  # ['Rolf', 'Anne', 'Charlie']

friends_age.remove(["Anne", 25])
print(friends_age)  # [['Rolf', 23], ['Bob', 24]]

# Joining Lists #

my_friends = ", ".join(friends)
print(f"My friends are {my_friends}.")

############################################################################

# Slicing is the process of getting a part of the list or other iterable(list, tuple, string)
friends = ["Rolf", "Adam", "Smith", "Charlie", "Jen"]
print(friends[2:4])  # prints from indices 2,3 , skips 4(4 will not execute)
print(friends[1:])   # prints everything except indices 0
print(friends[:1])   # prints until indices 4, skips 4
print(friends[-2:])  # indices starts from right to left
print(friends[:-2])
