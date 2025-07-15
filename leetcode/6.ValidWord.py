"""
A word is considered valid if:

It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.

Notes:

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.

Input: word = "234Adas"
Output: true
Explanation: The word contains 7 characters, includes digits and letters, has vowels ('a'), and has consonants ('d', 's').

Intution:
1. Check if the length of the word is at least 3 characters.
2. Check if the word contains at least one vowel and one consonant.
3. Check if the word contains only valid characters (digits and letters).
"""


class Solution:
    def isValidWord(self, word: str) -> bool:
        """
        Checks if a word is valid based on the following criteria:
        - Contains at least 3 characters.
        - Contains only digits and English letters (uppercase and lowercase).
        - Includes at least one vowel.
        - Includes at least one consonant.

        Args:
            word (str): The input word to validate.

        Returns:
            bool: True if the word is valid, False otherwise.
        """
        if len(word) < 3:
            return False

        vowels: set[str] = set("aeiouAEIOU")
        has_vowel: bool = False
        has_consonant: bool = False

        for char in word:
            if char.isdigit() or char.isalpha():
                if char in vowels:
                    has_vowel = True
                elif char.isalpha():
                    has_consonant = True
            else:
                return False

        return has_vowel and has_consonant and len(word) >= 3


def main():
    # Example usage:
    solution = Solution()
    print(solution.isValidWord("234Adas"))  # Output: True
    print(solution.isValidWord("ab1"))  # Output: True
    print(solution.isValidWord("a"))  # Output: False
    print(solution.isValidWord("abc"))  # Output: True


if __name__ == "__main__":
    main()
