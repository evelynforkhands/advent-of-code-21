def read_input():
    f = open('inputs/input 9.txt', 'r')
    return [[int(char) for char in x] for x in f.read().split('\n')[:-1]]


def get_all_neighbours(row, col, point_class):
    if point_class == 'top_left':
        return [[row + 1, col], [row, col + 1]]
    elif point_class == 'top':
        return [[row + 1, col], [row, col - 1], [row, col + 1]]
    elif point_class == 'top_right':
        return [[row + 1, col], [row, col - 1]]
    elif point_class == 'left':
        return [[row - 1, col], [row + 1, col], [row, col + 1]]
    elif point_class == 'middle':
        return [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    elif point_class == 'right':
        return [[row - 1, col], [row + 1, col], [row, col - 1]]
    elif point_class == 'bottom_left':
        return [[row, col + 1], [row - 1, col]]
    elif point_class == 'bottom':
        return [[row, col - 1], [row, col + 1], [row - 1, col]]
    elif point_class == 'bottom_right':
        return [[row, col - 1], [row - 1, col]]


class BikiniBottom:

    def get_point(self, corrdinates):
        return self.map[corrdinates[0]][corrdinates[1]]

    def get_point_class(self, row, col):
        if row == 0:
            if col == 0:
                return 'top_left'
            elif col == len(self.map[row]) - 1:
                return 'top_right'
            else:
                return 'top'
        elif row == len(self.map) - 1:
            if col == 0:
                return 'bottom_left'
            elif col == len(self.map[row]) - 1:
                return 'bottom_right'
            else:
                return 'bottom'
        else:
            if col == 0:
                return 'left'
            elif col == len(self.map[row]) - 1:
                return 'right'
            else:
                return 'middle'

    def calculate_risk(self):
        risk = 0
        for point in self.lowest_points:
            risk += self.get_point(point) + 1
        return risk

    def find_lowest_points(self):  # lowest point are those whose adjacent neighbors are higher
        lowest_points = []
        for row in range(len(self.map)):
            for col in range(len(self.map[row])):
                if self.is_lowest_point(row, col):
                    lowest_points.append([row, col])
        return lowest_points

    def find_basins(self):
        basin_sizes = []
        for point in self.lowest_points:
            basin_sizes.append(self.find_basin(point))
        basin_sizes.sort(reverse=True)
        return basin_sizes[:3]

    def __init__(self):
        self.map = read_input()
        self.lowest_points = self.find_lowest_points()
        self.basins = self.find_basins()

    def is_lowest_point(self, row, col):
        point_class = self.get_point_class(row, col)
        neighbours = get_all_neighbours(row, col, point_class)
        for neighbour in neighbours:
            if self.get_point(neighbour) < self.map[row][col]:
                return False
            else:
                continue
        return True

    def find_basin(self, point):
        basin = [point]
        for p in basin:
            point_class = self.get_point_class(p[0], p[1])
            neighbours = get_all_neighbours(p[0], p[1], point_class)
            for neighbour in neighbours:
                if self.get_point(p) < self.get_point(neighbour) < 9 and neighbour not in basin:
                    basin.append(neighbour)
        return len(basin)


b = BikiniBottom()
x = 1
for i in b.basins:
    x *= i
print(x)
