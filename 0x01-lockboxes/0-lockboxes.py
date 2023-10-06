#!/usr/bin/python3
"""
ALX Interview on Lockboxes
This code solve the problem of
lockbox by checking the state of every box
after traversing the keys
"""


def canUnlockAll(boxes):
    """
    Creates a register to know if the boxes are opened

    Args:
    boxes (list of list): List of boxes that contains the list of keys.
    Returns:
    True if all boxes can be opened, otherwise False
    """
    register = [0]
    for box in register:
        for key in boxes[box]:
            if key < len(boxes) and key not in register:
                register.append(key)
    if len(register) == len(boxes):
        return True
    return False
