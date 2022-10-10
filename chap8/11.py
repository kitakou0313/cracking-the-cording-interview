import unittest


def helper_func(value: int, coins: list, memo: dict) -> int:
    """
    メモ化した関数
    """
    res = 0
    for coin in coins:
        trg_val = value - coin
        if trg_val < 0:
            continue
        res += memo[trg_val] if trg_val in memo else helper_func(
            trg_val, coins, memo)

    memo[value] = res
    return res


def calculate_coins(value: int, coins: list) -> int:
    """
    与えられたコインでの支払い方の総数を返す
    """
    memo = {}
    memo[0] = 1
    return helper_func(value, coins, memo)


class Test(unittest.TestCase):
    def test1(self):
        test_cases = [
            (1, 1),
            (4, 1),
            (5, 2),
            (15, 6),
            (20, 9)
        ]

        coins = [
            1, 5, 10, 25
        ]

        for value, expected in test_cases:
            res = calculate_coins(value, coins)
            self.assertEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
