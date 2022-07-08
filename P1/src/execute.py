from state import *
from utils import *
from input import *
from display import *
import timeit

def performance_analysis(state, algorithm):
    """
    Runs the algorithm and prints the time it took to finish
    """
    with Loader("Running the algorithm..."):
        start = timeit.default_timer()
        final = algorithm(state)
        end = timeit.default_timer()
    print("Runtime: "+ str(end-start) + " seconds")
    return final


def execute_option(option, state): 
    """
    Deals with menu option chosen
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    if option == 1:
        game_loop(state)
    elif option == 2:
        display_algorithm_menu()
        alg_option = get_algorithm_option()
        os.system('cls' if os.name == 'nt' else 'clear')
        execute_algorithm_option(alg_option, state)
    return


def execute_algorithm_option(option, state):
    """
    Deals with algorithm option chosen
    """
    if option == 1:
        final = performance_analysis(state, bfs)
    elif option == 2:
        final = performance_analysis(state, dfs)
    elif option == 3:
        display_greedy_menu()
        g_option = get_greedy_option()
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(state)
        if g_option == 1:
            final = performance_analysis(state, greedy_manhattan)
        elif g_option == 2:
            final = performance_analysis(state, greedy_empty_space)
        elif g_option == 3:
            final = performance_analysis(state, greedy_double_h)
    i=input("Reconstruct path? (Y/N): ")
    if(i=='Y' or i=='y'):
        while(True):
            path=reconstruct_path(final)
            display_path(path)
            i=input("Replay? (Y/N): ")
            if(i=='N' or i=='n'):
                break


def game_loop(state):
    """
    Game loop for the user
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    display_board(state)
    while (not is_goal(state)):
        if has_no_moves(state):
            print("There are no moves left for you to make!")
            break
        state = execute_move(state)
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(state)
        

    print("Game over!")