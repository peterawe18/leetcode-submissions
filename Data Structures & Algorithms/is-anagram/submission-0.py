class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st = {}
        tt = {}
        for i in s:
            if i in st:
                st[i]+=1
            else:
                st[i]=1
        for i in t:
            if i in tt:
                tt[i]+=1
            else:
                tt[i]=1

        return st == tt
        