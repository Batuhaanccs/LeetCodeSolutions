class Solution:
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        
        current = 0
        onePrev = 2
        twoPrev = 1
        for i in range(3,n+1):
            current = onePrev + twoPrev
            twoPrev = onePrev
            onePrev = current
        return current