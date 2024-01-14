#Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

#In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

#Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.


#Function to find a continuous sub-array which adds up to a given number.

"""
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.
"""


class Solution:
    def subArraySum(self,arr, n, s):
       #Write your code here
         if s == 0:  # Handling the case where required sum is zero
            return [1, 1] if 0 in arr else [-1]
       start = end = sum_arr=0
       found=False

       while end < n:
           sum_arr += arr[end]

           if sum_arr > s:
               sum_arr -= arr[start]
               start +=1
            
            if sum_arr == s:
                found=True
                break

        end += 1

        if found:
            return [start+1, end+1]
        else:
            return [-1]


