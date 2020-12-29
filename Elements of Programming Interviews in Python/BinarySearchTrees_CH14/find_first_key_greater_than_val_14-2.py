'''
Write a function that returns the first key that would appear in an inorder traversal which is greater than the input value.
'''

from helper import Helper
import binarytree

def main():

    h = Helper()
    nums = h.generate_random_list(0, 100, 10)
    bst = binarytree.bst(nums)