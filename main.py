# given an integer, return its binary representation

def countBits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)  # dp for dynamic programming
    offset = 1  # keep track of current highest power of 2

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp
