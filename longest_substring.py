"""
# Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

"""
Solution:
 1) I will need a dict of all characters with their indexes
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}  # Dictionary to store last seen indices of characters
        left = 0  # Left pointer for the sliding window
        max_length = 0  # Stores the length of the longest valid substring

        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1  # Move left pointer forward

            char_index[char] = right  # Update last seen index
            max_length = max(max_length, right - left + 1)  # Update max length

        return max_length

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "sdfhg", ""]
    
    for string in test_cases:
        print("Longest substring in '{}' has {} characters.".format(string, solution.lengthOfLongestSubstring(string)))
