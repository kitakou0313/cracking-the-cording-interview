import queue
import unittest
from libs.queue import IntQueue


def is_having_path_A_to_B(graph: dict, A: int, B: int) -> bool:
    """
    有向グラフでA->Bのパスの有無を探索
    幅探索でやる
    """
    queue = IntQueue()
    added_nodes = set([])

    queue.add(A)
    added_nodes.add(A)

    while not(queue.is_empty()):
        node = queue.pop()

        if node == B:
            return True

        for connected_node in graph[node]:
            if connected_node in added_nodes:
                continue
            queue.add(connected_node)
            added_nodes.add(connected_node)

    return False


class Test(unittest.TestCase):
    def test1(self):
        graph = {
            1: [2],
            2: [3, 4],
            3: [],
            4: [5],
            5: [6],
            6: [4]
        }

        testCases = [
            ((1, 2), True),
            ((1, 3), True),
            ((2, 5), True),
            ((4, 6), True),
            ((3, 4), False),
            ((3, 6), False)
        ]

        for testInput, expected in testCases:
            self.assertEqual(is_having_path_A_to_B(
                graph, testInput[0], testInput[1]), expected)


if __name__ == "__main__":
    unittest.main()
