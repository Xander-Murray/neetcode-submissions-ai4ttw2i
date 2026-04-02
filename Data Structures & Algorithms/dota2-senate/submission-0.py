class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        s = list(senate)
        cnt = 0
        for senator in s:
            if senator == 'R':
                if cnt < 0:
                    s.append('D')
                cnt += 1
            else:
                if cnt > 0:
                    s.append('R')
                cnt -= 1
        return 'Radiant' if cnt > 0 else 'Dire'
        
        