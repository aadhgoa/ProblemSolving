#Given a boolean matrix of size RxC where each cell contains either 0 or 1, find the row numbers (0-based) of row which already exists or are repeated.

"""
Input:
R = 2, C = 2
matrix[][] = {{1, 0},
            {1, 0}}
Output: 
1
Explanation:
Row 1 is duplicate of Row 0.
"""

class Solution:
    def repeatedRows(self, arr, m, n):
        """
        Find the repeated rows in a boolean matrix.

        Args:
        - arr (List[List[int]]): Boolean matrix where each cell contains either 0 or 1.
        - m (int): Number of rows in the matrix.
        - n (int): Number of columns in the matrix.

        Returns:
        - List[List[int]]: List of repeated rows (as lists).
        """
        seen_rows = set()
        repeated_rows = []

        for row in range(m):
            tuple_row = tuple(arr[row])

            if tuple_row in seen_rows:
                # Append the row as a list to the result
                repeated_rows.append(list(arr[row]))
            else:
                seen_rows.add(tuple_row)

        return repeated_rows

# Example usage:
arr = [[1, 0], [1, 0], [0, 1]]
m, n = 3, 2
sol = Solution()
result = sol.repeatedRows(arr, m, n)
print(result)  # Output: [[1, 0]]

