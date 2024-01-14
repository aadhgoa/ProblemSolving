#Given a non-negative integer S represented as a string, remove K digits from the number so that the new number is the smallest possible.
#Note : The given num does not contain any leading zero.

"""
Input:
S = "149811", K = 3
Output:
111
Explanation:
Remove the three digits
4, 9, and 8 to form the new number 111
which is smallest.
"""
class Solution:
    def removeKdigits(self, S: str, K: int) -> str:
        """
        Remove K digits from the given number to create the smallest possible number.
        
        Args:
        - S (str): The input number as a string.
        - K (int): The number of digits to be removed.
        
        Returns:
        - str: The smallest possible number after removing K digits.
        """
        stack = []

        for digit in S:
            while stack and K > 0 and int(stack[-1]) > int(digit):
                stack.pop()
                K -= 1

            stack.append(digit)

        # Remove remaining K digits from the end
        while K > 0:
            stack.pop()
            K -= 1

        # Construct the result string
        result = "".join(stack).lstrip('0')
        
        return '0' if result == "" else result

