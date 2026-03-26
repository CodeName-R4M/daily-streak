class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        valids=0
        skip=0
        for i in range(len(flowerbed)):
            if skip==1:
                skip=0
                continue
            if flowerbed[i]==0:
                if(len(flowerbed)==1):
                    valids+=1
                    break
                if(i==0):
                    if(flowerbed[i+1]==0):
                        valids+=1
                        skip=1
                        continue
                elif i==(len(flowerbed)-1):
                    if (flowerbed[i-1]==0):
                        valids+=1
                        continue
                    else:
                        continue
                if(flowerbed[i-1]==0 and flowerbed[i+1]==0):
                    valids+=1
                    skip=1
            
        if(valids>=n):
            return True
        else:
            return False
            
        