friends = ["Rolf", "john", "Anne"]

for friend in enumerate(friends, start=1) :
    print(friend)

print(list(enumerate(friends, start=1)))
print(dict(enumerate(friends, start=1)))