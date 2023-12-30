import tqdm

def part1(input_file):
    table = [[y for y in x.strip()] for x in input_file]
    for row_index in range(len(table)):
        for column_index in range(len(table[row_index])):
            if table[row_index][column_index] == "O":
                current_row = row_index
                target_row = current_row - 1
                while target_row >= 0 and table[target_row][column_index] == ".":
                    table[target_row][column_index] = "O"
                    table[current_row][column_index] = "."
                    target_row -= 1
                    current_row -= 1
    total = 0
    for row_index, row in enumerate(table):
        total += (len(table) - row_index) * row.count("O")
        print("".join(row) + " " + str(len(table) - row_index))
    print(total)

def part2(input_file):
    table_string = ""
    num_columns = 0
    for line in input_file:
        num_columns = max(len(line.strip()), num_columns)
        table_string += line
    table_string = table_string.strip()

    cache = dict()
    for i in tqdm.tqdm(range(1000000000)):
        precalculated = cache.get(table_string, None)
        if precalculated is not None:
            table_string = precalculated
        else:
            table = [list(x) for x in table_string.split("\n")]

            # North
            for row_index in range(len(table)):
                for column_index in range(len(table[row_index])):
                    if table[row_index][column_index] == "O":
                        current_row = row_index
                        target_row = current_row - 1
                        while target_row >= 0 and table[target_row][column_index] == ".":
                            table[target_row][column_index] = "O"
                            table[current_row][column_index] = "."
                            target_row -= 1
                            current_row -= 1

            # West
            for column_index in range(len(table[0])):
                for row_index in range(len(table)):
                    if table[row_index][column_index] == "O":
                        current_column = column_index
                        target_column = current_column - 1
                        while target_column >= 0 and table[row_index][target_column] == ".":
                            table[row_index][target_column] = "O"
                            table[row_index][current_column] = "."
                            target_column -= 1
                            current_column -= 1

            # South
            for row_index in reversed(range(len(table))):
                for column_index in range(len(table[row_index])):
                    if table[row_index][column_index] == "O":
                        current_row = row_index
                        target_row = current_row + 1
                        while target_row < len(table) and table[target_row][column_index] == ".":
                            table[target_row][column_index] = "O"
                            table[current_row][column_index] = "."
                            target_row += 1
                            current_row += 1

            # East
            for column_index in reversed(range(len(table[0]))):
                for row_index in range(len(table)):
                    if table[row_index][column_index] == "O":
                        current_column = column_index
                        target_column = current_column + 1
                        while target_column < len(table[0]) and table[row_index][target_column] == ".":
                            table[row_index][target_column] = "O"
                            table[row_index][current_column] = "."
                            target_column += 1
                            current_column += 1

            new_string = "\n".join(["".join(x) for x in table])
            cache[table_string] = new_string
            table_string = new_string

    table = [list(x) for x in table_string.split("\n")]
    total = 0
    for row_index, row in enumerate(table):
        total += (len(table) - row_index) * row.count("O")
        print("".join(row) + " " + str(len(table) - row_index))
    print(total)

if __name__ == "__main__":
    with open("input.txt") as input_file:
        part2(input_file)
        