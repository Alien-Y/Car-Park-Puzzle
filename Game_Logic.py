import copy
from queue import Queue, PriorityQueue

class Game_Logic:

    visited_states = []
    queue_path = []      # to save the path
    entry_count = 0      # if two priorities are equal

    # this will return the path that the DFS has saved
    def get_queue_path(self):
        return self.queue_path

    # get the visited states while running the algorithm
    def get_visited_states(self):
        return self.visited_states

    # check if this board is equal to another
    def equals(self, board1, board2):
        if (board1 == board2):
            return True
        return False

    # BFS
    def bfs_solution(self, node):
        self.visited_states.append(node)
        self.queue_path.append("")
        queue_states = []
        queue_states.append(node)
        visited = 0  # iterator for visited states

        while queue_states :
            state_is_visited = False
            state = queue_states.pop(0)
            path = self.queue_path.pop(0)
            visited += 1

            if state.is_goal() :
                print("Path is : ", path)
                print("\nNumber of visited states : ", visited, "\n")
                state.display_board()
                return

            next_states, movements, costs = state.next_states()
            for iter_state, move in zip(next_states, movements) :
                for state_iter in self.visited_states :
                    if self.equals(state_iter.get_board(), iter_state.get_board()) :
                        state_is_visited = True
                if not state_is_visited :
                    self.visited_states.append(iter_state)
                    queue_states.append(iter_state)
                    new_path = list(path)
                    new_path.append(move)
                    self.queue_path.append(new_path)

    # DFS
    def dfs_solution(self, node):
        for state in self.visited_states:
            if self.equals(state.get_board(), node.get_board()) :
                return 0
        if node.is_goal():
            node.display_board()
            return 1
        self.visited_states.append(node)
        next_states, movements, costs = node.next_states()
        for iter_state, move in zip(next_states, movements) :
            if self.dfs_solution(iter_state) == 1 :
                self.queue_path.append(move)  # to save the path while turning back
                return 1

    # Uniform Cost Search
    def ucs_solution(self, node):
        ucs_queue = PriorityQueue()
        cost_list = []
        ucs_queue.put((0, self.entry_count, node, ""))  # (priority, entry_number, node, path)
        visited = 0  # iterator for visited states

        while True :
            state_is_visited = False
            cost, entry_count, current_node, path = ucs_queue.get()
            self.visited_states.append(current_node)
            cost_list.append(cost)
            visited += 1

            if current_node.is_goal():
                print("Path is : ", path)
                print("\nNumber of visited states : ", visited, "\n")
                current_node.display_board()
                return

            next_states, movements, costs = current_node.next_states()
            for iter_state, move, iter_cost in zip(next_states, movements, costs) :
                for state_iter, t_cost in zip(self.visited_states, cost_list) :
                     if self.equals(state_iter.get_board(), iter_state.get_board()) and t_cost < (iter_cost + cost):
                         state_is_visited = True
                if not state_is_visited :
                    self.entry_count += 1
                    new_path = list(path)
                    new_path.append(move)
                    ucs_queue.put((cost + iter_cost, self.entry_count, iter_state, new_path))

    # heuristic function for A* algorithm
    def heuristic(self, node):
        n, m = node.get_board_dimensions()
        distance = n - node.get_red_car().get_cell3().get_y()
        num_of_blank_cells = 0
        for i in range(node.get_red_car().get_cell3().get_y(), n):
            if (node.get_board()[node.get_red_car().get_cell3().get_x()][i] == '*'):
                num_of_blank_cells += 1
        estimate = (num_of_blank_cells)/(distance)
        return estimate

    # A_Star algorithm
    def A_Star_solution(self, node):
        A_Star_queue = PriorityQueue()
        cost_list = []
        A_Star_queue.put((0, self.entry_count, node, ""))  # (priority, entry_number, node, path)
        visited = 0  # iterator for visited states

        while True:
            state_is_visited = False
            cost, entry_count, current_node, path = A_Star_queue.get()
            cost = cost - self.heuristic(current_node)
            self.visited_states.append(current_node)
            cost_list.append(cost)
            visited += 1

            if current_node.is_goal():
                print("Path is : ", path)
                print("\nNumber of visited states : ", visited, "\n")
                current_node.display_board()
                return

            next_states, movements, costs = current_node.next_states()
            for iter_state, move, iter_cost in zip(next_states, movements, costs):
                for state_iter, t_cost in zip(self.visited_states, cost_list):
                    if self.equals(state_iter.get_board(), iter_state.get_board()) and t_cost < (iter_cost + cost):
                        state_is_visited = True
                if not state_is_visited:
                    self.entry_count += 1
                    new_path = list(path)
                    new_path.append(move)
                    A_Star_queue.put((cost + iter_cost - self.heuristic(state_iter), self.entry_count, iter_state, new_path))
