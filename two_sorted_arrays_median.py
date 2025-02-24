"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = sorted(nums1 + nums2)
        merged_arr_len = len(merged_arr)
        merged_arr_center = merged_arr_len // 2

        if merged_arr_len % 2 == 0:
            return (merged_arr[merged_arr_center] + merged_arr[merged_arr_center - 1]) / 2
        else:
            return merged_arr[merged_arr_center]

if __name__ == "__main__":
    solution = Solution()

    # Test case: 1 [1,3], nums2 = [2]
    results = solution.findMedianSortedArrays([1,3], [2])
    print(f"The median of the 2 arrays is: {results}")

    # Test case: 2 [1,2], nums2 = [3,4]
    results = solution.findMedianSortedArrays([1,2], [3,4])
    print(f"The median of the 2 arrays is: {results}")