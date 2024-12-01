# A for Rock
# B for Paper
# C for Scissors

# X means you need to lose
# Y means you need to end the round in a draw
# Z means you need to win

# The score for a single round is the score for
# the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).


shape_score = {'A': 1, 'B': 2, 'C': 3}
outcome_score = {'X': 0, 'Y': 3, 'Z': 6}

loosing_shape = {'A': 'B', 'B': 'C', 'C': 'A'}
winning_shape = {'A': 'C', 'B': 'A', 'C': 'B'}


def read_plays():
    with open('./2022/day2/input1.txt', 'r') as file:
        lines = file.readlines()
    return [plays.split() for plays in lines]


def choose_shape(play):
    # win
    if play[1] == 'X':
        return winning_shape[play[0]]
    # draw
    if play[1] == 'Y':
        return play[0]
    # lose
    if play[1] == 'Z':
        return loosing_shape[play[0]]


def compute_score(play):
    shape = choose_shape(play)
    return shape_score[shape] + outcome_score[play[1]]


def main():
    score = 0
    for play in read_plays():
        score = score + compute_score(play)
    print(score)


if __name__ == '__main__':
    main()
