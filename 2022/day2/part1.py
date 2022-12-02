# A for Rock
# B for Paper
# C for Scissors

# X for Rock
# Y for Paper
# Z for Scissors

# The score for a single round is the score for
# the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

def read_plays():
    with open('./2022/day2/input1.txt', 'r') as file:
        lines = file.readlines()
    return [plays.split() for plays in lines]


def score_for_shape(shape):
    if shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return 3
    else:
        raise Exception('invalid shape!')


def score_for_round(play):
    # draw
    if play in [['A', 'X'], ['B', 'Y'], ['C', 'Z']]:
        return 3
    # win
    if play in [['A', 'Y'], ['B', 'Z'], ['C', 'X']]:
        return 6
    # lost
    return 0


def compute_score(play):
    return score_for_shape(play[1]) + score_for_round(play)


def main():
    score = 0
    for play in read_plays():
        score = score + compute_score(play)
    print(score)


if __name__ == '__main__':
    main()
