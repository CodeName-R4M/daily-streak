class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = []
        d = []
        n = len(senate)
        for i in range(n):
            if senate[i] == "R":
                r.append(i)
            else:
                d.append(i)

        while r and d:
            if r[0] < d[0]:
                r.append(r[0] + n)
            else:
                d.append(d[0] + n)
            r.pop(0)
            d.pop(0)
        if r:
            return "Radiant"
        return "Dire"