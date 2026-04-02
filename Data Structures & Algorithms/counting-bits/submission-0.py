class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        def countOnes(num):
            cnt = 0
            while num:
                num &= num - 1
                cnt += 1
            return cnt
        for i in range(n + 1):
            output.append(countOnes(i))
        
        return output