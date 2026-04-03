class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        i=0
        brox=[]
        j=len(height)-1
        while i!=j and i<j:
            area=min(height[i],height[j])*(j-i)
            brox.append(area)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max(brox)