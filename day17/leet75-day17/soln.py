class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        largest = 0
        current = 0
        befo = 0
        
        firsta = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                current += 1
            else:
                if firsta == 0:
                    befo = current  
                    current += 1    
                    firsta = 1
                else:
                    if current > largest:
                        largest = current
                    current = current - befo
                    befo = current - 1  

        if current > largest:
            largest = current

        return largest - 1