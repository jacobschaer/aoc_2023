import itertools
import sys
from functools import cache

def recount_groups(line):
    groups = []
    count = 0
    for character in line:
        if character == "." and count > 0:
            groups.append(count)
            count = 0
        elif character == "#":
            count += 1
    if count > 0:
        groups.append(count)
    return groups

def part1(input_text):
    arrangements = 0

    for line in input_text:
        graph, counts = line.strip().split(" ")
        counts = [int(x) for x in counts.split(",")]
        num_hashes = graph.count("#")
        num_questions = graph.count("?")
        question_positions = [i for i, x in enumerate(graph) if x == "?"]
        for new_hash_positions in itertools.combinations(question_positions, sum(counts) - num_hashes):
            #print(new_hash_positions)
            new_graph = []
            for i, x in enumerate(graph):
                if i in new_hash_positions:
                    new_graph.append("#")
                elif x == "?":
                    new_graph.append(".")
                else:
                    new_graph.append(x)
            for hash_position in new_hash_positions:
                new_graph[hash_position] = "#"
            #print(new_graph)
            #print(recount_groups(new_graph), counts)
            if recount_groups(new_graph) == counts:
                arrangements += 1

    print(arrangements)

def part2(input_text):
    @cache
    def count(characters, remaining, current_group_count=0):
        #print(characters, remaining, current_group_count)
        if not characters:
            if not remaining:
                return 1
            else:
                return 0
        current_character = "."
        current_character = characters[0]
        current_remaining = 0
        try:
            current_remaining = remaining[0]
        except IndexError:
            pass
        if current_character == ".":
            if current_group_count == 0:
                return count(characters[1:], remaining, current_group_count)
            elif current_group_count != current_remaining:
                return 0
            else:
                return count(characters[1:], remaining[1:], 0)
        elif current_character == "#":
            return count(characters[1:], remaining, current_group_count + 1)
        else:
            return count("." + characters[1:], remaining, current_group_count) + \
                   count("#" + characters[1:], remaining, current_group_count)

    total = 0
    for line in input_text:
        graph, counts = line.strip().split(" ")
        graph = "?".join([graph for _ in range(5)])
        counts = ",".join([counts for _ in range(5)])
        counts = tuple(int(x) for x in counts.split(","))
        subtotal = count(graph + ".", counts)
        print(subtotal)
        total += subtotal

    print(total)

if __name__ == "__main__":
    sys.setrecursionlimit(99999999)
    #print(recount_groups("....###.##.#.##"))
    with open("input.txt") as input_file:
        part2(input_file)