import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        j=i+k
        curwin=sum(nums[:k])
        if len(nums)==1:
            return nums[0]
        larger = sum(nums[:k]) / k
        if len(nums)<j:
            return
        for j in range(i+k,len(nums)):
            curwin-=nums[i]
            curwin+=nums[j]
            current=curwin/k
            if(current>larger):
                larger=current
            i+=1
        return larger