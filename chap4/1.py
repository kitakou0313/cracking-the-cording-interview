import unittest


def is_having_path_A_to_B(graph: dict, A: str, B: str) -> bool:
    """
    有向グラフでA->Bのパスの有無を探索
    幅探索でやる
    """
    pass


class Test(unittest.TestCase):
    def test1(self):
        graph = {
            "1": ["2"],
            "2": ["3", "4"],
            "3": [],
            "4": ["5"],
            "5": ["6"],
            "6": ["4"]
        }

        testCases = [
            (("1", "2"), True),
            (("1", "3"), True),
            (("2", "5"), True),
            (("4", "6"), True),
            (("3", "4"), False),
            (("3", "6"), False)
        ]

        for testInput, expected in testCases:
            self.assertEqual(is_having_path_A_to_B(
                graph, testInput[0], testInput[1]), expected)


if __name__ == "__main__":
    unittest.main()
