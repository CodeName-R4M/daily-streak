class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest=0
        current=0
        now=[]
        for i in range(len(gain)):
            current+=gain[i]
            now.append(current)
            if largest<current:
                largest=current
        return largest