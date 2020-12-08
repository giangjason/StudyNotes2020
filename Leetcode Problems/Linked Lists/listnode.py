from __future__ import annotations

class ListNode():

    def __init__(self, val:int=0, next:ListNode=None):
        """Constructs a new instance of the ListNode class.

        Args:
            val (int, optional): The value of the list node. Defaults to 0.
            next ([type], optional): [description]. Defaults to None.
        """
        self.val = val
        self.next = next