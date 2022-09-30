import unittest


def cal_num_of_ways_N(N: int) -> int:
    """
    0からN点までの経路数を出力
    ステップの大きさ1,2,3
    """
    dp = [0 for _ in range(0, N+1)]
    dp[0] = 1
    for n in range(0, N):
        if n+1 <= N:
            dp[n + 1] += dp[n]
        if n+2 <= N:
            dp[n + 2] += dp[n]
        if n+3 <= N:
            dp[n + 3] += dp[n]

    return dp[N]


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(cal_num_of_ways_N(3), 4)
        self.assertEqual(cal_num_of_ways_N(7), 44)


if __name__ == "__main__":
    unittest.main()
