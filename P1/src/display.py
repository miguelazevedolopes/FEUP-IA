import colorama
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
import os


def display_board(state):
    """
    Displays the current state of the maze
    """
    colorama.init()
    color = colorama.Back.BLACK
    for y in range(len(state.board)):
        print(colorama.Style.RESET_ALL+"")
        for x in range(len(state.board[0])):
            print(colorama.Style.RESET_ALL + "|", end="")
            if state.board[y][x] == 0:
                color = colorama.Back.LIGHTBLUE_EX
                print(color + "_x_", end="")
            elif state.board[y][x] == 1:
                color = colorama.Back.LIGHTRED_EX
                print(color + "___", end="")
            elif state.board[y][x] == 2:
                color = colorama.Back.LIGHTBLACK_EX
                print(color + "___", end="")
            elif state.board[y][x] == 3:
                color = colorama.Back.LIGHTGREEN_EX
                print(color + "___", end="")
        print(colorama.Style.RESET_ALL + "|", end="")
    print(colorama.Style.RESET_ALL+"")
    print()
    colorama.deinit()


def display_path(path):
    """
    Displays the path to the solution
    """
    while(len(path)!=0):
        sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(path.pop())


def display_menu():
    """
    Displays initial menu
    """
    print("\n\n  ________________________________ ")
    for _ in range(3):
        print(" |                                |")
    print(" |      Unequal Length Mazes      |")
    print(" |             1.Play             |")
    print(" |          2.Algorithm           |")
    for _ in range(2):
        print(" |                                |")
    print(" |________________________________|\n")


def display_algorithm_menu():
    """
    Display algorithm menu
    """
    print("  ________________________________ ")
    for _ in range(3):
        print(" |                                |")
    print(" |             1.BFS              |")
    print(" |             2.DFS              |")
    print(" |           3.Greedy             |")
    for _ in range(2):
        print(" |                                |")
    print(" |________________________________|\n")


def display_greedy_menu():
    """
    Display greedy algorithm options
    """
    print("  ________________________________ ")
    for _ in range(3):
        print(" |                                |")
    print(" |          1.Manhattan           |")
    print(" |         2.Empty space          |")
    print(" |       3.Double heuristic       |")
    for _ in range(2):
        print(" |                                |")
    print(" |________________________________|\n")


class Loader:
    """
    A purely aesthetic function. Makes waiting for the algorithms to be done more pleasant.
    """
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿ ", "⣻ ", "⣽ ", "⣾ ", "⣷ ", "⣯ ", "⣟ ", "⡿ "]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()