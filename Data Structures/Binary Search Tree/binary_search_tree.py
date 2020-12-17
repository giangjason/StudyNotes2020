from binarytree import Node
from typing import List
from helper import Helper
from queue import Queue
import sys

def delete(root: Node, val: int) -> Node:
    if root is None:
        return None

    if val < root.val:
        # Delete from left subtree if val is less than current node.
        root.left = delete(root.left, val)
    elif val > root.val:
        # Delete from right subtree if val is less than current node.
        root.right = delete(root.right, val)
    else:
        
        # Return the left subchild and mark the current node as None
        # if no right subchild exists.
        if root.right is None:
            left = root.left
            root = None
            return left

        # Return the right subchild and mark the current node as None
        # if no left subchild exists.
        if root.left is None:
            right = root.right
            root = None
            return right

        # If the node has both children, get the minimum node in the right subtree.
        # This will be the node that replaces the current node. 
        right_min = get_min(root.right)
        root.val = right_min.val

        # Delete the minimum node retrieved from the right subtree from the right subtree.
        root.right = delete(root.right, right_min.val)

    return root



def get_max(root: Node) -> Node:
    """Gets the node containing the maximum value in the tree.

    Args:
        root (Node): The root of the tree to search through.

    Returns:
        Node: The reference to the node containing the maximum value. None if the tree is empty.
    """
    if root is None:
        return None
    if root.right:
        return get_max(root.right)
    return root

def get_min(root: Node) -> Node:
    """Gets the node containing the minimum value in the tree.

    Args:
        root (Node): The root of the tree to search through.

    Returns:
        Node: The reference to the node containing the minimum value. None if the tree is empty.
    """
    if root is None:
        return None
    if root.left:
        return get_min(root.left)
    return root

def insert(root: Node, val: int) -> Node:
    """Creates and inserts a node into the tree.

    Time complexity: 
        Average: O(logn)
        Worst: O(n) - inserting a sorted list

    Args:
        root (Node): The root of the tree to insert the node into.
        val (int): The value of the new node.

    Returns:
        Node: Returns the root of the tree being inserted into.
    """
    if root is None:
        return Node(val)

    if val < root.val:
        # Insert into the left subtree if val is lesser than current node.
        root.left = insert(root.left, val)
    else:
        # Insert into the right subtree if val is greater or equal to the current node.
        root.right = insert(root.right, val)
    return root

def print_breadth_first(root: Node) -> None:
    """Traverses the tree level by level and prints out the value of each node.

    Args:
        root (Node): The root of the tree to traverse.
    """
    if root is None:
        print(None)

    que = Queue()
    que.put(root)

    while not que.empty():
        curr = que.get()
        print(curr.val, end=" -> ")
        
        if curr.left:
            # Add the left subchild to the stack if exists.
            que.put(curr.left)

        if curr.right:
            # Add the right subchild to the stack if exists.
            que.put(curr.right)


def print_inorder(root: Node) -> None:
    """Inorder traverses the tree and prints out the value of each node.

    Args:
        root (Node): The root of the tree to traverse.
    """
    if root is None:
        print(None)
    if root.left:
        print_inorder(root.left)
    print(root.val, end=" -> ")
    if root.right:
        print_inorder(root.right)

def print_preorder(root: Node) -> None:
    """Preorder traverses the tree and prints out the value of each node.

    Args:
        root (Node): The root of the tree to traverse.
    """
    if root is None:
        print(None)
    print(root.val, end=" -> ")
    if root.left:
        print_preorder(root.left)
    if root.right:
        print_preorder(root.right)

def print_postorder(root: None) -> None:
    """Postorder traverses the tree and prints out the value of each node.

    Args:
        root (Node): The root of the tree to traverse.
    """
    if root is None:
        print(None)
    if root.left:
        print_postorder(root.left)
    if root.right:
        print_postorder(root.right)
    print(root.val, end=" -> ")

def search(root: Node, val: int) -> Node:
    """Searches a tree for the given value.

    Time complexity: 
        Average: O(logn)
        Worst: O(n) 

    Args:
        root (Node): The root of the tree to search through.
        val (int): The value of the node to search for.

    Returns:
        Node: The reference to the node being searched for. None if not in tree.
    """
    if root is None:
        return None

    if val == root.val:
        # Return the reference if node is found.
        return root
    elif val < root.val:
        # Search through left subtree if value is less than current node.
        return search(root.left, val)
    else:
        # Search through right subtree if value is greather or equal to current node.
        return search(root.right, val)

def construct_binary_search_tree(r: int, nums: List[int]) -> Node:
    """Constructs a binary search tree

    Args:
        r (int): The root key.
        nums (List[int]): The list of numbers to insert into the tree.

    Returns:
        Node: The root node of the binary search tree.
    """
    root = Node(r)
    for num in nums:
        insert(root, num)
    return root

def main():

    low = 0
    high = 100
    length = 20

    nums = Helper().generate_random_list(low, high, length)
    print(nums)

    root = construct_binary_search_tree(nums[0], nums[1:])

    print("\n")
    print("-----Binary Search Tree-----")
    print(root)

    if length <= 30:
        print("\n")
        print("------Inorder Traversal------")
        print_inorder(root)

        print("\n")
        print("------Preorder Traversal------")
        print_preorder(root)

        print("\n")
        print("------Postorder Traversal------")
        print_postorder(root)

        print("\n")
        print("------Breadth First Traversal-----")
        print_breadth_first(root)

    print("\n")
    pos_test = nums[length // 4]
    neg_test1 = (low * 2) - 1
    neg_test2 = (high * 2) + 1
    pos_test_result = search(root, pos_test)
    neg_test1_result = search(root, neg_test1)
    neg_test2_result = search(root, neg_test2)
    print("Contains {0}?:\t({1})".format(pos_test, False if pos_test_result is None else pos_test_result.val == pos_test))
    print("Contains {0}?:\t({1})".format(neg_test1, False if neg_test1_result is None else neg_test1_result.val == neg_test1))
    print("Contains {0}?:\t({1})".format(neg_test2, False if neg_test2_result is None else neg_test2_result.val == neg_test2))

    print("\n")
    print("-----Subtree of {0}-----".format(pos_test))
    pos_test_node = search(root, pos_test)
    print(pos_test_node)

    print("\n")
    min_node = get_min(root)
    max_node = get_max(root)
    print("Min node of the tree:\t({0})".format(min_node.val))
    print("Max node of the tree:\t({0})".format(max_node.val))

    print("\n")
    print("-----Deleting {0}-----".format(pos_test))
    delete(root, pos_test)
    print(root)

    print("\n")
main()