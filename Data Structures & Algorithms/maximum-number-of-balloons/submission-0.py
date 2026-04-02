class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        count = {}

        for c in text:
            if c in 'balon':
                count[c] = count.get(c, 0) + 1

        if len(count) < 5:
            return 0

        
        count['l'] //= 2
        count['o'] //= 2

        return min(count.values())


            
        