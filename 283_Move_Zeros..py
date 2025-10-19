"""
Question =>283:

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pos=0
        for i in range(n):
            if nums[i]!=0:
                nums[pos]=nums[i]
                pos+= 1
        for i in range(pos,n):
            nums[i]=0
        return nums
