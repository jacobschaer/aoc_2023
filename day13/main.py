def part1(input_file):
    charts = []
    chart = []
    for row in input_file:
        row = row.strip()
        if not row:
            charts.append(chart)
            chart = []
        else:
            chart.append(row)
    if chart:
        charts.append(chart)

    count = 0
    for chart_index, chart in enumerate(charts):
        value = 0
        for row_index in range(len(chart) - 1):
            above = row_index
            below = row_index + 1
            is_mirror = True
            while True:
                if above < 0 or below >= len(chart):
                    break
                if chart[above] != chart[below]:
                    is_mirror = False
                    break
                else:
                    above -= 1
                    below += 1
            if is_mirror:
                value = 100 * (1 + row_index)
        
        if not value:
            for column_index in range(len(chart[0]) - 1):
                left = column_index
                right = column_index + 1
                is_mirror = True
                while True:
                    if left < 0 or right >= len(chart[0]):
                        break
                    if not all(map(lambda row_index: chart[row_index][left] == chart[row_index][right], range(len(chart)))):
                        is_mirror = False
                        break
                    else:
                        left -= 1
                        right += 1
                if is_mirror:
                    value = column_index + 1

        count += value
    print(count)

def part2(input_file):
    charts = []
    chart = []
    for row in input_file:
        row = row.strip()
        if not row:
            charts.append(chart)
            chart = []
        else:
            chart.append(row)
    if chart:
        charts.append(chart)

    count = 0
    for chart_index, chart in enumerate(charts):
        value = 0
        for row_index in range(len(chart) - 1):
            above = row_index
            below = row_index + 1
            error_count = 0
            while error_count <= 1:
                if above < 0 or below >= len(chart):
                    break
                for column_index in range(len(chart[row_index])):
                    if chart[above][column_index] != chart[below][column_index]:
                        error_count += 1
                else:
                    above -= 1
                    below += 1
            if error_count == 1:
                value = 100 * (1 + row_index)
        
        if not value:
            for column_index in range(len(chart[0]) - 1):
                left = column_index
                right = column_index + 1
                error_count = 0
                while True:
                    if left < 0 or right >= len(chart[0]):
                        break
                    for row_index in range(len(chart)):
                        if chart[row_index][left] != chart[row_index][right]:
                            error_count += 1
                    else:
                        left -= 1
                        right += 1
                if error_count == 1:
                    value = column_index + 1

        count += value
    print(count)


if __name__ == "__main__":
    with open("input.txt") as input_file:
        part2(input_file)