class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lastr=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                lastr.append(True)
            else:
                lastr.append(False)
        return lastr