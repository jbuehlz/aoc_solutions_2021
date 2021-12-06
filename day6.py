class School:
    def __init__(self, initial_school):
        self.fish = [0 for i in range(9)]
        for i in range(8):
            self.fish[i] = initial_school.count(i)

    def simulate_day(self):
        breeding_fish = self.fish[0]
        for i in range(8):
            self.fish[i] = self.fish[i + 1]
        self.fish[6] += breeding_fish
        self.fish[8] = breeding_fish

    def total_fish(self):
        return sum(self.fish)


def attempt(days=80):
    file = open('input_files/day_6.txt')
    split = file.readline().split(',')
    fish_list = [int(i) for i in split]
    school = School(fish_list)
    for i in range(days):
        school.simulate_day()
    print(school.total_fish())


if __name__ == "__main__":
    print('=== Day 6 Pt 1 ===')
    attempt()
    print('=== Day 6 Pt 2 ===')
    attempt(256)
