from binarytree import Node
from typing import List
from helper import Helper
from queue import Queue

def delete(root: Node, val: int) -> Node:
    """Deletes a node from the binary tree.

    Args:
        root (Node): The root of the tree to delete from.
        val (int): The value of the node to delete.

    Returns:
        Node: The root of the tree. None if tree is empty
    """

    def _delete_last(last: Node) -> None:
        que = Queue()
        que.put(root)

        while not que.empty():
            curr = que.get()

            # Set the current node to None if the current node is the last node
            if curr is last:
                curr = None
                break
            
            # Set the left child to None if it is the last node,
            # otherwise add it to the queue if it exists.
            if curr.left:
                if curr.left is last:
                    curr.left = None
                    break
                que.put(curr.left)

            # Set the right child to None if it is the last node,
            # otherwise add it to the queue if it exists.
            if curr.right:
                if curr.right is last:
                    curr.right = None
                    break
                que.put(curr.right)

    if root is None:
        return None

    que = Queue()
    que.put(root)

    last_node = None
    delete_node = None
    while not que.empty():
        curr = que.get()

        # Set the delete node as the current node if it contains the value searched for.
        if curr.val == val:
            delete_node = curr
        
        # Add the left child to the queue if exists
        if curr.left:
            que.put(curr.left)

        # Add the right child to the queue if exists
        if curr.right:
            que.put(curr.right)

        # Set the last node to the current node.
        last_node = curr

    if delete_node is None:
        return delete_node

    # Replace the deleted node's value with last node's value
    delete_node.val = last_node.val

    # Delete the last node in the tree.
    _delete_last(last_node)

def get_max(root: Node) -> Node:
    """Gets the node containing the maximum value in the tree.

    Time complexity:
        Average: O(n)
        Worst: O(n)

    Args:
        root (Node): The root of the tree to search.

    Returns:
        Node: The reference to the node containing the maximum value.
    """
    if root is None:
        return None

    que = Queue()
    que.put(root)

    max_node = None

    while not que.empty():
        curr = que.get()

        # Set the node containing the min value to the current node
        # if the max_node is None of if the current's value is smaller.
        if max_node is None or curr.val > max_node.val:
            max_node = curr

        # Add the left child to the queue if exists
        if curr.left:
            que.put(curr.left)

        # Add the right child to the queue if exists
        if curr.right:
            que.put(curr.right)

    return max_node

def get_min(root: Node) -> Node:
    """Gets the node containing the mininum value in the tree.

    Time complexity:
        Average: O(n)
        Worst: O(n)

    Args:
        root (Node): The root of the tree to search.

    Returns:
        Node: The reference to the node containing the minimum value.
    """
    if root is None:
        return None

    que = Queue()
    que.put(root)

    min_node = None

    while not que.empty():
        curr = que.get()

        # Set the node containing the min value to the current node
        # if the min_node is None of if the current's value is smaller.
        if min_node is None or curr.val < min_node.val:
            min_node = curr

        # Add the left child to the queue if exists
        if curr.left:
            que.put(curr.left)

        # Add the right child to the queue if exists
        if curr.right:
            que.put(curr.right)

    return min_node

def print_inorder(root: Node) -> None:
    """Inorder traverses the tree and prints every node value.

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
    """Preorder traverses the tree and prints every node value.

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

def print_postorder(root: Node) -> None:
    """Postorder traverses the tree and prints every node value.

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

def print_breadth_first(root: Node) -> None:
    """Traverses the tree level by level and prints every node value.

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

        # Add the left child to the queue if exists
        if curr.left:
            que.put(curr.left)

        # Add the right child to the queue if exists
        if curr.right:
            que.put(curr.right)

def insert(root: Node, val: int) -> Node:
    """Creates and inserts a node into the binary tree.

    Time complexity:
        Average: O(n)
        Worst: O(n)

    Args:
        root (Node): The root of the tree to insert into.   
        val (int): The value of the node to insert.
    
    Returns:
        Node: The root of the tree.
    """
    if root is None:
        return Node(val)

    que = Queue()
    que.put(root)

    while not que.empty():
        curr = que.get()

        if curr.left:
            # Add the left child to the queue if exists
            que.put(curr.left)
        else:
            # Set the new node as the left child if left child does not exist
            curr.left = Node(val)
            break

        if curr.right:
            # Add the right child to the queue if exists
            que.put(curr.right)
        else:
            # Set the new node as the right child if the right child does not exist
            curr.right = Node(val)
            break

    return root

def search(root: Node, val: int) -> Node:
    """Searches a binary tree for the given node.

    Args:
        root (Node): The root of the tree to search.
        val (int): The value of the node to search for.

    Returns:
        Node: The reference to the searched node. None if the node is not in the tree.
    """
    if root is None:
        return None

    que = Queue()
    que.put(root)

    while not que.empty():
        curr = que.get()

        # Return reference to node if val matches the node's val.
        if curr.val == val:
            return curr

        # Add the left child to the queue if exists.
        if curr.left:
            que.put(curr.left)
        
        # Add the right child to the queue if exists.
        if curr.right:
            que.put(curr.right)

    return None

def construct_binary_tree(r: int, nums: List[int]) -> Node:
    """Constructs a binary tree

    Args:
        r (int): The root key.
        nums (List[int]): The list of numbers to insert into the tree.

    Returns:
        Node: The root node of the binary tree.
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

    print("\n")
    print("-----Numbers Generated-----")
    print(nums)

    root = construct_binary_tree(nums[0], nums[1:])

    print("\n")
    print("-----Binary Tree-----")
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
    print("-----Deleting the root-----")
    delete(root, root.val)
    print(root)

    print("\n")
main()

