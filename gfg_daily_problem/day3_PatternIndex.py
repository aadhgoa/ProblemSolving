#Given two strings, one is a text string, txt and other is a pattern string, pat. The task is to print the indexes of all the occurences of pattern string in the text string. Use one-based indexing while returing the indices. 
#Note: Return an empty list incase of no occurences of pattern. Driver will print -1 in this case.


"""
Input:
txt = "geeksforgeeks"
pat = "geek"
Output:
1 9
Explanation:
The string "geek" occurs twice in txt, one starts are index 1 and the other at index 9.
"""

class Solution:
    def search(self, pat: str, txt: str) -> list:
        """
        Search for all occurrences of a pattern string in a text string.

        Args:
        - pat (str): Pattern string to search for.
        - txt (str): Text string in which to search.

        Returns:
        - list: A list containing the indices of all occurrences of the pattern string in the text string (1-based indexing).
        """
        indices = []  # List to store the indices of occurrences
        start = 0  # Starting index for searching in the text string

        while True:
            # Find the index of the pattern string in the text string
            index = txt.find(pat, start)

            if index == -1:  # If the pattern is not found, break the loop
                break

            indices.append(index + 1)  # Append the index of occurrence to the list
            start = index + 1  # Update the starting index for the next search

        return indices

if __name__ == "__main__":
    main()
