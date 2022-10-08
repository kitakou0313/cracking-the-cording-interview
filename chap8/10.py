from copy import deepcopy
import unittest
from libs.queue import TupleQueue


def fill_map_with_color(ori_map: list, pos: tuple, color: int) -> list:
    """
    指定したposのpixelをcolorの色に変更
    同じ色で囲まれた範囲を塗りつぶし
    """

    colored_map = deepcopy(ori_map)

    R = len(ori_map)
    C = len(ori_map[0])

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    q = TupleQueue()
    poses_added_to_queue = set([])

    q.add(pos)
    poses_added_to_queue.add(pos)

    while not (q.is_empty()):
        current_r, current_c = q.pop()
        colored_map[current_r][current_c] = 1

        for d_ind in range(len(dr)):
            nxt_r = current_r + dr[d_ind]
            nxt_c = current_c + dc[d_ind]
            nxt_pos = (nxt_r, nxt_c)

            if not (0 <= nxt_r and nxt_r < R and 0 <= nxt_c and nxt_c < C):
                continue
            if ori_map[nxt_r][nxt_c] == color:
                continue
            if nxt_pos in poses_added_to_queue:
                continue

            q.add(nxt_pos)
            poses_added_to_queue.add(nxt_pos)

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
