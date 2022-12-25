import unittest


class Box(object):
    """
    箱クラス
    """

    def __init__(self, hi: int, wi: int, di: int):
        self.hi = hi
        self.wi = wi
        self.di = di


def search_highest_box_stacks(boxes: list[Box]) -> int:
    """
    docstring
    """
    pass


class Test(unittest.TestCase):
    """
    docstring
    """

    def test_1(self):
        """
        test
        """
        test_cases = [
            ([Box(4, 3, 2), Box(5, 4, 1)], 5),
            ([Box(3, 2, 1), Box(6, 5, 4)], 9),
            ([Box(100, 100, 100), Box(25, 25, 25),
             Box(20, 5, 30), Box(17, 4, 28)], 137)
        ]

        for boxes, height in test_cases:
            self.assertEqual(search_highest_box_stacks(boxes), height)


if __name__ == "__main__":
    unittest.main()
