"""
For this exercise we've provided you with a list of lottery players, and also with 6 random lottery numbers.

Find out the player with the most correct numbers, and print out their winnings and their name.

The random numbers are generated like this (I know we've not looked at the import keyword yet, bear with me on that one!):

import random
lottery_numbers = set(random.sample(range(22), 6))
And the list of players we've given you are:

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 21, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]
Your task is to find who matched the most numbers, and print out a string with their name and the amount they won. For this exercise, assume there will only be 1 winner. Don't worry about two players matching the same amount of numbers.

For example:

Jen won 1000.

The winnings are calculated with this formula:

winnings = 100 ** len(numbers_matched)
"""
import random


lottery_numbers = set(random.sample(list(range(22)), 6))


players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

players_name = [players[i]["name"] for i in range(len(players))]
#print(players_name)

numbers = [players[i]["numbers"] for i in range(len(players))]
numbers_matched = [lottery_numbers.intersection(numbers[i]) for i in range(len(numbers))]
len_numbers_matched = []

for n in numbers_matched:
    len_numbers_matched.append(len(list(n)))
print(len_numbers_matched)

final_list = [
    (players_name[i],len_numbers_matched[i])
    for i in range(len(len_numbers_matched))
]
print(final_list)


top_player = max(len_numbers_matched)
print(top_player)

winning = 0
for player in final_list:
    if player[1] >= top_player:
        winning += 100 ** player[1]
        print(f"{player[0]} won {winning}")










