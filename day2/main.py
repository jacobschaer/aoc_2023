import re

example = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

def parse_line(line):
    title, data = line.split(":")
    game, game_number = title.split(" ")
    assert game == "Game"
    groups = data.split(';')
    rounds = []
    for group in groups:
        round = {}
        for count_color in group.split(','):
            number, color = count_color.strip().split(' ')
            number = int(number)
            round[color] = number
        rounds.append(round)
    return int(game_number), rounds


def part_1(lines):
    target = {
        'red' : 12,
        'green' : 13,
        'blue' : 14
    }
    game_sums = 0
    for line in lines:
        game_number, rounds = parse_line(line)
        possible = True
        for round in rounds:
            total_seen = 0
            for color, count in round.items():
                if count > target[color]:
                    possible = False
                    break
                total_seen += count
            if total_seen > sum(target.values()):
                print(f"Game: {game_number} is not possible")
                possible = False
                break
            if not possible:
                print(f"Game: {game_number} is not possible")
                break
        if possible:
            print(f"Game: {game_number}: is possible")
            game_sums += game_number

    print(game_sums)

def part_2(lines):
    from functools import reduce
    from operator import mul
    power_sums = 0
    for line in lines:
        game_number, rounds = parse_line(line)
        color_mins = {}
        for round in rounds:
            for color, count in round.items():
                if color not in color_mins or count >= color_mins[color]:
                    color_mins[color] = count

        power = reduce(mul, color_mins.values())
        print(color, count, power)
        power_sums += power
    print(power_sums)

if __name__ == "__main__":
    #part_2(example)
    with open("input") as input_file:
        part_2(input_file)
