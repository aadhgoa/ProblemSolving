#You are given an integer array matches where matches[i] = [winner, loser] indeicatesthat the platerwinner defeated player loser in a match.
#Return a llist answer of size 2 where :
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.

# The values in the two lists should be returned in increasing order.return

"""
Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].
"""

from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        """
        Given a list of match results, returns a list of winners:
        - winners[0] is a list of players who have not lost any matches.
        - winners[1] is a list of players who have lost exactly one match.

        Args:
        - matches (List[List[int]]): List of match results, where each element is [winner, loser].

        Returns:
        - List[List[int]]: A list containing two lists - players who have not lost any matches and players who lost once.
        """

        # Dictionary to store the count of wins for each player
        winner_count = {}

        # Dictionary to store the count of losses for each player
        loser_count = {}

        # Process matches and update win and lose counts
        for winner, loser in matches:
            winner_count[winner] = winner_count.get(winner, 0) + 1
            loser_count[loser] = loser_count.get(loser, 0) + 1

        # Identify players who have not lost any matches
        not_lost_any = [player for player in winner_count if player not in loser_count]

        # Identify players who have lost exactly one match
        lost_once = [player for player in loser_count if loser_count[player] == 1]

        # Sort the results in increasing order
        not_lost_any.sort()
        lost_once.sort()

        return [not_lost_any, lost_once]

# Example usage:
solution = Solution()
matches1 = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
output1 = solution.findWinners(matches1)
print(output1)  # Output: [[1, 2, 10], [4, 5, 7, 8]]
