def day3_pt1():
    file = open('input_files/input_day3.txt')
    gamma, epsilon, line_count, bins = '', '', 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for x in file:
        if x != '\n':
            line_count += 1
        for i in range(0, 12):
            if x[i] == '1':
                bins[i] += 1
    for i in bins:
        if i > 500:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print('===== Day3 Pt1 =====')
    print(int(gamma, 2) * int(epsilon, 2))


def day3_pt2():
    file = open('input_files/input_day3.txt')
    oxygen_list, co2_list = [], []
    for x in file:
        oxygen_list.append(x[0:-1])
        co2_list.append(x[0:-1])

    oxygen_rating_bin = sort_oxygen(0, oxygen_list)
    co2_rating_bin = sort_c02(0, co2_list)

    print('===== Day3 Pt2 =====')
    print(int(oxygen_rating_bin, 2) * int(co2_rating_bin, 2))


def sort_oxygen(position, curr_list):
    if len(curr_list) == 1:
        return curr_list[0]
    true, false, new_list = 0, 0, []
    for num in curr_list:
        if num[position] == '1':
            true += 1
        else:
            false += 1
    for num in curr_list:
        if true >= false and num[position] == '1':
            new_list.append(num)
        elif false > true and num[position] == '0':
            new_list.append(num)
    if len(new_list) == 1:
        return new_list[0]
    return sort_oxygen(position + 1, new_list)


def sort_c02(position, curr_list):
    if len(curr_list) == 1:
        return curr_list[0]
    true, false, new_list = 0, 0, []
    for num in curr_list:
        if num[position] == '1':
            true += 1
        else:
            false += 1
    for num in curr_list:
        if true < false and num[position] == '1':
            new_list.append(num)
        elif false <= true and num[position] == '0':
            new_list.append(num)
    if len(new_list) == 1:
        return new_list[0]
    return sort_c02(position + 1, new_list)


if __name__ == "__main__":
    day3_pt1()
    day3_pt2()
