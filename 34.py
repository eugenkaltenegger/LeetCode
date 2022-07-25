#!/usr/bin/env python3

# Problem description: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        split = int(len(nums) / 2)
        left_nums = nums[0: split]
        right_nums = nums[split: len(nums)]

        left_search = self.searchRange(left_nums, target)
        right_search = self.searchRange(right_nums, target)

        if left_search == [-1, -1] and right_search == [-1, -1]:
            return [-1, -1]

        if left_search == [-1, -1] and right_search != [-1, -1]:
            return split + right_search[0], split + right_search[1]

        if left_search != [-1, -1] and right_search == [-1, -1]:
            return left_search

        if left_search != [-1, -1] and right_search != [-1, -1]:
            return [left_search[0], split+right_search[1]]


if __name__ == "__main__":
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))  # [3, 4]
    # print(Solution().searchRange([0, 0, 1, 2, 3, 3, 4], 2))  # [3, 3]
