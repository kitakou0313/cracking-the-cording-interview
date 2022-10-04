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


def find_magic_index_with_bin_search(array: list) -> int:
    """
    indexと値が等しいインデックスを返す
    二分探索する
    O(log(len(array)))
    """
    def is_ok(ind, val):
        """
        ind <= valか検証
        """
        return ind <= val

    # ind <= valが成立する最小のindを探索し、それがind == valか検証
    ng = -1
    ok = len(array)

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, array[mid]):
            ok = mid
        else:
            ng = mid

    return ok if array[ok] == ok else NOT_FOUND


class Test(unittest.TestCase):
    test_case = [
        ([-11, 0, 2, 6, 7, 10], 2),
        ([-11, -10, -9, 10, 11], NOT_FOUND)
    ]

    def test1(self):
        for input_case, excepted in self.test_case:
            self.assertEqual(find_magic_index(input_case), excepted)

    def test2(self):
        test_case = [
            ([-11, 0, 2, 6, 7, 10], 2),
            ([-11, -10, -9, 10, 11], NOT_FOUND)
        ]
        for input_case, excepted in self.test_case:
            self.assertEqual(
                find_magic_index_with_bin_search(input_case), excepted)


if __name__ == "__main__":
    unittest.main()
