import unittest


def replace_zero(matrix: list) -> list:
    """
    0が存在する行、列を0で埋める
    """
    rows = set([])
    cols = set([])

    row_num = len(matrix)
    col_num = len(matrix[0])

    for row in range(row_num):
        for col in range(col_num):
            if matrix[row][col] == 0:
                rows.add(row)
                cols.add(col)

    for row_to_be_replaced in range(row_num):
        for col in range(col_num):
            matrix[row_to_be_replaced][col] = 0

    for col_to_be_replaced in range(col_num):
        for row in range(row_num):
            matrix[row][col_to_be_replaced] = 0

    return matrix


class Test(unittest.TestCase):
    testCases = [
        (
            [
                [1, 2, 3, 4, 0],
                [6, 0, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 0, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [11, 0, 13, 14, 0],
                [0, 0, 0, 0, 0],
                [21, 0, 23, 24, 0],
            ],
        )
    ]

    def test_replace_zero(self):
        for test, expected in self.testCases:
            assert replace_zero(test) == expected


if __name__ == "__main__":
    unittest.main()
