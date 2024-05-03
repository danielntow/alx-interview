#!/usr/bin/python3
"""
lockbox module
"""

from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    Args:
        boxes (list of lists): A list of lists representing the
        boxes and their keys.

    Returns:
        bool: True if all boxes can be opened, else False.

    Examples:
        >>> boxes = [[1], [2], [3], [4], []]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        >>> canUnlockAll(boxes)
        True

        >>> boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        >>> canUnlockAll(boxes)
        False
    """
    # Check if boxes list is empty or None
    if not boxes or len(boxes) == 0:
        return False

    # Number of boxes
    n = len(boxes)

    # Set to store opened boxes, initially containing box 0
    opened = set([0])

    # Queue to store boxes to be visited
    queue = deque([0])

    # Perform BFS
    while queue:
        # Dequeue box
        box = queue.popleft()
        # Iterate through keys in the box
        for key in boxes[box]:
            # If key is not opened and within valid range
            if key not in opened and key < n:
                # Mark key as opened
                opened.add(key)
                # Add key to queue for further exploration
                queue.append(key)

    # Check if all boxes are opened
    return len(opened) == n
