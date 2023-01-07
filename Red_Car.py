from Cell import Cell

class Red_Car:
    number = 0
    cell1 = Cell(0, 0)
    cell2 = Cell(0, 0)
    cell3 = Cell(0, 0)
    cost = 0

    def __init__(self, number, cell1, cell2, cell3, cost):
        self.number = number
        self.cell1 = cell1
        self.cell2 = cell2
        self.cell3 = cell3
        self.cost = cost

    def set_cell1(self, cell):
        self.cell1 = cell

    def set_cell2(self, cell):
        self.cell2 = cell

    def set_cell3(self, cell):
        self.cell3 = cell

    def get_number(self):
        return self.number

    def get_cell1(self):
        return self.cell1

    def get_cell2(self):
        return self.cell2

    def get_cell3(self):
        return self.cell3

    def get_cost(self):
        return self.cost