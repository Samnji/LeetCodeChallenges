"""
5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest 
palindromic
 
substring
 in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, max_length = 0, 0

        def expand_around_center(left: int, right: int):
            nonlocal start, max_length
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_length:
                    start, max_length = left, right - left + 1
                left -= 1
                right += 1

        for i in range(len(s)):
            print(i)
            expand_around_center(i, i)      # Odd-length palindrome
            expand_around_center(i, i + 1)  # Even-length palindrome

        return s[start:start + max_length]


if __name__ == '__main__':
    solution = Solution()

    # Test case 1: "bab" or "aba"
    s = "babad"
    print(f"Longest Palindrome: {solution.longestPalindrome(s)}")