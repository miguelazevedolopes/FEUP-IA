from state import *
import keyboard


def execute_move(state):
    """
    Executes the moves made by the player
    """
    key=None
    if os.name != 'nt': # checks if os isn't Windows
        os.system("stty -echo") # removes echo of input (only works in linux)
    while (key==None):
        key=keyboard.read_hotkey(suppress=False)
        if key == 'w':
            if can_move_up(state):
                if os.name != 'nt':
                    os.system("stty echo") # turns input echo on again
                return move_up(state)
            else:
                print("You can't move up.")
                key=None
        elif key == 's':
            if can_move_down(state):
                if os.name != 'nt':
                    os.system("stty echo")
                return move_down(state)
            else:
                print("You can't move down.")
                key=None
        elif key == 'd':
            if can_move_right(state):
                if os.name != 'nt':
                    os.system("stty echo")
                return move_right(state)
            else:
                print("You can't move right.")
                key=None
        elif key == 'a':
            if can_move_left(state):
                if os.name != 'nt':
                    os.system("stty echo")
                return move_left(state)
            else:
                print("You can't move left.")
                key=None
        else:
            key=None
    return state


def clear_input():
    """
    Clears input line
    """
    if os.name == 'nt':
        from pynput.keyboard import Key, Controller
        kb = Controller()
        kb.press (Key.ctrl_l )
        kb.press (Key.home )
        time.sleep(0.5)
        kb.release (Key.ctrl_l )
        kb.release (Key.home )
    else:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def get_menu_option():
    """
    Gets main menu option chosen by the user
    """
    while True:
        try:
            option = int(input("Please select a valid option:"))
        except ValueError:
            continue
        if (option == 1 or option == 2):
            break
        else:
            continue
    return option


def get_algorithm_option():
    """
    Gets algorithm chosen by the user
    """
    while True:
        try:
            option = int(input("Please select a valid option:"))
        except ValueError:
            continue
        if (option == 1 or option == 2 or option == 3):
            break
        else:
            continue
    return option


def get_end_option():
    """
    Gets leaving option chosen by the user
    """
    clear_input()

    while True:
        try:
            option = int(input("Please select 0 to leave or 1 to play again:"))
        except ValueError:
            continue
        if (option == 0 or option == 1):
            break
        else:
            continue
    return option


def get_greedy_option():
    """
    Gets greedy heuristics option chosen by the user
    """
    while True:
        try:
            option = int(input("Please select a version of the greedy algorithm desired:"))
        except ValueError:
            print("Must be between 1 and 3")

        if(option == 1 or option == 2 or option == 3):
            break
        else:
            continue
    return option


