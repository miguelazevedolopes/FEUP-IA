import time


def get_empty(state):
    """
    Gets number of empty spaces
    """
    count=0
    for x in state.board:
        for y in x:
            if(y==2):
                count+=1
    return count


def manhattan_distance(state):
    """
    Gets the manhattan distance to the objective square
    """
    current = state.head
    objective = (len(state.board[0]) - 1, 0)
    return abs(current[0] - objective[0]) + abs(current[1] - objective[1])


def greedy_double_heuristic(state):
    """
    Combines both heuristics
    """
    return manhattan_distance(state) + get_empty(state)


def greedy_heuristic_manhattan(state):
    """
    Uses manhattan distance heuristic
    """
    return manhattan_distance(state)


def greedy_heuristic_empty_space(state):
    """
    Uses empty spaces heuristic
    """
    return get_empty(state)






