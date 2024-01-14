#Given a singly linked list, sort the list (in ascending order) using insertion sort algorithm.

"""
Input:
N = 10
Linked List = 30->23->28->30->11->14->
              19->16->21->25 
Output : 
11 14 16 19 21 23 25 28 30 30 
Explanation :
The resultant linked list is sorted.
"""

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def insertionSort(self, head):
        """
        Sorts a linked list in ascending order using the insertion sort algorithm.

        Args:
        - head: The head of the linked list.

        Returns:
        - Node: The head of the sorted linked list.
        """
        # Create a dummy node for the sorted linked list
        dummy = Node(float('-inf'))

        # Pointer to traverse the original linked list
        current = head

        while current:
            # Save the next node before disconnecting it
            next_node = current.next

            # Find the correct position to insert the current node in the sorted list
            prev, current_sorted = dummy, dummy.next

            while current_sorted and current_sorted.data < current.data:
                prev, current_sorted = current_sorted, current_sorted.next

            # Insert the current node into the sorted list
            prev.next, current.next = current, current_sorted

            # Move to the next node in the original list
            current = next_node

        return dummy.next
