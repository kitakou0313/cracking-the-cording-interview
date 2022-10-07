from copy import deepcopy
import unittest


def fill_map_with_color(ori_map: list, pos: tuple, color: int) -> list:
    """
    指定したposのpixelをcolorの色に変更
    同じ色で囲まれた範囲を塗りつぶし
    """

    colored_map = deepcopy(ori_map)

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]

    return colored_map


class Test(unittest.TestCase):
    def test1(self):
        test_cases = [
            ([
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
            ], (2, 3), 1,
                [
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
                [0, 1, 1, 1, 1, 1, 0],
            ]
            )
        ]

        for [ori_map, pos, color, expected] in test_cases:
            self.assertEqual(fill_map_with_color(
                ori_map, pos, color), expected)


if __name__ == "__main__":
    unittest.main()
