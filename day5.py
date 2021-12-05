class Map:
    def __init__(self, height=1001, width=1001):
        self.board = [[0] * height for _ in range(width)]

    def process_vent_line(self, line, part_two=False):
        split = line.split(' -> ')
        start = split[0]
        end = split[1]
        start_split = start.split(',')
        xs, ys, = int(start_split[0]), int(start_split[1])
        end_split = end.split(',')
        xe, ye, = int(end_split[0]), int(end_split[1])
        if xs == xe or ys == ye:
            self.populate_line_straight(xs, ys, xe, ye)
        elif part_two:
            self.populate_line_diag(xs, ys, xe, ye)

    def populate_line_straight(self, xs, ys, xe, ye):
        if xs > xe:
            hold = xs
            xs = xe
            xe = hold
        if ys > ye:
            hold = ys
            ys = ye
            ye = hold
        if xs == xe:
            for y in range(ys, ye + 1):
                self.board[xs][y] += 1
        elif ys == ye:
            for x in range(xs, xe + 1):
                self.board[x][ys] += 1

    def populate_line_diag(self, xs, ys, xe, ye):
        curr_x, curr_y = xs, ys
        while True:
            self.board[curr_x][curr_y] += 1
            if curr_x < xe:
                curr_x += 1
            else:
                curr_x -= 1
            if curr_y < ye:
                curr_y += 1
            else:
                curr_y -= 1
            if curr_x == xe and curr_y == ye:
                self.board[curr_x][curr_y] += 1
                break

    def count_spots(self):
        num_spots = 0
        for row in self.board:
            for cell in row:
                if cell >= 2:
                    num_spots += 1
        return num_spots


def part_one(part_two=False):
    sea_floor_map = Map()
    file = open('input_files/day_5.txt')
    for x in file:
        sea_floor_map.process_vent_line(x, part_two=part_two)
    print(f'# of vent spots: {sea_floor_map.count_spots()}')


if __name__ == '__main__':
    print('=== day 5 part 1 ===')
    part_one(False)
    print('=== day 5 part 2 ===')
    part_one(True)
