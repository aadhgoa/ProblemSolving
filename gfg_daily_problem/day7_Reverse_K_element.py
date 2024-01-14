#Given an integer K and a queue of integers, we need to reverse the order of the first K elements of the queue, leaving the other elements in the same relative order.

#Only following standard operations are allowed on queue.

#enqueue(x) : Add an item x to rear of queue
#dequeue() : Remove an item from front of queue
#size() : Returns number of elements in queue.
#front() : Finds front item.
#Note: The above operations represent the general processings. In-built functions of the respective languages can be used to solve the problem.


"""
Input:
5 3
1 2 3 4 5
Output: 
3 2 1 4 5
Explanation: 
After reversing the given
input from the 3rd position the resultant
output will be 3 2 1 4 5.
"""

class Solution:
    def modifyQueue(self, q: list, k: int) -> list:
        """
        Reverse the order of the first K elements in the given queue.

        Args:
        - q (list): The input queue.
        - k (int): The number of elements to reverse.

        Returns:
        - list: The modified queue after reversing the first K elements.
        """
        # Check if the value of k is invalid
        if k <= 0 or k > len(q):
            return ("Invalid value of k")

        stack = []

        # Push the first K elements into the stack
        for _ in range(k):
            stack.append(q.pop())

        # Pop elements from the stack and enqueue them back to reverse the order
        while stack:
            q.append(stack.pop())

        # Enqueue the remaining elements to maintain their order
        for _ in range(len(q) - k):
            q.append(q.pop())

        return q
