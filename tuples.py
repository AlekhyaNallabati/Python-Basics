"""
        **In this file, we got to know about tuples and their functions**
Tuples -  Tuple is used to store collections of data in a single variable
-- To create a Tuples we use curved brackets, and inside the Tuples we put different values separated by comas
-- A tuple is a collection which is ordered and unchangeable.
"""

friends = ("Rolf", "Bob", "Anne")
# Indices:    0       1        2

            # SLICING #
print(friends[0])  # Rolf (0 --> first element)
print(friends[1])  # Bob (1 --> Second element)
print(friends[2])  # Anne (2 --> Third element)

friends_age = (("Rolf", 23), ("Bob", 24), ["Anne", 25])
print(friends_age[1])
print(friends_age[0][1])  # 23
print(friends_age[1][0])  # Bob
print(friends_age[2][1])

            # operations in tuples #
print(len(friends))  # gives length of the tuple
""" As tuples are unchangeable, we cannot use append function to it, we need to declare another variable and add 
element to the tuple
"""
friends = friends + ("Charlie", )
print(friends)