from enum import IntEnum
from functools import cmp_to_key

class HandStrength(IntEnum):
    FiveOfAKind = 6
    FourOfAKind = 5
    FullHouse = 4
    ThreeOfAKind = 3
    TwoPair = 2
    OnePair = 1
    HighCard = 0

cards = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
card_rank = {
    card : rank for rank, card in enumerate(reversed(cards))
}

print(card_rank)

def compare(hand1, hand2):
    str_1, str_2 = hand_strength(hand1), hand_strength(hand2)
    if str_1 > str_2:
        return 1
    elif str_1 == str_2:
        for index in range(len(hand1)):
            difference = card_rank[hand1[index]] - card_rank[hand2[index]]
            if difference > 0:
                return 1
            elif difference < 0:
                return -1
        return 0
    elif str_2 > str_1:
        return -1

def inner_hand_strength(hand):
    counts = {x : hand.count(x) for x in hand}
    counts_values = counts.values()
    max_counts = max(counts_values)

    if max_counts == 5:
        return HandStrength.FiveOfAKind
    elif max_counts == 4:
        return HandStrength.FourOfAKind
    elif max_counts == 3:
        if len(counts) == 2:
            return HandStrength.FullHouse
        else:
            return HandStrength.ThreeOfAKind
    elif len(counts) == 3:
       return HandStrength.TwoPair
    elif len(counts) == 4:
       return HandStrength.OnePair
    else:
        return HandStrength.HighCard

def hand_strength(hand):
    if "J" in hand:
        # This can be done more efficiently by unrolling the possibilities in inner_hand_strength
        # but it's somewhat error prone to do by hand. And for the purposes of this question
        # it's quite cheap to be naiive here and just find the best substitution by brute
        # force ignoring the fact that at most 4 substitions will make sense for any given hand
        return max(map(inner_hand_strength, [hand.replace("J", card) for card in cards]))
    else:
        return inner_hand_strength(hand)

def part2(input_text):
    inputs = []
    for line in input_text:
        inputs.append(line.split(" "))

    inputs.sort(key = cmp_to_key(lambda x, y: compare(x[0], y[0])))
    total_winnings = 0
    for rank, (hand, bid) in enumerate(inputs):
        bid = int(bid)
        total_winnings += bid * (rank + 1)
        print(rank + 1, hand, bid)
    print(total_winnings)

if __name__ == "__main__":
    example = (
        "32T3K 765",
        "T55J5 684",
        "KK677 28",
        "KTJJT 220",
        "QQQJA 483",
    )
    #part2(example)
    with open("input") as input_file:
        part2(input_file)
