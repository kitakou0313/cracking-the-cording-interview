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
    def search_highest_with_box(bottom_box: Box, boxes: list[Box], memo: dict[Box, int]) -> int:
        """
        docstring
        """
        pass

    memo: dict[Box, int] = {}

    max_height = -1
    for bottom_box in boxes:
        res = memo[bottom_box] if bottom_box in boxes else search_highest_with_box(
            bottom_box=bottom_box, boxes=boxes, memo=memo)
        memo[bottom_box] = res
        max_height = max(max_height, res)

    return max_height


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
