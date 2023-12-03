import math

def part_1(input_text):
    symbols_positions = set()
    numbers = []

    for row_index, row in enumerate(input_text):
        current_number_characters = []
        start_column = None
        for column_index, character in enumerate(row):
            if character.isnumeric():
                current_number_characters.append(character)
                if start_column is None:
                    start_column = column_index
            else:
                if current_number_characters:
                    current_number = int(''.join(current_number_characters))
                    current_number_characters = []
                    numbers.append(((row_index, start_column), current_number))
                    start_column = None
                if character != "." and character != "\n":
                    symbols_positions.add((row_index, column_index))

    running_sum = 0
    for (row, column), number in numbers:
        found_adjacent_symbol = False
        #print((row, column, number))
        for column_offset in range(len(str(number))):
            # This is lazy - we can be slightly smarter and only check left/right
            # if we're at the ends, but meh...
            candidate_locations = (
                ((row - 1), column + column_offset - 1), # Above left
                ((row - 1), column + column_offset), # Above
                ((row - 1), column + column_offset + 1), # Above right
                ((row), column + column_offset + 1), # Right
                ((row + 1), column + column_offset + 1), # Below right
                ((row + 1), column + column_offset), # Below
                ((row + 1), column + column_offset - 1), # Below left
                ((row), column + column_offset - 1), # Left
            )

            for candidate_column, candidate_row in candidate_locations:
                if candidate_column < 0:
                    continue
                if candidate_row < 0:
                    continue
                if (candidate_column, candidate_row) in symbols_positions:
                    found_adjacent_symbol = True
                    break

        if not found_adjacent_symbol:
            print(f"Not Part: {number}")
        else:
            running_sum += number

    print(running_sum)

def part_2(input_text):
    stars = dict()
    numbers = []

    for row_index, row in enumerate(input_text):
        current_number_characters = []
        start_column = None
        for column_index, character in enumerate(row):
            if character.isnumeric():
                current_number_characters.append(character)
                if start_column is None:
                    start_column = column_index
            else:
                if current_number_characters:
                    current_number = int(''.join(current_number_characters))
                    current_number_characters = []
                    numbers.append(((row_index, start_column), current_number))
                    start_column = None
                if character == "*":
                    stars[(row_index, column_index)] = set()

    for (row, column), number in numbers:
        found_adjacent_symbol = False
        #print((row, column, number))
        for column_offset in range(len(str(number))):
            # This is lazy - we can be slightly smarter and only check left/right
            # if we're at the ends, but meh...
            candidate_locations = (
                ((row - 1), column + column_offset - 1), # Above left
                ((row - 1), column + column_offset), # Above
                ((row - 1), column + column_offset + 1), # Above right
                ((row), column + column_offset + 1), # Right
                ((row + 1), column + column_offset + 1), # Below right
                ((row + 1), column + column_offset), # Below
                ((row + 1), column + column_offset - 1), # Below left
                ((row), column + column_offset - 1), # Left
            )

            for candidate_column, candidate_row in candidate_locations:
                if candidate_column < 0:
                    continue
                if candidate_row < 0:
                    continue
                if (candidate_column, candidate_row) in stars:
                    stars[(candidate_column, candidate_row)].add((candidate_row, candidate_column, number))

    running_sum = 0
    for (row, column), adjacent_numbers in stars.items():
        count_adjacent = len(adjacent_numbers)
        if count_adjacent == 2:
            print(f"Gear ({row}, {column})")
            running_sum += math.prod([x[2] for x in adjacent_numbers])
        else:
            print(f"Not a gear ({row}, {column}) - {count_adjacent} adjacent: {','.join(map(str, adjacent_numbers))}")

    print(running_sum)

if __name__ == "__main__":
    example = (
        "467..114..",
        "...*......",
        "..35..633.",
        "......#...",
        "617*......",
        ".....+.58.",
        "..592.....",
        "......755.",
        "...$.*....",
        ".664.598..",
    )
    #part_1(example)
    #with open("input") as input_file:
    #    part_1(input_file)
    #part_2(example)
    with open("input") as input_file:
        part_2(input_file)
