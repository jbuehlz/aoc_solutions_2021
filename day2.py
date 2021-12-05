def day2_part1():
    file = open('./input_files/day_2_input.txt')
    x, y = 0, 0
    for line in file:
        split = line.split(' ')
        operation = split[0]
        distance = int(split[1])
        if operation == 'forward':
            x = x + distance
        elif operation == 'down':
            y = y + distance
        elif operation == 'up':
            y = y - distance
    print('===== Day2 Pt1 =====')
    print(x * y)


def day2_part2():
    file = open('./input_files/day_2_input.txt')
    x, y, aim = 0, 0, 0
    for line in file:
        split = line.split(' ')
        operation = split[0]
        distance = int(split[1])
        if operation == 'forward':
            x = x + distance
            y += aim * distance
        elif operation == 'down':
            aim += distance
        elif operation == 'up':
            aim -= distance
    print('===== Day2 Pt2 =====')
    print(x * y)


if __name__ == "__main__":
    day2_part1()
    day2_part2()
