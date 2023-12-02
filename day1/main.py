from typing import Iterable

def line_value(line : str):
    numbers = [x for x in line if x.isnumeric()]
    return int(numbers[0] + numbers[-1])

def part_1(input_lines : Iterable[str]):
    sum = 0
    for line in input_lines:
        value = line_value(line)
        print(line, value)
        sum += value
    print(sum)

def part_2(input_lines : Iterable[str]):
    replacements = [
            ("one", 1),
            ("two", 2),
            ("three", 3),
            ("four", 4),
            ("five", 5),
            ("six", 6),
            ("seven", 7),
            ("eight", 8),
            ("nine", 9)
    ]
    lengths = [len(x[0]) for x in replacements]
    min_group_length = min(lengths)
    max_group_length = max(lengths)
    sum = 0
    for line in input_lines:
        filtered_line = []
        for start_index in range(len(line)):
            found = False
            for src, dst in replacements:
                if line[start_index:].startswith(src):
                    filtered_line.append(str(dst))
                    start_index += len(src)
                    found = True
                    break
            if not found:
                filtered_line.append(line[start_index])
                    

        value = line_value(''.join(filtered_line))
        print(line, value)
        sum += value
    print(sum)


if __name__ == '__main__':
    input = (
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    )

    #input = ("1abc2n",
    #         "a1b2c3d4e5f",
    #         "treb7uchet",
    #         "pqr3stu8vwx",)
    #part_2(input)
    with open("input1") as input_file:
        part_2(input_file)
