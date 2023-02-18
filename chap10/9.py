import unittest
import bisect


def search_trgnum_pos_in_sorted_matrix(matrix: list[list[int]], trg_num: int) -> tuple[int]:
    """
    docstring
    """
    C = len(matrix[0])
    R = len(matrix)

    for r in range(R):
        if not (matrix[r][0] <= trg_num and trg_num <= matrix[r][-1]):
            continue
        trg_num_col = bisect.bisect_left(matrix[r], trg_num)
        if matrix[r][trg_num_col] != trg_num:
            continue
        return (r, trg_num_col)


class Test(unittest.TestCase):
    def test_searchPosOfNumInSortedMatrix(self):
        mat = [[1,   2,  3,  4,  5,  6,  7,  8,  9],
               [5,  10, 15, 20, 25, 30, 35, 40, 45],
               [10, 20, 30, 40, 50, 60, 70, 80, 90],
               [13, 23, 33, 43, 53, 63, 73, 83, 93],
               [14, 24, 34, 44, 54, 64, 74, 84, 94],
               [15, 25, 35, 45, 55, 65, 75, 85, 95],
               [16, 26, 36, 46, 56, 66, 77, 88, 99]]
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 10), (1, 1))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 13), (3, 0))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 14), (4, 0))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 16), (6, 0))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 56), (6, 4))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 65), (5, 5))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 74), (4, 6))
        self.assertEqual(search_trgnum_pos_in_sorted_matrix(mat, 99), (6, 8))


if __name__ == "__main__":
    unittest.main()
