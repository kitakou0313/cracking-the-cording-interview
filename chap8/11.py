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


def helper_func_without_memo(value: int, coins: list) -> set[tuple]:
    """
    メモ化した関数
    """
    res: set[tuple] = set([])

    for coin_id, coin_val in enumerate(coins):
        lasted_value = value - coin_val

        if lasted_value < 0:
            continue

        res_with_lasted_values = helper_func_without_memo(
            lasted_value, coins) if lasted_value != 0 else set([tuple([0 for _ in range(len(coins))])])

        for payment_way in res_with_lasted_values:
            tmp = list(payment_way)
            tmp[coin_id] += 1
            res.add(tuple(tmp))

    return res


def calculate_coins(value: int, coins: list) -> int:
    """
    与えられたコインでの支払い方の総数を返す
    """
    memo = {}
    # memo[0] = 1
    # return helper_func(value, coins, memo)
    return len(helper_func_without_memo(value, coins))


class Test(unittest.TestCase):
    def test_1(self):
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
