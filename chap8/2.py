import unittest
from libs.queue import TupleQueue


def find_path(map: list) -> bool:
    """
    周囲4マスのみ遷移可能
    0が通行可能
    (0,0) -> (R-1, C-1)までの経路の有無を探索
    """
    R = len(map)
    C = len(map[0])

    dR = [0, 0, 1, -1]
    dC = [1, -1, 0, 0]

    q = TupleQueue()
    added_axis = set([])

    q.add((0, 0))
    added_axis.add((0, 0))

    while not(q.is_empty()):
        current_axis = q.pop()

        if current_axis[0] == R-1 and current_axis[1] == C-1:
            return True

        for dindex in range(len(dR)):
            nxt_r = current_axis[0] + dR[dindex]
            nxt_c = current_axis[1] + dC[dindex]

            if nxt_r < R and nxt_r >= 0 and nxt_c < C and nxt_c >= 0 and not((nxt_r, nxt_c) in added_axis) and map[nxt_r][nxt_c] == 0:
                q.add((nxt_r, nxt_c))
                added_axis.add((nxt_r, nxt_c))

    return False


class Test(unittest.TestCase):
    def test1(self):
        map1 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(find_path(map1), True)

        map2 = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(find_path(map2), False)


if __name__ == "__main__":
    unittest.main()
