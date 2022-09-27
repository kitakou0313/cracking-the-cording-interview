import unittest
from libs.tree import BinTreeNode, cal_bin_tree_height


def create_minimal_height_bin_tree(vals_list: list) -> BinTreeNode:
    """
    与えられた要素を用いて高さが最小の二分探索木を生成
    vals_listはすべてソート済みのため、半分に分割して二分木にしていく
    """
    if len(vals_list) == 0:
        return None

    middle_ind = len(vals_list)//2

    left_tree_vals = vals_list[:middle_ind]
    right_tree_vals = vals_list[middle_ind+1:]

    root_node: BinTreeNode = BinTreeNode(vals_list[middle_ind])

    root_node.set_left_node(create_minimal_height_bin_tree(left_tree_vals))
    root_node.set_right_node(create_minimal_height_bin_tree(right_tree_vals))

    return root_node


class Test(unittest.TestCase):

    def test1(self):
        test_case = [
            ([1, 2, 3], 2),
            ([1, 2], 2),
            ([1, 2, 3, 4], 3),
            ([1, 2, 3, 4, 5], 3)
        ]

        for input_case, expected in test_case:
            root_node = create_minimal_height_bin_tree(input_case)
            self.assertEqual(cal_bin_tree_height(root_node), expected)


if __name__ == "__main__":
    unittest.main()
