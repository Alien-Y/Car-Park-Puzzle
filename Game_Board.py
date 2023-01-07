import copy
from Cell import Cell
from Red_Car import Red_Car
from Green_Car import Green_Car

class Game_Board:
    n, m = 0, 0     # n and m are board dimensions where n refers to columns number and m refers to rows number
    board = [['*' for x in range(n)] for y in range(m)]
    green_cars = []
    red_car = Red_Car(0, Cell(0, 0), Cell(0, 0), Cell(0, 0), 0)

    def __init__(self, n, m, green_cars_list, red_car):
        self.n = n
        self.m = m
        self.green_cars = green_cars_list
        self.red_car = red_car
        self.board = [['*' for x in range(n)] for y in range(m)]

        # setting cars in the board

        # setting the red car
        self.board[self.red_car.get_cell1().get_x()][self.red_car.get_cell1().get_y()] = self.red_car.get_number()
        self.board[self.red_car.get_cell2().get_x()][self.red_car.get_cell2().get_y()] = self.red_car.get_number()
        self.board[self.red_car.get_cell3().get_x()][self.red_car.get_cell3().get_y()] = self.red_car.get_number()

        # setting the green cars
        for car in self.green_cars:
            self.board[car.get_cell1().get_x()][car.get_cell1().get_y()] = car.get_number()
            self.board[car.get_cell2().get_x()][car.get_cell2().get_y()] = car.get_number()

    # display the area
    def display_board(self):
        for cell in self.board:
            for value in cell:
                if value == '*' :
                    print(value, end="   ")
                else :
                    if int(value) <= 9 :
                        print(value,end="   ")
                    if int(value) > 9 :
                        print(value, end="  ")
            print()

    # get board dimensions
    def get_board_dimensions(self):
        return self.n, self.m

    # get red car object
    def get_red_car(self):
        return self.red_car

    # get the 2D board array
    def get_board(self):
        return self.board

    # movement checking in the 4 directions
    def can_move_left(self, target_car):
        if(target_car.get_cell1().get_y()  - target_car.get_cell2().get_y() == 0): #check if the car is vertical
            return False
        if((target_car.get_cell1().get_y() - 1) < 0):
            return False
        if(self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y() - 1] == '*'):
            return True
        else:
            return False

    def can_move_right(self, target_car):
        if (target_car.get_cell1().get_y() - target_car.get_cell2().get_y() == 0): #check if the car is vertical
            return False
        if(target_car == self.red_car):
            if ((target_car.get_cell3().get_y() + 1) >= self.n):
                return False
            if (self.board[target_car.get_cell3().get_x()][target_car.get_cell3().get_y() + 1] == '*'):
                return True
        else:
            if ((target_car.get_cell2().get_y() + 1) >= self.n):
                return False
            if (self.board[target_car.get_cell2().get_x()][target_car.get_cell2().get_y() + 1] == '*'):
                return True
        return False

    def can_move_up(self, target_car):
        if (target_car == self.red_car): # red car can't move up
            return  False
        if ((target_car.get_cell1().get_x() - 1) < 0):
            return False
        if (target_car.get_cell1().get_x()  - target_car.get_cell2().get_x() == 0): # check if the car is horizontal
            return False
        if (self.board[target_car.get_cell1().get_x() - 1][target_car.get_cell1().get_y()] == '*'):
            return True
        else:
            return False

    def can_move_down(self, target_car):
        if (target_car == self.red_car): # red car can't move down
            return  False
        if ((target_car.get_cell2().get_x() + 1) >= self.m):
            return False
        if (target_car.get_cell1().get_x()  - target_car.get_cell2().get_x() == 0): # check if the car is horizontal
            return False
        if (self.board[target_car.get_cell2().get_x() + 1][target_car.get_cell1().get_y()] == '*'):
            return True
        else:
            return False

    # movement method
    def move(self, car_number, direction):
        target_car = None
        if int(self.red_car.get_number()) == int(car_number) :
            target_car = self.red_car
        else :
            for car in self.green_cars :
                if int(car.get_number()) == int(car_number) :
                    target_car = car
                    break
        if direction == 'left':
            if(self.can_move_left(target_car)):
                if (target_car == self.red_car):
                    self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y() - 1] = car_number
                    self.board[target_car.get_cell3().get_x()][target_car.get_cell3().get_y()] = '*'
                    target_car.set_cell3(target_car.get_cell2())
                    target_car.set_cell2(target_car.get_cell1())
                    target_car.set_cell1(Cell(target_car.get_cell1().get_x(), target_car.get_cell1().get_y() - 1))
                    return
                else :
                    self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y() - 1] = car_number
                    self.board[target_car.get_cell2().get_x()][target_car.get_cell2().get_y()] = '*'
                    target_car.set_cell2(target_car.get_cell1())
                    target_car.set_cell1(Cell(target_car.get_cell1().get_x(), target_car.get_cell1().get_y() - 1))
                    return
            else :
                print("Can't move !")
                print()
                return

        if direction == 'right':
            if(self.can_move_right(target_car)):
                if (target_car == self.red_car):
                    self.board[target_car.get_cell3().get_x()][target_car.get_cell3().get_y() + 1] = car_number
                    self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y()] = '*'
                    target_car.set_cell1(target_car.get_cell2())
                    target_car.set_cell2(target_car.get_cell3())
                    target_car.set_cell3(Cell(target_car.get_cell3().get_x(), target_car.get_cell3().get_y() + 1))
                    return
                else :
                    self.board[target_car.get_cell2().get_x()][target_car.get_cell2().get_y() + 1] = car_number
                    self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y()] = '*'
                    target_car.set_cell1(target_car.get_cell2())
                    target_car.set_cell2(Cell(target_car.get_cell2().get_x(), target_car.get_cell2().get_y() + 1))
                    return
            else:
                print("Can't move !")
                print()
                return

        if direction == 'up':
            if(self.can_move_up(target_car)):
                self.board[target_car.get_cell1().get_x() - 1][target_car.get_cell1().get_y()] = car_number
                self.board[target_car.get_cell2().get_x()][target_car.get_cell2().get_y()] = '*'
                target_car.set_cell2(target_car.get_cell1())
                target_car.set_cell1(Cell(target_car.get_cell1().get_x() - 1, target_car.get_cell1().get_y()))
                return
            else:
                print("Can't move !")
                print()
                return

        if direction == 'down':
            if(self.can_move_down(target_car)):
                self.board[target_car.get_cell2().get_x() + 1][target_car.get_cell2().get_y()] = car_number
                self.board[target_car.get_cell1().get_x()][target_car.get_cell1().get_y()] = '*'
                target_car.set_cell1(target_car.get_cell2())
                target_car.set_cell2(Cell(target_car.get_cell2().get_x() + 1, target_car.get_cell2().get_y()))
                return
            else:
                print("Can't move !")
                print()
                return

    # the possible next states from the current state
    def next_states(self):

        states_list = [] # to store all the possible moves
        hints = []       # to store car movements
        cost = []

        # red car possible moves
        if (self.can_move_right(self.red_car)):
            temp = copy.deepcopy(self)
            temp.move(self.red_car.get_number(), 'right')
            states_list.append(temp)
            hints.append(str(temp.red_car.get_number()) + " to right")
            cost.append(self.red_car.get_cost())

        if (self.can_move_left(self.red_car)):
            temp = copy.deepcopy(self)
            temp.move(self.red_car.get_number(), 'left')
            states_list.append(temp)
            hints.append(str(temp.red_car.get_number()) + " to left")
            cost.append(self.red_car.get_cost())

        # iterate on the green cars
        for car in self.green_cars:
            if(self.can_move_up(car)):
                temp = copy.deepcopy(self)
                temp.move(car.get_number(), 'up')
                states_list.append(temp)
                hints.append(str(car.get_number()) + " to up")
                cost.append(car.get_cost())

            if (self.can_move_down(car)):
                temp = copy.deepcopy(self)
                temp.move(car.get_number(), 'down')
                states_list.append(temp)
                hints.append(str(car.get_number()) + " to down")
                cost.append(car.get_cost())

            if (self.can_move_left(car)):
                temp = copy.deepcopy(self)
                temp.move(car.get_number(), 'left')
                states_list.append(temp)
                hints.append(str(car.get_number()) + " to left")
                cost.append(car.get_cost())

            if (self.can_move_right(car)):
                temp = copy.deepcopy(self)
                temp.move(car.get_number(), 'right')
                states_list.append(temp)
                hints.append(str(car.get_number()) + " to right")
                cost.append(car.get_cost())

        return states_list, hints, cost

    # checking if this is a final state
    def is_goal(self):
        exit = int(self.m/2) # exit row
        try:
            if(int(self.board[exit][self.n-1]) == self.red_car.get_number()):
                return True
        except:
            return False
        return False




