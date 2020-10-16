# Problem 44 - WildCard Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)
        # List comprehension Method
        dp = [[False for i in range(pl+1)] for j in range(sl+1)]
        s = " "+s
        p = " "+p
        dp[0][0]=True
        for i in range(1,pl+1):
            # Check for * symbol
            if p[i] == '*':
                dp[0][i] = dp[0][i-1]
        for i in range(1,sl+1):
            for j in range(1,pl+1):
                # Check for ? symbol
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j]=='*':
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[sl][pl]
