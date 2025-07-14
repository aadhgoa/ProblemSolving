"""
41. First Missing Positive
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: The smallest postive integer missing from nums is 2.

Intuition:
The problem requires me to find the smallest postive integer that is not present in the given array.

To solve this problem, I will use the following approach:
1. Iterate through the array and for each number, if it is in the range [1, n] (where n is the length of the array),
I will place it at its correct index (i.e., nums[i] should be at index nums[i] - 1).
2. After rearranging the numbers, I will iterate through the array again to find the first index where the number is not equal to its index + 1.
3. The first missing positive integer will be index + 1.
"""
from typing import List

class Solution:
    def find_missing_positive(self, nums: List[int]) -> int:
        """
        Find the first missing positive integer in an unsorted array.
        
        Args:
            nums (List[int]): List of integers.
            
        Returns:
            int: The first missing positive integer.
        
        Example:
            >>> find_missing_positive([3, 4, -1, 1])
            2
        """

        n: int = len(nums)

        # Step 1: Place each number in its correct index
        for i in range(n):
            while (
                1 <= nums[i] <= n
                and nums[nums[i] - 1] != nums[i]
            ):
                # Swap nums[i] with nums[nums[i] -1]
                nums[nums[i] - 1] , nums[i] = nums[i], nums[nums[i] - 1]

        # Step 2: Find the first missing positive integer
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        # If all numbers from 1 to n are present, return n + 1
        return n + 1
    

def main():
    solution = Solution()
    nums = [3, 4, -1, 1]
    print(solution.find_missing_positive(nums))  # Output: 2

if __name__ == "__main__":
    main()