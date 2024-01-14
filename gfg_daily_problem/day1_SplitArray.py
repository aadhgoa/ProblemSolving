#Split Array Largest Sum
#Given an array arr[] of N elements and a number K., split the given array into K subarrays such that the maximum subarray sum achievable out of K subarrays formed is minimum possible. Find that possible subarray sum.

"""
Input:
N = 3, K = 2
A[] = {1, 1, 2}
Output:
2
Explanation:
Splitting the array as {1,1} and {2} is optimal.
This results in a maximum sum subarray of 2.
"""

#User function Template for python3

class Solution:
    def isPossible(self, arr, N, K, mid)->bool:
        """
        Checks if it's possible to split the array into K subarrays
        with a maximum sum less than or equal to the given mid value.

        Args:
        - arr: The input array of integers.
        - N: The size of the array.
        - K: The number of subarrays to split the array into.
        - mid: The maximum sum allowed for each subarray.

        Returns:
        - bool: True if it's possible to split the array into K subarrays
                with a maximum sum less than or equal to mid, False otherwise.
        """
        count = 1  # Initialize the count of subarrays
        _sum = 0   # Initialize the current sum

        for i in range(N):
            _sum += arr[i]
            if _sum > mid:
                count += 1  # Increment the count for a new subarray
                _sum = arr[i]  # Reset the sum for the new subarray

        return count <= K  # Check if the count of subarrays is less than K
        
    def splitArray(self, arr, N, K):
        """
        Performs a binary search to find the minimum possible maximum sum of subarrays
        when splitting the given array into K subarrays.

        Args:
        - arr: The input array of integers.
        - N: The size of the array.
        - K: The number of subarrays to split the array into.

        Returns:
        - int: The minimum possible maximum sum of subarrays.
        """

        # Initialize the low and high values for binary search
        low = max(arr)  # Minimum possible maximum sum of subarrays
        high = sum(arr)  # Maximum possible maximum sum of subarrays

        result = 0  # Initialize the result to store the minimum possible maximum sum

        # Perform binary search until low <= high
        while low <= high:
            mid = low + (high - low) // 2  # Calculate mid value

            # Check if it's possible to split the array into K subarrays
            # with a maximum sum less than or equal to mid
            if self.isPossible(arr, N, K, mid):
                result = mid  # Update the result to the current mid
                high = mid - 1  # Update the upper limit for binary search
            else:
                low = mid + 1  # Update the lower limit for binary search

        return result  # Return the minimum possible maximum sum of subarrays 


solution = Solution()
arr = [1, 1, 2]
K = 2
N = 3
result = solution.splitArray(arr,N, K)
print(result)

