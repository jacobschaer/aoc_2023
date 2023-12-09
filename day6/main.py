def part_1(input_text):
    times = []
    distances = []
    for line in input_text:
        if line.startswith("Time"):
            times = [int(x) for x in line.split(":")[1].strip().split(" ") if x.strip()]
        elif line.startswith("Distance"):
            distances = [int(x) for x in line.split(":")[1].strip().split(" ") if x.strip()]
    print(times,distances)

    product = 1
    for i in range(len(times)):
        race_time = times[i]
        best_distance = distances[i]
        ways_to_win = 0
        for time_held in range(1, race_time):
            distance = time_held * (race_time - time_held)
            if distance > best_distance:
                ways_to_win += 1
        product *= ways_to_win
    print(product)

def part_2(input_text):
    race_time = None
    best_distance = None
    for line in input_text:
        if line.startswith("Time"):
            race_time = int(line.split(":")[1].replace(" ",""))
        elif line.startswith("Distance"):
            best_distance = int(line.split(":")[1].replace(" ",""))
    print(race_time,best_distance)

    ways_to_win = 0
    for time_held in range(1, race_time):
        distance = time_held * (race_time - time_held)
        if distance > best_distance:
            ways_to_win += 1
    print(ways_to_win)



if __name__ == "__main__":
    example = (
        "Time:      7  15   30",
        "Distance:  9  40  200",
    )
    #part_1(example)
    #with open("input") as input_file:
    #    part_1(input_file)
    #part_1(example)
    with open("input") as input_file:
        part_2(input_file)
