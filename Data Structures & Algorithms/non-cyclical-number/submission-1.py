class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(num):
            res = 0
            for d in str(num):
                res += int(d) ** 2
            return res
        
        seen = set()

        while n not in seen:
            seen.add(n)
            n = helper(n)
            if n == 1:
                return True
        return False

            
        