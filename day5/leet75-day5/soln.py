class Solution:
    def reverseVowels(self, s: str) -> str:
        inde=[]
        vowe=[]
        for i in range(len(s)):
            if(s[i]=="A" or s[i]=="E" or s[i]=="I" or s[i]=="O" or s[i]=="U" or s[i]=="a" or s[i]=="e" or s[i]=="i" or s[i]=="o" or s[i]=="u"):
                inde.append(i)
                vowe.append(s[i])
        vowe=vowe[::-1]
        for j in range(len(inde)):
            s = s[:inde[j]] + vowe[j] + s[inde[j]+1:]
        return s