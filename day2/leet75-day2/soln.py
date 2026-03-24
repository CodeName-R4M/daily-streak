class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n=0
        ugh=0
        gcd=""
        finalee=""
        sudo=0
        smol=min(len(str1),len(str2))
        large=max(len(str1),len(str2))
        smolest=min(str1,str2)
        largest=max(str1,str2)
        for i in range(1,smol+1):
            gcd=smolest[0:i]
            if smol % i == 0 and large % i == 0:
                sudo=smol//len(gcd)
                if(gcd*sudo==smolest):
                    ugh=large//len(gcd)
                    if(gcd*ugh==largest):
                        finalee=gcd
        if len(gcd)==0:
            return ""
        else:
            return finalee