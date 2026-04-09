class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        io=0
        j=io+k
        window=s[:j]
        largest=0
        current=0
        for j in range(j,len(s)+1):
            window=s[io:j]
            a=window.count("a")
            e=window.count("e")
            i=window.count("i")
            o=window.count("o")
            u=window.count("u")
            current=a+e+i+o+u
            if current>largest:
                largest=current
                if largest==k:
                    break
            io+=1
        return largest