import unittest
from libs.tree import BinTreeNode, cal_bin_tree_height


def create_minimal_height_bin_tree(vals_list: list) -> BinTreeNode:
    """
    与えられた要素を用いて高さが最小の二分探索木を生成
    """
    pass


class Test(unittest.TestCase):

    def test1(self):
        test_case = [
            ([1, 2, 3], 2),
            ([1, 2], 2),
            ([1, 2, 3, 4], 3)
        ]

        for input_case, expected in test_case:
            root_node = create_minimal_height_bin_tree(input_case)
            self.assertEqual(cal_bin_tree_height(root_node), expected)


if __name__ == "__main__":
    unittest.main()
