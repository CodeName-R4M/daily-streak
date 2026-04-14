class Solution:
    
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        largest=0
        i=0
        shift=0
        finished=0
        dis1=list(set(nums1))
        dis2=list(set(nums2))
        if len(dis1)>len(dis2):
            largest=dis1
        else:
            largest=dis2
            
        while finished==0:
            if i<len(dis1) and dis1[i] in nums2:
                dis1.remove(dis1[i])
                shift=1
            if i<len(dis2) and dis2[i] in nums1:
                dis2.remove(dis2[i])
                shift=1
            if shift==1:
                if i>0:
                    i-=1
            else:
                i+=1
            shift=0
            if i>=len(dis1) and i>=len(dis2):
                finished=1
        result=[dis1,dis2]
        return result