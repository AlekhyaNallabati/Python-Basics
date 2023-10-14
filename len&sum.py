"""
length and sum operators of list
tuples and sets are not the best data types to store the collection of grades
because we cannot add elements to a tuple after declaration
and we cannot duplicate elements of a set
"""

grades = [80, 85, 90, 75]

total = sum(grades)
length = len(grades)

average = total/length
print(average)