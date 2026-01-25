class Solution:
    def romanToInt(self, s: str) -> int:
        myDict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000}
        last = 1
        total = 0
        for i in s[::-1]:
            if myDict[i]<last:
                total -= myDict[i]
            else:
                total+= myDict[i]
            last = myDict[i]
        return total