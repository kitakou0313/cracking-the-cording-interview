import unittest


def calculate_coins(value: int, coin: list) -> int:
    """
    与えられたコインでの支払い方の総数を返す
    """
    pass


class Test(unittest.TestCase):
    def test1(self):
        testCases = [
            (1, 1),
            (4, 1),
            (5, 2),
            (15, 6),
            (20, 9)
        ]

        coins = [
            1, 5, 10, 25
        ]

        for value, expected in testCases:
            res = calculate_coins(value, coins)
            print(res)
            self.assertEqual(len(res), expected)


if __name__ == "__main__":
    unittest.main()
