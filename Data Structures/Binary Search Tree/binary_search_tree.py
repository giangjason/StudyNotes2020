from __future__ import annotations
from typing import Type

class Node():

    def __init__(self, key: int, left: Node = None, right: Node = None) -> Node:
        """Initializes an instances of a Node object.

        Args:
            key (int): The key of the node      
            left ([type], optional): The left child of the node. Defaults to None:Node.
            right ([type], optional): The right child of the node. Defaults to None:Node.

        Returns:
            Node: [description]
        """
        self.key = key
        self.left = left
        self.right = right
