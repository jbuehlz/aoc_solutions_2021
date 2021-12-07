def attempt(part_two=False):
    file = open('input_files/day7.txt')
    strings = file.readline().split(',')
    numbers = [int(i) for i in strings]
    minimum_fuel = 0
    for i in range(max(numbers)):
        if part_two:
            fuel_required = sum(map(lambda x: lammy(x, i), numbers))
        else:
            fuel_required = sum(map(lambda x: abs(x - i), numbers))
        if not minimum_fuel:
            minimum_fuel = fuel_required
            continue
        if fuel_required < minimum_fuel:
            minimum_fuel = fuel_required
    print(round(minimum_fuel))


def lammy(pos, dest):
    d = abs(pos - dest)
    return d * (d+1)/2


if __name__ == "__main__":
    print("=== day 7 pt 1 ===")
    attempt()
    print("=== day 7 pt 2 ===")
    attempt(True)
