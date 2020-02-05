import keyboard
import string
from threading import *


# I can't find a complete list of keyboard keys, so this will have to do:
keys = list(string.ascii_lowercase)
"""
Optional code(extra keys):
"""
keys.append("space_bar")
keys.append("shift")
keys.append("esc")
keys.append("up")
keys.append("left")
keys.append("right")
keys.append("down")
keys.append("ctrl")

def listen(key):
    while True:
        keyboard.wait(key)
        if key in action_dict:
            print("[+] Pressed",action_dict[key])
threads = [Thread(target=listen, kwargs={"key":key}) for key in keys]
for thread in threads:
    thread.start()



action_dict = {
    "d":'MOVE_EAST',
    "s":'MOVE_SOUTH',
    "w": 'MOVE_NORTH',
    "a": 'MOVE_WEST',
    "e": 'MOVE_NORTH_EAST',
    "q": 'MOVE_NORTH_WEST',
    "c": 'MOVE_SOUTH_EAST',
    "z": 'MOVE_SOUTH_WEST',
    "space_bar": 'JUMP',
    "up": 'LOOK_NORTH',
    "down": 'LOOK_SOUTH',
    "right": 'LOOK_EAST',
    "left": 'LOOK_WEST',
    "ctrl": 'MOVE_FORWARD',
    "x": 'BREAK_BLOCK',
    "r": 'COLLECT_FROM_BLOCK',
    "f": 'USE',
    "t": 'PLACE_CRAFTING_TABLE',
    "g": 'PLACE_TREE_TAP',
    "h": 'SELECT_AXE',
    "p": 'SELECT_POGO_STICK',
    "l": 'CRAFT_PLANKS',
    "k": 'CRAFT_CRAFTING_TABLE',
    "i": 'CRAFT_STICKS',
    "y": 'CRAFT_AXE',
    "b": 'CRAFT_TREE_TAP',
    "v": 'CRAFT_POGO_STICK'
}


"""
Version with gym implemented: YET TO TEST

import keyboard
import string
from threading import *

import PolycraftGym, time, json, numpy as np
import numpy as np
import cv2


gym = PolycraftGym.Gym('127.0.0.1', 9000)
gym.sock_connect()
gym.send_command("START")
gym.step_command("RESET domain ../experiments/pogo.psm")


keys = list(string.ascii_lowercase)


keys.append("space_bar")
keys.append("shift")
keys.append("esc")
keys.append("up")
keys.append("left")
keys.append("right")
keys.append("down")
keys.append("ctrl")

def listen(key):
    while True:
        keyboard.wait(key)
        if key in action_dict:
            print("[+] Pressed",action_dict[key])
            data = gym.step_command(action_dict[key])
            print(data)
threads = [Thread(target=listen, kwargs={"key":key}) for key in keys]
for thread in threads:
    thread.start()



action_dict = {
    "d":'MOVE_EAST',
    "s":'MOVE_SOUTH',
    "w": 'MOVE_NORTH',
    "a": 'MOVE_WEST',
    "e": 'MOVE_NORTH_EAST',
    "q": 'MOVE_NORTH_WEST',
    "c": 'MOVE_SOUTH_EAST',
    "z": 'MOVE_SOUTH_WEST',
    "space_bar": 'JUMP',
    "up": 'LOOK_NORTH',
    "down": 'LOOK_SOUTH',
    "right": 'LOOK_EAST',
    "left": 'LOOK_WEST',
    "ctrl": 'MOVE_FORWARD',
    "x": 'BREAK_BLOCK',
    "r": 'COLLECT_FROM_BLOCK',
    "f": 'USE',
    "t": 'PLACE_CRAFTING_TABLE',
    "g": 'PLACE_TREE_TAP',
    "h": 'SELECT_AXE',
    "p": 'SELECT_POGO_STICK',
    "l": 'CRAFT_PLANKS',
    "k": 'CRAFT_CRAFTING_TABLE',
    "i": 'CRAFT_STICKS',
    "y": 'CRAFT_AXE',
    "b": 'CRAFT_TREE_TAP',
    "v": 'CRAFT_POGO_STICK'
}


"""