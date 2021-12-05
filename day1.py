def day1_part1():
    file = open('./input_files/day_1_input.txt')
    curr_num, prev_num = None, None
    greater_thans = 0
    for l in file:
        curr_num = int(l)
        if not prev_num:
            prev_num = curr_num
            continue
        if curr_num > prev_num:
            greater_thans += 1
        prev_num = curr_num
    print('===== Day1 Pt1 =====')
    print(greater_thans)

def day1_part2():
    file = open('./input_files/day_1_input.txt')
    numbers = []
    for x in file:
        numbers.append(int(x))
    greater_thans = 0
    current_sum, previous_sum = None, None
    try:
        for idx, num in enumerate(numbers):
            if not numbers[idx + 2]:
                break
            current_sum = numbers[idx] + numbers[idx + 1] + numbers[idx + 2]
            if not previous_sum:
                previous_sum = current_sum
                continue
            if current_sum > previous_sum:
                greater_thans += 1
            previous_sum = current_sum
    except IndexError as e:
        pass
    finally:
        print('===== Day1 Pt2 =====')
        print(greater_thans)

if __name__ == "__main__":
    day1_part1()
    day1_part2()