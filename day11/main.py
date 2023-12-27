import pprint
import itertools

def distances(graph):
    distances = {}
    for row_index  in range(len(graph)):
        for column_index in range(len(graph[row_index])):
            if graph[row_index][column_index] == "#":
                distances[(row_index, column_index)] = {}
    
    for source_row_index, source_column_index in distances:
        for target_row_index, target_column_index in distances:
            if source_row_index == target_row_index and source_column_index == target_column_index:
                continue
            else:
                distance = abs(target_row_index - source_row_index) + abs(target_column_index - source_column_index)
                distances[(source_row_index, source_column_index)][(target_row_index, target_column_index)] = distance
    
    seen = set()
    total = 0
    count = 0

    print(len(distances))
    x = 0
    for i in range(len(distances)):
        x += i

    for source in distances:
        for destination in distances[source]:
            key = tuple(sorted([source, destination]))
            #print(key)
            if key in seen:
                continue
            else:
                seen.add(key)
                total += distances[source][destination]
                count += 1

    assert x == count

    #pprint.pprint(distances)
    print(count)
    print(total)

def part1(input_text):
    expanded = []
    for row in input_text:
        row = row.strip()
        if all(map(lambda x: x == ".", row)):
            #print("Is empty")
            expanded.append([x for x in row])
        expanded.append([x for x in row])
    column = 0
    while column < len(expanded[0]):
        #print(column)
        column_expand = True
        for row in range(len(expanded)):
            if expanded[row][column] != ".":
                column_expand = False
                break
        if column_expand:
            #print("Expanding")
            for row in range(len(expanded)):
                expanded[row].insert(column, ".")
            column += 1
        column += 1

    
    pprint.pprint(expanded)
    distances(expanded)


def part2(input_text):
    row_space = []
    column_space = []
    #dilation = 10000
    dilation = 1000000
    unexpanded = []

    def get_distance(start, finish):
        a, b = sorted((start[0], finish[0]))
        c, d = sorted((start[1], finish[1]))
        return sum(row_space[a:b+1]) + sum(column_space[c:d+1]) -2

    for row in input_text:
        row = row.strip()
        if all(map(lambda x: x == ".", row)):
            row_space.append(dilation)
        else:
            row_space.append(1)
        unexpanded.append([x for x in row])

    for column_index in range(len(unexpanded[0])):
        is_empty = True
        for row in unexpanded:
            if row[column_index] == "#":
                is_empty = False
                break
        if is_empty:
            column_space.append(dilation)
        else:
            column_space.append(1)

    galaxies = []
    for row_index in range(len(unexpanded)):
        for column_index in range(len(unexpanded[row_index])):
            if unexpanded[row_index][column_index] == "#":
                galaxies.append((row_index, column_index))

    #print(galaxies)
    #print(list(itertools.combinations(galaxies, 2)))
    print(sum(map(lambda x: get_distance(x[0], x[1]), itertools.combinations(galaxies, 2))))

if __name__ == "__main__":
    example = (
        "...#......",
        ".......#..",
        "#.........",
        "..........",
        "......#...",
        ".#........",
        ".........#",
        "..........",
        ".......#..",
        "#...#.....",
    )
    #part1(example)
    #with open("input.txt") as input_file:
    #    part1(input_file)
    #part2(example)
    with open("input.txt") as input_file:
        part2(input_file)
