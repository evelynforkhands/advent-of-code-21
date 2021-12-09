class BikiniBottom:
    def calculate_risk(self):
        risk = 0
        for point in self.lowest_points:
            risk += point + 1
        return risk

    def find_lowest_points(self):  # lowest point are those whose adjacent neighbors are higher
        lowest_points = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.is_lowest_point(row, col):
                    lowest_points.append(self.map[row][col])
        return lowest_points

    def __init__(self):
        self.map = read_input()
        self.lowest_points = self.find_lowest_points()

    def is_lowest_point(self, row, col):
        if row == 0:
            if col == 0:
                return self.map[row][col] < self.map[row][col + 1] and self.map[row][col] < self.map[row + 1][col]
            elif col == len(self.map[row]) - 1:
                return self.map[row][col] < self.map[row][col - 1] and self.map[row][col] < self.map[row + 1][col]
            else:
                return self.map[row][col] < self.map[row][col - 1] and self.map[row][col] < self.map[row][col + 1] and \
                       self.map[row][col] < self.map[row + 1][col]
        elif row == len(self.map) - 1:
            if col == 0:
                return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row][col + 1]
            elif col == len(self.map[row]) - 1:
                return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row][col - 1]
            else:
                return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row][col - 1] and \
                       self.map[row][col] < self.map[row][col + 1]
        elif col == 0:
            return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row + 1][col] and \
                   self.map[row][col] < self.map[row][col + 1]
        elif col == len(self.map[row]) - 1:
            return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row + 1][col] and \
                   self.map[row][col] < self.map[row][col - 1]
        else:
            return self.map[row][col] < self.map[row - 1][col] and self.map[row][col] < self.map[row + 1][col] and \
                   self.map[row][col] < self.map[row][col - 1] and self.map[row][col] < self.map[row][col + 1]


def read_input():
    f = open('inputs/input 9.txt', 'r')
    return [[int(char) for char in x] for x in f.read().split('\n')[:-1]]


b = BikiniBottom()
print(b.calculate_risk())
