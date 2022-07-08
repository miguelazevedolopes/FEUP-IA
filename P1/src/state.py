from queue import PriorityQueue
from tree import *
from display import *
from utils import *


class State(Node):
    """
    Class that determines the state of the game at every move.
    Has the board matrix, the position of the head and the info of what it has done.
    """

    def __init__(self, board: list, head: tuple, previous_move: str, previous_move_count=0, move_count=0,heuristic_function=None, parent=None):
        self.board = board
        self.head = head
        self.previous_move = previous_move
        self.previous_move_count = previous_move_count
        self.move_count = move_count
        if(heuristic_function!=None):
            self.heuristics = heuristic_function(self)
        else:
            self.heuristics=1
        super().__init__(parent)

    def __str__(self):
        state = "Head: " + str(self.head) + " - " + self.info + "\n"
        for row in self.board:
            state += str(row) + "\n"
        return state

    def __eq__(self, o) -> bool:
        for y in range(len(self.board)):
            for x in range(len(self.board[0])):
                if (self.board[y][x] != o.board[y][x]):
                    return False
        if(self.previous_move != o.previous_move or self.move_count != o.move_count or self.previous_move_count != o.previous_move_count):
            return False
        if(self.heuristics != o.heuristics):
            return False
        return True

    def __lt__(self, o) -> bool:
        return self.heuristics < o.heuristics


def clone_board(board):
    """
    Creates a copy of the board
    """
    cloned = []
    for row in board:
        new_row = []
        for col in row:
            new_row.append(col)
        cloned.append(new_row)
    return cloned


def can_move_up(state: State):
    """
    Verifies if it is possible to move up according to the rules and board disposition
    """
    x, y = state.head
    return 0 < y <= (len(state.board) - 1) and state.board[y-1][x] == 2 and ((state.previous_move != "Up" and state.move_count != state.previous_move_count) or (state.previous_move == "Up"))


def move_up(state: State,heuristic=None):
    """
    Executes the move up and returns the new state
    """
    x, y = state.head
    clone = clone_board(state.board)
    clone[y][x] = 3
    clone[y-1][x] = 0
    if(state.previous_move == "Up"):
        return State(clone, (x, y - 1), "Up", state.previous_move_count, state.move_count+1,heuristic, state)
    else:
        return State(clone, (x, y - 1), "Up", state.move_count, 2,heuristic, state)


def can_move_down(state: State):
    """
    Verifies if it is possible to move down according to the rules and board disposition
    """
    x, y = state.head
    return 0 <= y < (len(state.board) - 1) and state.board[y+1][x] == 2 and ((state.previous_move != "Down" and state.move_count != state.previous_move_count) or (state.previous_move == "Down"))


def move_down(state: State,heuristic=None):
    """
    Executes the move down and returns the new state
    """
    x, y = state.head
    clone = clone_board(state.board)
    clone[y][x] = 3
    clone[y+1][x] = 0
    if(state.previous_move == "Down"):
        return State(clone, (x, y + 1), "Down", state.previous_move_count, state.move_count+1,heuristic, state)
    else:
        return State(clone, (x, y + 1), "Down", state.move_count, 2,heuristic, state)


def can_move_left(state: State):
    """
    Verifies if it is possible to move left according to the rules and board disposition
    """
    x, y = state.head
    return 0 < x <= (len(state.board[0]) - 1) and state.board[y][x-1] == 2 and ((state.previous_move != "Left" and state.move_count != state.previous_move_count) or (state.previous_move == "Left"))


def move_left(state: State,heuristic=None):
    """
    Executes the move left and returns the new state
    """
    x, y = state.head
    clone = clone_board(state.board)
    clone[y][x] = 3
    clone[y][x - 1] = 0
    if(state.previous_move == "Left"):
        return State(clone, (x - 1, y), "Left", state.previous_move_count, state.move_count+1,heuristic, state)
    else:
        return State(clone, (x-1, y), "Left", state.move_count, 2,heuristic, state)


def can_move_right(state: State):
    """
    Verifies if it is possible to move right according to the rules and board disposition
    """
    x, y = state.head
    return 0 <= x < (len(state.board[0]) - 1) and state.board[y][x+1] == 2 and ((state.previous_move != "Right" and state.move_count != state.previous_move_count) or (state.previous_move == "Right"))


