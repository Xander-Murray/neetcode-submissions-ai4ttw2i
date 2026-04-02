class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1

        for i in range(len(num) - 2): 
            if num[i] == num[i + 1] == num[i + 2]: # if the num is contiguous by 3
                res = max(res, int(num[i]))        # check if its the max so far
        return str(res) * 3 if res != -1 else ""
