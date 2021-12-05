def day4_pt1():
    file = open('input_files/day_4.txt')
    winning_numbers = file.readline().split(',')
    winning_cards = []
    bingo_cards = []
    not_done = True
    while not_done:
        file.readline()
        card = [
            file.readline()[0:-1].split(),
            file.readline()[0:-1].split(),
            file.readline()[0:-1].split(),
            file.readline()[0:-1].split(),
            file.readline()[0:-1].split()
            ]
        if not card[0]:
            break
        bingo_cards.append(card)

    for num in winning_numbers:
        for card in bingo_cards:
            for row in card:
                for idx, val in enumerate(row):
                    if num == val:
                        row[idx] = 1000
        for idx, card in enumerate(bingo_cards):
            done = False
            for row in card:
                if row == [1000, 1000, 1000, 1000, 1000]:
                    winning_cards.append(num)
                    winning_cards.append(card)
                    bingo_cards.remove(card)
                    done = True
                    break
            if not done:
                for i in range(5):
                    if card[0][i] == 1000 and card[1][i] == 1000 and card[2][i] == 1000 and card[3][i] == 1000 and card[4][i] == 1000:
                        winning_cards.append(num)
                        winning_cards.append(card)
                        bingo_cards.remove(card)
                        break
    for win in winning_cards:
        print(win)
    print('==== day 4 pt 1 =====')


if __name__ == "__main__":
    day4_pt1()