'''
Given a non-empty integer array,
find the minimum number of moves required to make all array elements equal,
where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
'''


class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        median = nums[len(nums) // 2]
        print(median)
        return sum([abs(n - median) for n in nums])


s = Solution()

nums = [1, 0, 0, 8, 6, 9]

print(s.minMoves2(nums))

