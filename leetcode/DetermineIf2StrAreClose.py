#Two strings are considered close if you can attain one from the other using the following operations:

#Operation 1: Swap any two existing characters.
#For example, abcde -> aecdb
#Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
#For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
#You can use the operations on either string as many times as necessary.

#Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

"""
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
"""

class Solution:
    def closeStrings(self, word1:str, word2:str)->bool:
        """
        Check if two words are considered close according to the provided criteria.
        
        Args:
            -word1 (str): The first word.
            -word2 (str): The second word.

        Returns:
            - bool: True if the words are close, False otherwise.
        """


        if len(word1) != len(word2):
            return False

        #Freq list
        freq_word1 = {}
        freq_word2 = {}

        #Iterate through both the words to calcutate the frequencies.

        for char in word1:
            freq_word1[char] = freq_word1.get(char, 0) + 1

        for char in word2:
            freq_word2[char] = freq_word2.get(char, 0) + 1

        #check if the set of characters are same in both the words.
        if set(freq_word1.keys()) != set(freq_word2.keys()):
            return False

        #Check if the sorted frequency count is the same for both the words.
        return sorted(freq_word1.values()) == sorted(freq_word2.values())
