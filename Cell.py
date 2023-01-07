class Cell:
    x = 0  # x is row
    y = 0  # y is column

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_cell(self):
        print(self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y