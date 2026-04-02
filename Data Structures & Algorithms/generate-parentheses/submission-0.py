class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        # understand we are given N the number of valid nested parantheses combinations

        # use back tracking we can keep track of open and closed parenthesis
        # use stack for back tracking
        # can only start with open parenthesis
        # keep track of open and close
        # can only add close if closedN so far < openN


        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if int(openN) < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0,0)
        return res