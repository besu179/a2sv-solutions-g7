class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            swaps = 0
            for j in range(n - i - 1):
                if nums[j] > nums[j + 1]:
                    swaps += 1
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if swaps == 0:
                return nums
        return nums