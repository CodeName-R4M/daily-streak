class Solution:
    def compress(self, chars: List[str]) -> int:
        temb=""
        counter=1
        finale=""
        ol_temb=chars[0]
        for i in chars[1:]:
            temb=i
            if(temb==ol_temb):
                counter+=1
                continue
            else:
                finale += ol_temb
                if counter > 1:
                    finale += str(counter)
                ol_temb = i
                counter = 1  

        finale+=ol_temb
        if counter>1:
            finale+=str(counter)
        for i in range(len(finale)):
            chars[i] = finale[i]
        return len(finale)
            