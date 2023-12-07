from functools import reduce
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(f'{dir_path}/input.txt') as file:
    input = file.read()

input = input.split("\n")
updated_input = []
for play in input:
    updated_input.append((play[0], play[-1]))


# A/X : Rock, B/Y : Paper, C/Z : Scissor
# Rock: 1 point, Paper: 2 paper, Scissors: 3 points

dict = {
    'A': 'Rock',
    'X': 'Rock',
    'B': 'Paper',
    'Y': 'Paper',
    'C': 'Scissors',
    'Z': 'Scissors',
}


def check_if_player_2_won_and_give_score_for_round(match) -> int:
    opponent = dict.get(match[0])
    player = dict.get(match[1])
    # Rock vs
    if opponent == 'Rock':
        if player == 'Rock':
            return 1 + 3
        elif player == 'Paper':
            return 2 + 6
        elif player == 'Scissors':
            return 3 + 0
    # Paper vs
    if opponent == 'Paper':
        if player == 'Rock':
            return 1 + 0
        elif player == 'Paper':
            return 2 + 3
        elif player == 'Scissors':
            return 3 + 6
    # Scissors vs
    if opponent == 'Scissors':
        if player == 'Rock':
            return 1 + 6
        elif player == 'Paper':
            return 2 + 0
        elif player == 'Scissors':
            return 3 + 3


# Part one answer
final = sum(map(check_if_player_2_won_and_give_score_for_round, updated_input))
print(final)
