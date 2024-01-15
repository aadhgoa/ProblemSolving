#You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

#Return the minimum number of steps to make t an anagram of s.

#An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.


"""
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
"""



class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        Calculate the minimum number of steps to make string 't' an anagram of string 's'.

        Args:
        - s (str): The input string.
        - t (str): The target string.

        Returns:
        - int: The minimum number of steps needed for replacements.
        """
        # Check if the lengths of both strings are not equal
        if len(s) != len(t):
            return -1  # Invalid input, lengths should be equal

        # Initialize dictionaries to store character counts
        count_s = {}
        count_t = {}

        # Update counts for string s
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        # Update counts for string t
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        # Calculate the absolute differences between counts
        differences = {char: abs(count_s[char] - count_t.get(char, 0)) for char in set(count_s) | set(count_t)}

        # Sum the absolute differences to get the total number of replacements needed
        total_replacement = sum(differences.values())
        total_replacement = total_replacement//2

        return total_replacement

