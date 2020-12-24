import os

with open("input.txt") as f:
    decks = f.read().split("\n\n")

p1 = decks[0].split("\n")
p2 = decks[1].split("\n")

p1, p2 = [int(i) for i in p1 if "Player" not in i], [
    int(i) for i in p2 if "Player" not in i
]


def play_game(p1, p2, all_rounds, round_num):
    while len(p1) >= 0 and len(p2) >= 0:
        if p1 == []:
            return 0, p2
        if p2 == []:
            return 1, p1
        else:
            # print("-- ROUND", round_num, " --")
            round_num += 1
            # print("Decks:", p1, p2)
            if (tuple(p1), tuple(p2)) in all_rounds:
                # print("Player 1 won as:", (tuple(p1), tuple(p2)) in all_rounds)
                return 1, p1
            all_rounds.add((tuple(p1), tuple(p2)))
            round = (p1.pop(0), p2.pop(0))

            # print("Plays:", round[0], round[1])
            if len(p1) >= round[0] and len(p2) >= round[1]:
                # print("--- Playing Subgame --- ")
                winner, _ = play_game(
                    p1[0 : round[0]].copy(),
                    p2[0 : round[1]].copy(),
                    set(),
                    1,
                )
                if winner:
                    # print("sub_game_winner: p1")
                    p1.append(round[0])
                    p1.append(round[1])
                else:
                    # print("sub_game_winner: p2")
                    p2.append(round[1])
                    p2.append(round[0])
            else:
                # print("sub_game_not_playable - winner: ", end="")
                if round[0] > round[1]:
                    # print("p1")
                    p1.append(round[0])
                    p1.append(round[1])
                else:
                    # print("p2")
                    p2.append(round[1])
                    p2.append(round[0])


total = 0
for i, val in enumerate(reversed(play_game(p1, p2, set(), 1)[1])):
    total += (i + 1) * val
print(total)