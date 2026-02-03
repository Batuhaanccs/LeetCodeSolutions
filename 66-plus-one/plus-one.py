class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) -1
        intVal = 1
        newDigits=[]
        for val in digits:
            intVal += val*(10**i)
            i-=1
        for char in str(intVal):
            newDigits.append(int(char))
        return newDigits