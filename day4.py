from functools import reduce


class Card:
    def __init__(self, values):
        self.winning_num = None
        self.values = values

    def check_number(self, val):
        for row in self.values:
            for i, _ in enumerate(row):
                if row[i] == val:
                    row[i] = 1000
        self.check_complete()

    def get_total_points(self):
        unmatched_numbers = 0
        for i in range(5):
            for j in range(5):
                if self.values[i][j] != 1000:
                    unmatched_numbers += self.values[i][j]
        return unmatched_numbers * self.winning_num

    def check_complete(self):
        for i in range(5):
            if reduce(lambda x, y: x + y, self.values[i]) == 5000:
                return True
            if self.values[0][i] + self.values[1][i] + self.values[2][i] + self.values[3][i] + self.values[4][i] == 5000:
                return True
        return False


def attempt():
    file = open('input_files/day_4.txt')
    winning_numbers = [int(i) for i in file.readline().split(',')]
    winning_cards = []
    bingo_cards = []
    while True:
        file.readline()
        values = [
            [int(i) for i in file.readline()[0:-1].split()],
            [int(i) for i in file.readline()[0:-1].split()],
            [int(i) for i in file.readline()[0:-1].split()],
            [int(i) for i in file.readline()[0:-1].split()],
            [int(i) for i in file.readline()[0:-1].split()]
        ]
        if not values[0]:
            break
        bingo_cards.append(Card(values))

    for num in winning_numbers:
        for card in bingo_cards:
            card.check_number(num)
        for _, card in enumerate(bingo_cards):
            won = card.check_complete()
            if won:
                bingo_cards.remove(card)
                winning_cards.append(card)
                card.winning_num = num
    print('=== Day 4 ===')
    print(f"Part 1: First Winning Card Score: {winning_cards[0].get_total_points()}")
    print(f"Part 2: Last Winning Card Score: {winning_cards[-1].get_total_points()}")


if __name__ == "__main__":
    attempt()