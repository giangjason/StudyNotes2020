from binarytree import Node
from typing import List
from queue import Queue
import random


class Helper():

    def generate_random_list(self, low: int, high: int, length: int) -> List[int]:
        """Generates a random list of numbers

        Args:
            low (int): The lowest possible value in the list
            high (int): The highest possible value in the list
            length (int): The length of the list

        Returns:
            List[int]: Returns a random list of numbers
        """
        nums = []
        while len(nums) <= length:
            rand_num = random.randint(low, high)
            nums.append(rand_num)
        return nums


    def construct_binary_tree(self, nums: List[int]) -> Node:
        """Constructs a binary tree from a given list of numbers.

        Args:
            nums (List[int]): The list of numbers to construct the binary tree.

        Returns:
            Node: The root of the binary tree.
        """

        def _insert(root: Node, val: int) -> None:
            if root is None:
                return
            
            que = Queue()
            que.put(root)

            while not que.empty():
                curr = que.get()

                if curr.left:
                    que.put(curr.left)
                else:
                    curr.left = Node(val)
                    break

                if curr.right:
                    que.put(curr.right)
                else:
                    curr.right = Node(val)
                    break

        root = Node(nums[0])
        for num in nums[1:]:
            _insert(root, num)
        
        return root

        
