#Given two linked lists of size N and M, which are sorted in non-decreasing order. The task is to merge them in such a way that the resulting list is in non-increasing order.


"""
Input:
N = 2, M = 2
list1 = 1->3
list2 = 2->4
Output:
4->3->2->1
Explanation:
After merging the two lists in non-increasing order, we have new lists as 4->3->2->1.
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def mergeResult(self, h1, h2):
        """
        Merge two sorted linked lists in non-decreasing order.

        Args:
        - h1 (Node): Head of the first sorted linked list.
        - h2 (Node): Head of the second sorted linked list.

        Returns:
        - Node: Head of the merged sorted linked list.
        """
        # Create a dummy node to serve as the head of the merged list
        dummy = Node(0)
        tail = dummy  # Initialize a pointer to the dummy node

        # Traverse both lists until one of them reaches the end
        while h1 and h2:
            if h1.data <= h2.data:
                tail.next = h1
                h1 = h1.next
            else:
                tail.next = h2
                h2 = h2.next
            
            tail = tail.next  # Move the tail pointer to the newly added node

        # Attach any remaining nodes from list1 or list2
        if h1:
            tail.next = h1
        if h2:
            tail.next = h2

        # Find the actual head of the merged list by reversing it
        return self.reverseList(dummy.next)

    def reverseList(self, head):
        """
        Reverse a linked list.

        Args:
        - head (Node): Head of the linked list.

        Returns:
        - Node: Head of the reversed linked list.
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev

