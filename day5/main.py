def part_1(input_text):
    seeds = []
    mappings = {}
    source, destination = None, None
    for line in input_text:
        if line.strip().startswith("seeds:"):
            seeds = [int(x) for x in line[6:].split(" ") if x.strip()]
        elif line.strip().endswith("map:"):
            map_name = line.split(" ")[0]
            source, destination = map_name.split('-to-')
            mappings[source] = {destination: []}
        else:
            numbers = [int(x) for x in line.split(" ") if x.strip()]
            if numbers:
                dest_start, source_start, range_length = numbers
                mappings[source][destination].append((dest_start, source_start, range_length))

            
    #print(seeds)
    #print(mappings)
    locations = []
    for seed in seeds:
        current_unit = 'seed'
        current_value = seed
        print(seed)
        while current_unit != 'location':
            next_unit, next_map = next(iter(mappings[current_unit].items()))
            current_unit = next_unit
            for (dest_start, source_start, range_length) in next_map:
                offset = current_value - source_start
                if 0 <= offset <= range_length:
                    current_value = dest_start + offset
                    break
            print(current_unit, current_value)
        locations.append(current_value)
        print("-------")

    print(min(locations))

def convert_unit(mappings, value, source_unit, dest_unit):
    current_unit = source_unit
    current_value = value
    while current_unit != dest_unit:
        next_unit, next_map = next(iter(mappings[current_unit].items()))
        current_unit = next_unit
        for (dest_start, source_start, range_length) in next_map:
            offset = current_value - source_start
            if 0 <= offset <= range_length:
                current_value = dest_start + offset
                break
    return current_value


def part_2(input_text):
    seed_ranges = []
    forward_mappings = {}
    reverse_mappings = {}
    source, destination = None, None
    for line in input_text:
        if line.strip().startswith("seeds:"):
            seed_line = [int(x) for x in line[6:].split(" ") if x.strip()]
            for start_seed, num_seeds in zip(*(iter(seed_line),) * 2):
                seed_ranges.append((start_seed, num_seeds))
            seed_ranges.sort()
            
        elif line.strip().endswith("map:"):
            map_name = line.split(" ")[0]
            source, destination = map_name.split('-to-')
            forward_mappings[source] = {destination: []}
            reverse_mappings[destination] = {source: []}
        else:
            numbers = [int(x) for x in line.split(" ") if x.strip()]
            if numbers:
                dest_start, source_start, range_length = numbers
                forward_mappings[source][destination].append((dest_start, source_start, range_length))
                reverse_mappings[destination][source].append((source_start, dest_start, range_length))

    # Some unit tests
    #for input, output in ((79, 82), (14, 43), (55, 86), (13, 35)):
    #    print(input, output)
    #    print(convert_unit(forward_mappings, input, 'seed', 'location'))
    #    print(convert_unit(reverse_mappings, output, 'location', 'seed'))

    criticals_points = {}

    # Build up critical points top to bottom - we exploit the fact that the mapping is linear, so we need to find
    # find all points in the pre-image that correspond to local minima in the image. So, work through the conversions
    # one at a time using the endpoints of its own range plus the converted inputs of the parent functions range.
    # When we get to the final image we now know all the "interesting" bits and simply need to map these all the way
    # back to the image and we will have found all possible minima.
    current_unit = 'seed'
    while current_unit != 'location':
        next_unit, next_map = next(iter(forward_mappings[current_unit].items()))
        for (dest_start, source_start, range_length) in next_map:
            # Add all the source points to critical points
            if not current_unit in criticals_points:
                criticals_points[current_unit] = set([0])
            if not next_unit in criticals_points:
                criticals_points[next_unit] = set([0])
            for value in (source_start - 1, source_start, source_start + range_length, source_start + range_length + 1):
                if value >= 0:
                    criticals_points[current_unit].add(value)

        for critical_point in criticals_points[current_unit]:
            criticals_points[next_unit].add(convert_unit(forward_mappings, critical_point, current_unit, next_unit))
        current_unit = next_unit

    # Convert bottom to top
    critical_mappings = set()
    critical_mappings.add((0, convert_unit(forward_mappings, 0, 'seed', 'location')))
    for critical_point in criticals_points['location']:
        converted = convert_unit(reverse_mappings, critical_point, 'location', 'seed')
        critical_mappings.add((converted, critical_point))

    critical_mappings = list(critical_mappings)
    critical_mappings.sort()
    print(critical_mappings)

    # Now that we have all the seeds that correspond to local minima, we need only check to see if any of those
    # happen to be in our ranges, as well as the bounds of the range. This greatly reduces the search space
    best_mapped = None 
    for start_seed, num_seeds in seed_ranges:
        candidate = convert_unit(forward_mappings, start_seed, 'seed', 'location')
        #print(start_seed, candidate)
        if best_mapped is None or candidate < best_mapped[1]:
            best_mapped = start_seed, candidate

        candidate = convert_unit(forward_mappings, start_seed + num_seeds, 'seed', 'location')
        #print(start_seed + num_seeds, candidate)
        if candidate < best_mapped[1]:
            best_mapped = start_seed + num_seeds, candidate

        for critical_mapping in critical_mappings:
            if critical_mapping[0] in range(start_seed, start_seed + num_seeds):
                if critical_mapping[1] <= best_mapped[1]:
                    best_mapped = critical_mapping
    
    print(best_mapped)

if __name__ == "__main__":
    example = (
        "seeds: 79 14 55 13",
        "",
        "seed-to-soil map:",
        "50 98 2",
        "52 50 48",
        "",
        "soil-to-fertilizer map:",
        "0 15 37",
        "37 52 2",
        "39 0 15",
        "",
        "fertilizer-to-water map:",
        "49 53 8",
        "0 11 42",
        "42 0 7",
        "57 7 4",
        "",
        "water-to-light map:",
        "88 18 7",
        "18 25 70",
        "",
        "light-to-temperature map:",
        "45 77 23",
        "81 45 19",
        "68 64 13",
        "",
        "temperature-to-humidity map:",
        "0 69 1",
        "1 0 69",
        "",
        "humidity-to-location map:",
        "60 56 37",
        "56 93 4",
    )
    #part_1(example)
    #with open("input") as input_file:
    #    part_1(input_file)
    #part_2(example)
    with open("input") as input_file:
        part_2(input_file)
