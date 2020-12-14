import sys
from binary_search_tree import Node
from typing import List
from helper import Helper

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
        root.insert(num)
    return root

def main():
    
    low = -50
    high = 50
    length = 20

    args = sys.argv
    if len(args) > 1:
        nums = [int(arg) for arg in args[1:]]
        r = nums[0]
    else:
        nums = Helper().generate_random_list(low, high, length)
        r = nums[0]

    root = construct_binary_search_tree(r, nums)

    print("\n")
    print("-----Binary Search Tree-----")
    root.display()

    if length <= 25:
        print("\n")
        print("------Inorder Traversal------")
        root.print_inorder()

        print("\n")
        print("------Preorder Traversal------")
        root.print_preorder()

        print("\n")
        print("------Postorder Traversal------")
        root.print_postorder()

    print("\n")
    pos_test = nums[length // 2]
    neg_test1 = (low * 2) - 1
    neg_test2 = (high * 2) + 1
    pos_test_result = root.search(pos_test)
    neg_test1_result = root.search(neg_test1)
    neg_test2_result = root.search(neg_test2)
    print("Contains {0}?:\t({1})".format(pos_test, pos_test_result))
    print("Contains {0}?:\t({1})".format(neg_test1, neg_test1_result))
    print("Contains {0}?:\t({1})".format(neg_test2, neg_test2_result))

    print("\n")
    print("-----Subtree of {0}-----".format(pos_test))
    pos_test_node = root.get_node(pos_test)
    pos_test_node.display()

    print("\n")
    min_node = root.min()
    max_node = root.max()
    print("Min node of the tree:\t({0})".format(min_node.key))
    print("Max node of the tree:\t({0})".format(max_node.key))

    print("\n")
    print("-----Deleting {0}-----".format(pos_test))
    root.delete(pos_test)
    root.display()

    print("\n")

# if __name__ == "__main__":
#     main()

main()