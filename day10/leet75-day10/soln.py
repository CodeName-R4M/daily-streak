class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ind=0
        if 0 not in nums:
            return
        for i in range(len(nums)-1):
            ind=nums.index(0)
            nums.pop(ind)
            nums.insert(len(nums),0)