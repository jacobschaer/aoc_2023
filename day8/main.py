from math import lcm

def part1(input_text):
    command = []
    map = {}
    entry_point = "AAA"
    for i, line in enumerate(input_text):
        if i == 0:
            for letter in line:
                if letter == "L":
                    command.append(0)
                elif letter == "R":
                    command.append(1)
        elif i > 1:
            index, destinations = line.split("=")
            index = index.strip()
            destinations = [x.strip() for x in destinations.strip()[1:-1].split(",")]
            map[index] = destinations

    print(command)
    print(map)

    element_index = entry_point
    steps = 0
    while element_index != "ZZZ":
        element_index = map[element_index][command[steps % len(command)]]
        steps += 1
        print(element_index)

    print(steps)

def part2(input_text):
    command = []
    map = {}
    entry_point = "AAA"
    for i, line in enumerate(input_text):
        if i == 0:
            for letter in line:
                if letter == "L":
                    command.append(0)
                elif letter == "R":
                    command.append(1)
        elif i > 1:
            index, destinations = line.split("=")
            index = index.strip()
            destinations = [x.strip() for x in destinations.strip()[1:-1].split(",")]
            map[index] = destinations

    print(command)
    print(map)
    elements = [x for x in map if x.endswith("A")]

    # Brute force.. sucks > 15 minutes
    #element_index = entry_point
    #steps = 0
    #all_z = False
    #while not all_z:
    #    all_z = True
    #    for i in range(len(elements)):
    #        if not elements[i].endswith("Z"):
    #            all_z = False
    #        elements[i] = map[elements[i]][command[steps % len(command)]]
    #    if all_z:
    #        break
    #    steps += 1
    #    #print(elements)
    #    if steps % 100000 == 0:
    #        print(steps)

    #print(steps)

    # what we really want is to find the entire circuit for each one
    circuits = {}

    # While not intuitive, it turns out that the Z's are regularly spaced - this is not something
    # one would assume from reading the problem - in fact, in general one would expect that each
    # path would potentially traverse multiple endpoints. But, if we analyze the input and
    # make note of the various times we hit an endpoint in the command queue (ie: we found a loop)
    # we found that all Z's are regularly spaced with no offsets
    for start_element in elements:
        print("-----")
        num_cycles = 0
        num_steps = 0
        matches = set()
        current_element = start_element
        while num_cycles < 4:
            command_index = num_steps % len(command)
            if current_element.endswith("Z"):
                print(f"Match: {current_element} at {num_steps}")
                if not start_element in circuits:
                    circuits[start_element] = num_steps
                if (command_index, current_element) in matches:
                    num_cycles += 1
                else:
                    matches.add((command_index, current_element))
            current_element = map[current_element][command[command_index]]
            num_steps += 1

    # So, we need only find the LCM of the periods
    print(circuits)
    print(lcm(*[x for x in circuits.values()]))


if __name__ == "__main__":
    example1 = (
        "LLR",
        "",
        "AAA = (BBB, BBB)",
        "BBB = (AAA, ZZZ)",
        "ZZZ = (ZZZ, ZZZ)",
    )
    example2 = (
        "RL",
        "",
        "AAA = (BBB, CCC)",
        "BBB = (DDD, EEE)",
        "CCC = (ZZZ, GGG)",
        "DDD = (DDD, DDD)",
        "EEE = (EEE, EEE)",
        "GGG = (GGG, GGG)",
        "ZZZ = (ZZZ, ZZZ)",
    )
    #part1(example1)
    #part1(example2)
    #with open("input") as input_file:
    #    part1(input_file)
    example3 = (
        "LR",
        "",
        "11A = (11B, XXX)",
        "11B = (XXX, 11Z)",
        "11Z = (11B, XXX)",
        "22A = (22B, XXX)",
        "22B = (22C, 22C)",
        "22C = (22Z, 22Z)",
        "22Z = (22B, 22B)",
        "XXX = (XXX, XXX)",
    )
    #part2(example3)
    with open("input") as input_file:
        part2(input_file)
