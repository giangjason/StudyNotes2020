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

    def delete(self, key: int) -> Node:
        """Deletes the node associated with the given key.

        Time Complexity:
            Best: O(logn) 
            Average: O(logn)
            Worst: O(h) where h=height - when the key to delete for is the smallest or greatest.

        Args:
            key (int): The key of the node to delete

        Returns:
            Node: [description]
        """
        if not self: return self

        if key < self.key:
            # Delete from the left subtree if key is less than current key
            # Set the left child to the subtree with the key deleted
            self.left = self.left.delete(key)
        elif key > self.key: 
            # Delete from the right subtree if key is greater than current key 
            # Set the right child to the subtree with the key deleted.
            self.right = self.right.delete(key)
        else:
            # Delete the current node

            # Case where the node does not have a left child
            if not self.left:
                tmp = self.right
                self = None
                return tmp

            # Case where the node does not have a right child
            elif not self.right:
                tmp = self.left
                self = None
                return tmp

            # Case where the node has neither left nor right child
            tmp = self.right.min()
            self.key = tmp.key
            self.right = self.right.delete(tmp.key)

        return self
        
    def display(self):
        """Prints out the entire tree with the current node as the root."""
        if self: 
            lines, _, _, _ = self._display_aux()
            for line in lines:
                print(line)
        else: 
            print(None)

    def get_node(self, key: int) -> Node:
        """Gets the first node associated to the key

        Time Complexity:
            Best: O(1) - when the root is the key searched for.
            Average: O(logn)
            Worst: O(h) where h=height - when the key searched for is the smallest or greatest.

        Args:
            key (int): The key of the node to retrieve

        Returns:
            Node: Returns the node with the key searched for.
        """
        if key == self.key:
            return self
        elif key < self.key:
            # Search the left subtree, if exists, if the search key is less than the current key
            return self.left.get_node(key) if self.left else None
        else:
            # Search the right subtree, if exists,  if the search key is greater than the current key
            return self.right.get_node(key) if self.right else None

    def insert(self, key: int) -> None:
        """Creates a node and inserts into the binary search tree.
        
        Time Complexity:
            Best: O(logn) - when the tree contains only the root
            Average: O(logn)
            Worst: O(h) where h=height - then the key entered is the smallest or greatest in the tree.

        Args:
            key (int): The key of the new node created
        """
        if key < self.key:
            if self.left: 
                # Insert into the left subtree if it exists
                self.left.insert(key)
            else: 
                # Set as the left child if empty
                self.left = Node(key)
        else:
            if self.right:
                # Insert into right subtree if it exists
                self.right.insert(key)
            else:
                # Set as the right child if empty
                self.right = Node(key)

    def max(self) -> Node:
        """Gets the max node of the current tree.

        Returns:
            Node: The node that contains the max value in the tree.
        """
        if self.right:
            return self.right.max()
        return self

    def min(self) -> Node:
        """Gets the min node of the current tree

        Returns:
            Node: The node that contains the min value in the tree.
        """
        if self.left:
            return self.left.min()
        return self

    def print_inorder(self) -> None:
        """Prints the tree via inorder traversal."""
        if self.left: self.left.print_inorder()
        print(self.key, end=" ")
        if self.right: self.right.print_inorder()

    def print_preorder(self) -> None:
        """Prints the tree via preorder traversal"""
        print(self.key, end=" ")
        if self.left: self.left.print_preorder()
        if self.right: self.right.print_preorder()

    def print_postorder(self) -> None:
        """Prints the tree via postorder traversal"""
        if self.left: self.left.print_postorder()
        if self.right: self.right.print_postorder()
        print(self.key, end=" ")

    def search(self, key: int) -> bool:
        """Searches a binary search tree for a given node.

        Time Complexity:
            Best: O(1) - when the root is the key searched for.
            Average: O(logn)
            Worst: O(h) where h=height - when the key searched for is the smallest or greatest.

        Args:
            key (int): The key to search for.

        Returns:
            bool: True if found, False if not in tree
        """
        if key == self.key:
            return True
        elif key < self.key:
            # Search the left subtree, if exists, if the search key is less than the current key
            return self.left.search(key) if self.left else False

        else:
            # Search the right subtree, if exists,  if the search key is greater than the current key
            return self.right.search(key) if self.right else False


    ## Following method is for display purposes only. Private auxillory method.
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2