from Cell import Cell
from Red_Car import Red_Car
from Green_Car import Green_Car
from Game_Board import Game_Board
from Game_Logic import Game_Logic

green_cars_list = []

green_cars_list.append(Green_Car(1, Cell(0, 0), Cell(1, 0), 1))
green_cars_list.append(Green_Car(2, Cell(3, 0), Cell(4, 0), 1))
green_cars_list.append(Green_Car(3, Cell(2, 3), Cell(3, 3), 1))
green_cars_list.append(Green_Car(4, Cell(4, 2), Cell(4, 3), 1))
green_cars_list.append(Green_Car(5, Cell(2, 5), Cell(3, 5), 1))
green_cars_list.append(Green_Car(6, Cell(3, 6), Cell(4, 6), 1))
green_cars_list.append(Green_Car(7, Cell(1, 6), Cell(2, 6), 1))
green_cars_list.append(Green_Car(8, Cell(0, 1), Cell(0, 2), 1))
green_cars_list.append(Green_Car(9, Cell(0, 5), Cell(0, 6), 1))
green_cars_list.append(Green_Car(10, Cell(1, 2), Cell(1, 3), 1))
green_cars_list.append(Green_Car(11, Cell(3, 1), Cell(3, 2), 1))
green_cars_list.append(Green_Car(12, Cell(4, 4), Cell(4, 5), 1))

red_car = Red_Car(0, Cell(2, 0), Cell(2, 1), Cell(2, 2), 1)

game = Game_Board(7, 5, green_cars_list, red_car)
print("\nInitial State :\n")
game.display_board()
print('\n*************************\n')

########################################

#bfs solution

# print("BFS solution :\n")
# game_logic1 = Game_Logic()
# game_logic1.bfs_solution(game)

########################################

# dfs solution

# print("DFS solution :\n")
# game_logic2 = Game_Logic()
# game_logic2.dfs_solution(game)
# path = game_logic2.get_queue_path()
# print("\nNumber of visited states : ", len(game_logic2.get_visited_states()))
# print("\nPath is : ", path[::-1])

#########################################

# UCS solution

# print("UCS solution :\n")
# game_logic3 = Game_Logic()
# game_logic3.ucs_solution(game)

##########################################

# A_Star solution

print("A_Star solution :\n")
game_logic4 = Game_Logic()
game_logic4.A_Star_solution(game)

##########################################

# show the possible movements in every choosen state

# choosen_state = game
# while not choosen_state.is_goal():
#     next_states, movements = choosen_state.next_states()
#     state_no = 0
#     print('\n*************************\n')
#     print("   POSSIBLE MOVEMENTS :")
#     for state, move in zip(next_states, movements) :
#         print('\n*************************')
#         print('        STATE :', state_no, '\n')
#         state_no += 1
#         state.display_board()
#         print("\n      ", move)
#     choosen_state, movements = next_states[int(input("\nChoose a state : "))]

#########################################

# get the input from user

# while(not game.is_goal()):
#     target_car_number = input()
#     direction = input()
#     game.move(target_car_number, direction)
#     game.display_board()


