def extrapolate_forward(history):
    extrapolated_value = 0
    for step in reversed(history[:-1]):
        extrapolated_value = step[-1] + extrapolated_value
    return extrapolated_value

def extrapolate_backward(history):
    print(history)
    extrapolated_value = 0
    for step in reversed(history[:-1]):
        extrapolated_value = step[0] - extrapolated_value
    return extrapolated_value

def build_history(first_line):
    history = [first_line]
    while True:
        new_history = []
        for i in range(len(history[-1]) -1):
            new_history.append(history[-1][i + 1] - history[-1][i])
        history.append(new_history)
        if not any(new_history):
            break
    return history

def part_1(input_text):
    sum = 0
    for line in input_text:
        print("----")
        history = build_history([int(x) for x in line.strip().split(" ")])
        print(history)
        extrapolated = extrapolate_forward(history)
        print(extrapolated)
        sum += extrapolated
    print("Total ", sum)

def part_2(input_text):
    sum = 0
    for line in input_text:
        print("----")
        history = build_history([int(x) for x in line.strip().split(" ")])
        #for line in history:
        #    print(line)
        extrapolated = extrapolate_backward(history)
        print(extrapolated)
        sum += extrapolated
    print("Total ", sum)

if __name__ == "__main__":
    example = (
        "0 3 6 9 12 15",
        "1 3 6 10 15 21",
        "10 13 16 21 30 45",

    )
    #part_1(example)
    #with open("input") as input_file:
    #    part_1(input_file)
    #part_2(example)
    with open("input") as input_file:
        part_2(input_file)
