lottery_numbers = {13, 21, 22, 5, 8}
players = [
    {
        'name': 'Kushi',
        'numbers': {5, 8, 13, 15, 20}
    },
    {
        'name': 'Kriti',
        'numbers': {13, 14, 22, 8, 21}
    }

]
player1_name = players[0]["name"]
player2_name = players[1]["name"]

player1_numbers = players[0]["numbers"]
player2_numbers = players[1]["numbers"]

player1_luck = len(player1_numbers.intersection(lottery_numbers))
player2_luck = len(player2_numbers.intersection(lottery_numbers))

player1_lottery_luck = f"Player {player1_name} got {player1_luck} numbers right."
player2_lottery_luck = f"Player {player2_name} got {player2_luck} numbers right."
print(player1_lottery_luck)
print(player2_lottery_luck)