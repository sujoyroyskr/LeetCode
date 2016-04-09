class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        left = 0 
        right = len(nums)-1
        while left < right:
            mid = (left+right)/2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        if nums[left] == target:
            return left
        elif nums[left] > target:
            return left
        elif nums[left] < target:
            return left + 1