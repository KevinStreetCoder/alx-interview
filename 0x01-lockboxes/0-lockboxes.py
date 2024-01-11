#!/usr/bin/python3

'''LockBoxes Challenge'''

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of boxes, where each box is represented as a list of keys.

    Returns:
    - bool: True if all boxe_s can be opened, False otherwise.
    """
    # Set to keep track of opened boxes
    opened_boxes = set([0])

    # List to keep track of boxes to be explored
    boxes_to_explore = [0]

    # Explore boxes
    while boxes_to_explore:
        current_box = boxes_to_explore.pop()

        # Get keys in the current box
        keys = boxes[current_box]

        for key in keys:
            # If the key opens a new box and that box hasn't been opened yet
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                boxes_to_explore.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)

