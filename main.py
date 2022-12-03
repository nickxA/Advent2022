# Part 1: A and X = Rock, B and Y = Paper, C and Z = Scissors
# Part 2: X means lose, Y means draw, Z means win

def get_shape_score(line):
    # Expect a string with opponent move, space, our move. Part 1 only.
    shape_scores = {"X": 1, "Y": 2, "Z": 3}
    our_move = line[-1]
    return shape_scores[our_move]


def get_outcome_score(line):
    outcome_scores = {
        "A X": 3,  # Loss v Rock, played scissors, 0 points for loss 3 points for shape
        "A Y": 4,  # Draw v Rock, played rock, 3 points for draw 1 point for shape
        "A Z": 8,  # Win v Rock, played paper, 6 points for win 2 points for shape
        "B X": 1,  # Lose v Paper, played rock, 0 points for loss 1 point for shape
        "B Y": 5,  # Draw vs Paper, played paper, 3 points for draw 2 points for shape
        "B Z": 9,  # Win vs Paper, played scissors, 6 points for win 3 points for shape
        "C X": 2,  # Lose vs Scissors, played paper, 0 points for loss 2 points for shape
        "C Y": 6,  # Draw vs Scissors, played scissors, 3 points for draw 3 points for shape
        "C Z": 7   # Win vs Scissors, played rock, 6 points for win 1 point for shape
    }
    return outcome_scores[line]


def main():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    print(lines[0])
    total_score = 0
    for line in lines:
        line = line.strip()
        outcome_score = get_outcome_score(line)
        total_score += outcome_score
        print("Line {}, outcome score is {}, total score is now {}.".format(line, outcome_score, total_score))

    print("Final total score by guide is {}.".format(total_score))


if __name__ == "__main__":
    main()