def move_right(state: State,heuristic=None):
    """
    Executes the move right and returns the new state
    """
    x, y = state.head
    clone = clone_board(state.board)
    clone[y][x] = 3
    clone[y][x + 1] = 0
    if(state.previous_move == "Right"):
        return State(clone, (x + 1, y), "Right", state.previous_move_count, state.move_count+1,heuristic, state)
    else:
        return State(clone, (x+1, y), "Right", state.move_count, 2,heuristic, state)


def expand(state: State,heuristic=None):
    """
    Appends possible moves to the current tree of states
    """
    descendants = []
    if(state.board[0][len(state.board[0])-1] == 3 and is_full(state) == False):
        return []
    # can move right
    if can_move_right(state):
        descendants.append(move_right(state,heuristic))

    # can move left
    if can_move_left(state):
        descendants.append(move_left(state,heuristic))

    # can move up
    if can_move_up(state):
        descendants.append(move_up(state,heuristic))

    # can move down
    if can_move_down(state):
        descendants.append(move_down(state,heuristic))

    return descendants


def is_goal(state: State):
    """
    Checks if the current state is the goal state
    """
    if(state.head != (len(state.board[0])-1, 0)):
        return False
    for y in range(len(state.board)):
        for x in range(len(state.board[0])):
            if (state.board[y][x] == 2):
                return False
    return True


def is_full(state: State):
    """
    Checks if the full board has been visited
    """
    for y in range(len(state.board)):
        for x in range(len(state.board[0])):
            if (state.board[y][x] == 2):
                return False
    return True


def has_no_moves(state: State):
    """
    Checks if there are no possible moves
    """
    return not (can_move_down(state) or can_move_left(state) or can_move_right(state) or can_move_up(state))


def reconstruct_path(final_state):
    """
    Reconstructs the path leading to the final state
    """
    path=[final_state]
    state=final_state
    while(True):
        if(state is None):
            break
        path.append(state.parent)
        state=state.parent
    path.pop()
    return path


def dfs(node):
    """
    Performs depth-first-search to find the solution
    """
    s = [node]
    visited = []
    while(len(s) != 0):
        n = s.pop()
        if(is_goal(n) == True):
            return n
        if(n not in visited):
            visited.append(n)
            adjacentNodes = expand(n)
            for e in adjacentNodes:
                s.append(e)
    return node


def bfs(node):
    """
    Performs breadth-first-search to find the solution
    """
    q = []
    visited = [node]
    q.append(node)
    while(len(q) != 0):
        n = q.pop(0)
        if(is_goal(n) == True):
            return n
        adjacentNodes = expand(n)
        for e in adjacentNodes:
            if(e not in visited):
                visited.append(e)
                q.append(e)
    return node


def greedy_double_h(node):
    """
    Performs greedy search using empty spaces and manhattan distance heuristics
    """
    q = PriorityQueue()
    visited = []
    q.put(node)
    while(q.empty() == False):
        n = q.get()
        if(is_goal(n) == True):
            return n
        visited.append(n)
        adjacentNodes = expand(n,greedy_double_heuristic)
        for e in adjacentNodes:
            if(e not in visited):
                q.put(e)
    return node


def greedy_manhattan(node):
    """
    Performs greedy search using manhattan distance heuristic
    """
    q = PriorityQueue()
    visited = []
    q.put(node)
    while(q.empty() == False):
        n = q.get()
        if(is_goal(n) == True):
            return n
        visited.append(n)
        adjacentNodes = expand(n,greedy_heuristic_manhattan)
        for e in adjacentNodes:
            if(e not in visited):
                q.put(e)
    return node


def greedy_empty_space(node):
    """
    Performs greedy search using empty spaces heuristic
    """
    q = PriorityQueue()
    visited = []
    q.put(node)
    while(q.empty() == False):
        n = q.get()
        if(is_goal(n) == True):
            return n
        visited.append(n)
        adjacentNodes = expand(n,greedy_heuristic_empty_space)
        for e in adjacentNodes:
            if(e not in visited):
                q.put(e)
    return node

