# encoding:utf-8
# 要使任何S(i>=left, j<=right) >= S(left,right)，由于j-i <= right-left
# 必然要有min(ai,aj)>=min(a(left),a(right))才行

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max = 0
        while left < right:
            current = (right - left)* min(height[left],height[right])
            if current >max:
                max = current
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return max
