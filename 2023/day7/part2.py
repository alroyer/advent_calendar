from enum import Enum

CARD_VALUE = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'T': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
    'J': 1,
}


class HandType(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        if 1 in cards:
            if (5 * [1]) == cards:
                self.hand_type = HandType.FIVE_OF_A_KIND.value
            else:
                other_cards = set(cards)
                other_cards.discard(1)

                card_types = []
                for card in other_cards:
                    new_cards = [card if c == 1 else c for c in cards]
                    card_types.append(hand_type(new_cards))
                self.hand_type = max(card_types)
        else:
            self.hand_type = hand_type(self.cards)

    def __lt__(self, other) -> bool:
        return self.hand_type < other.hand_type or (self.hand_type == other.hand_type and self.cards < other.cards)

    def __repr__(self) -> str:
        return f'{self.cards=}-{self.hand_type=}'


def hand_type(cards: list[int]) -> int:
    count = {}
    for card in cards:
        if not card in count:
            count[card] = cards.count(card)

    highest = max(count.values())

    if highest == 5:
        return HandType.FIVE_OF_A_KIND.value
    elif highest == 4:
        return HandType.FOUR_OF_A_KIND.value
    elif len(count) == 2:
        return HandType.FULL_HOUSE.value
    elif highest == 3:
        return HandType.THREE_OF_A_KIND.value
    elif len(count) == 3:
        return HandType.TWO_PAIR.value
    elif highest == 2:
        return HandType.ONE_PAIR.value
    return HandType.HIGH_CARD.value


def read_data(path: str) -> list[Hand]:
    with open(path, 'r') as f:
        data = f.readlines()
        hands = []
        for d in data:
            hand, bid = d.strip().split(' ')
            hands.append(Hand([CARD_VALUE[c] for c in hand], int(bid)))
        return hands


def main():
    hands = read_data('input1.txt')
    hands.sort()

    sum = 0
    for rank, hand in enumerate(hands):
        sum = sum + (rank + 1) * hand.bid
    print(sum)


if __name__ == '__main__':
    main()
