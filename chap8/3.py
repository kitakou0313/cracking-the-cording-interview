from http.client import NO_CONTENT, NOT_FOUND
import unittest

NOT_FOUND = -1


def find_magic_index(array: list) -> int:
    """
    indexと値が等しいインデックスを返す
    """
    for ind, val in enumerate(array):
        if ind == val:
            return ind

    return NOT_FOUND


class Test(unittest.TestCase):
    def test1(self):
        test_case = [
            ([-11, 0, 2, 6, 7, 10], 2),
            ([-11, -10, -9, 10, 11], NOT_FOUND)
        ]
        for input_case, excepted in test_case:
            self.assertEqual(find_magic_index(input_case), excepted)


if __name__ == "__main__":
    unittest.main()
