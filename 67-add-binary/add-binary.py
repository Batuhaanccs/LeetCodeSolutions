class Solution:
    def addBinary(self, a: str, b: str) -> str:
        c = 0
        p = 0
        for i in range(len(a)-1,-1,-1):
            if a[i]=="1":
                c += 2**p
            p+=1

        p = 0
        for i in range(len(b)-1,-1,-1):
            if b[i]=="1":
                c += 2**p
            p+=1

        if c == 0:
            return "0"
        
        res = ""
        while c > 0:
            res = str(c%2) + res
            c //=2
        return res