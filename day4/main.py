example = (
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
)

def part_1(input_data):
    total_score = 0
    for row in input_data:
        card_title, card_data = row.split(":")
        winners, have = card_data.split("|")
        card_number = int(card_title.split(" ")[-1].strip())
        winners = set([int(x) for x in winners.strip().split(" ") if x.strip()])
        have = set([int(x) for x in have.strip().split(" ") if x.strip()])

        count_winners_have = len(winners & have)
        score = 0
        if count_winners_have == 0:
            score = 0
        else:
            score = 2**(count_winners_have - 1)

        print(f"Card {card_number}: {score}")
        total_score += score

    print(total_score)

def part_2(input_data):
    card_winners = []
    for row in input_data:
        card_title, card_data = row.split(":")
        winners, have = card_data.split("|")
        card_number = int(card_title.split(" ")[-1].strip())
        winners = set([int(x) for x in winners.strip().split(" ") if x.strip()])
        have = set([int(x) for x in have.strip().split(" ") if x.strip()])
        card_winners.append(len(winners & have))

    card_counts = [1 for x in range(len(card_winners))]
    for card_number, number_winners in enumerate(card_winners):
        for i in range(card_counts[card_number]):
            for j in range(number_winners):
                try:
                    card_counts[card_number + j + 1] += 1
                except IndexError:
                    pass

    print(sum(card_counts))

if __name__ == "__main__":
    #part_2(example)
    with open("input") as input_file:
        part_2(input_file)
