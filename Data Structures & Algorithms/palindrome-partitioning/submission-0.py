class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(idx, cur_path):
            if idx == len(s):
                res.append(cur_path.copy())
                return


            # otherwise need to do two checks
            # is the sub string a palindrome

            for j in range(idx,len(s)):
                substring = s[idx:j + 1]

                if palindrome(substring):
                    cur_path.append(substring)
                    backtrack(j + 1, cur_path)
                    cur_path.pop()


        def palindrome(a):
            l, r = 0, len(a) - 1
            while l <= r:
                if a[l] != a[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        backtrack(0, [])
        return res
        