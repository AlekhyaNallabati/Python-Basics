"""
List Comprehensions are a feature of python that allows us to create new list very succinctly(in a brief and explained manner)
"""
numbers= [5, 3, 8]
doubled_number = []

#using for loop
for num in numbers:
    doubled_number.append(num * 2)
print(doubled_number)

# using list comprehension
doubled_number = [num * 2 for num in numbers]
print(doubled_number)

friends = ["Rolf", "Sam", "Santosh", "Saurabh", "Jen"]
Starts_s = []

# using for loop
for friend in friends:
    if friend.startswith("S"):
        Starts_s.append(friend)
print(Starts_s)

# using list comprehension
Starts_s = [friend for friend in friends if friend.startswith("S")]
print(Starts_s)

ages = [22, 25, 27, 35, 20]
odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)

# Nested comprehension
friends = ["Rolf", "ruth", "charlie", "jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# list comprehension
present_friends = [
    name.title()
    for name in guests
    if name.lower() in [f.lower() for f in friends]
]
print(present_friends)

# set comprehension
friends_lower = {name.lower() for name in friends}
guests_lower = {name.lower() for name in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print(present_friends)

# Dictionary Comprehensions

friends = ["Rolf", "Jen", "Charlie", "Anne"]
time_since_seen = [3, 4, 5, 7]

long_timers = {
    friends[i] : time_since_seen[i]
    for i in range(len(time_since_seen))
}
print(long_timers)

# Zip function
long_timers = dict(zip(friends, time_since_seen))
print(long_timers)