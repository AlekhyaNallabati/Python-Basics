"""
        *In this file, we got to know about sets*
Sets - set is used to store collections of data in a single variable
To create a set we use curley braces,and inside the set we put different values separated by comas
A set is a collection which is unordered and do not allow duplicates
"""

art_friends = {"Rolf", "Bob", "Jen"}
science_friends = {"Jen", "Charlie"}

"""
we can't access the elements in set using indices as set is unordered
we can use add operation to add element to set
"""

art_friends.add("Anne")  # {'Rolf', 'Anne', 'Bob', 'Jen'}
print(art_friends)

art_friends.remove("Bob")
print(art_friends)  # {'Rolf', 'Anne', 'Jen'}

# Advanced Operations in sets #

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
print(art_but_not_science)  # {'Rolf', 'Anne'}
print(science_but_not_art)  # {'Charlie'}

not_in_both = science_friends.symmetric_difference(art_friends)
print(not_in_both)  # {'Rolf', 'Charlie', 'Anne'}

art_and_science = science_friends.intersection(art_friends)
print(art_and_science)  # {'Jen'}

