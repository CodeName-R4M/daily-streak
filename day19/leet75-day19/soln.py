class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=sum(nums[1:])
        for i in range(len(nums)):
            if right==left:
                return i
            left+=nums[i]
            if i + 1 < len(nums):
                right -= nums[i + 1]
        return -1            