#Given an array arr containing N integers and a positive integer K, find the length of the longest sub array with sum of the elements divisible by the given value K

"""
Input:
N = 6, K = 3
arr[] = {2, 7, 6, 1, 4, 5}
Output:
4
Explanation:
The subarray is {7, 6, 1, 4} with sum 18, which is divisible by 3.
"""
class Solution:
    def longSubarrWthSumDivByK(self, arr, n, K)->int:
        """
        Calculate the length of the longest subarray with sum divisible by K.

        Args:
        - arr (list): The input array of integers.
        - n (int): The size of the input array.
        - K (int): The divisor to check for subarray sum divisibility.

        Returns:
        - int: The length of the longest subarray with a sum divisible by K.
        """

        remainder_indexes = {0: -1}  # Store remainder and its index
        current_sum = 0  # Initialize current sum
        max_length = 0  # Initialize maximum length of subarray with sum divisible by K

        for i, num in enumerate(arr):  # Loop through the array elements and their indices
            current_sum += num  # Calculate the running sum

            # Calculate the modulo to handle negative values
            current_modulo = ((current_sum % K) + K) % K

            if current_modulo in remainder_indexes:  # If current modulo is in the dictionary
                # Update max_length if current subarray length is greater than the previous max_length
                max_length = max(max_length, i - remainder_indexes[current_modulo])
            else:
                # Store the index of the current remainder if seen for the first time
                remainder_indexes[current_modulo] = i

        return max_length  # Return the maximum length of subarray with sum divisible by K

