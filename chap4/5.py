from logging import root
import unittest
from libs.tree import BinTreeNode


class SearchRes(object):
    """
    BSTの探索結果
    """

    def __init__(self, is_bst, min_val, max_val):
        """
        docstring
        """
        self.is_bst = is_bst
        self.min_val = min_val
        self.max_val = max_val


def is_BST_helper(root_node: BinTreeNode) -> SearchRes:
    """
    is_bstのhelper関数
    """
    is_having_left_tree = not(root_node.get_left_node() is None)
    is_having_right_tree = not(root_node.get_right_node() is None)

    search_res_left_tree = is_BST_helper(root_node.get_left_node()) if is_having_left_tree else SearchRes(
        is_bst=True, min_val=float("inf"), max_val=-float("inf")
    )
    search_res_right_tree = is_BST_helper(root_node.get_right_node()) if is_having_right_tree else SearchRes(
        is_bst=True, min_val=float("inf"), max_val=-float("inf")
    )

    bst_check_res = (search_res_left_tree.is_bst and search_res_right_tree.is_bst) and (
        search_res_left_tree.max_val < root_node.get_val(
        ) and root_node.get_val() <= search_res_right_tree.min_val
    )

    return SearchRes(
        max_val=max(root_node.get_val(), search_res_right_tree.max_val),
        min_val=min(root_node.get_val(), search_res_left_tree.min_val),
        is_bst=bst_check_res
    )


def is_BST(root_node: BinTreeNode) -> bool:
    """
    二分探索木か判定
    再帰的に実装する
    """
    return is_BST_helper(root_node).is_bst


class Test(unittest.TestCase):
    def test1(self):
        """
        単体テスト
        """
        bst = BinTreeNode(val=5)
        bst.set_left_node(
            BinTreeNode(1)
        )
        bst.set_right_node(
            BinTreeNode(10)
        )

        self.assertEqual(is_BST(bst), True)

        not_bst_1 = BinTreeNode(val=5)
        not_bst_1.set_left_node(
            BinTreeNode(6)
        )
        not_bst_1.set_right_node(
            BinTreeNode(10)
        )
        self.assertEqual(is_BST(not_bst_1), False)

        not_bst_2 = BinTreeNode(val=5)
        not_bst_2.set_left_node(
            BinTreeNode(1)
        )
        not_bst_2.set_right_node(
            BinTreeNode(4)
        )
        self.assertEqual(is_BST(not_bst_2), False)

        Bst = BinTreeNode(val=5)
        Bst.set_left_node(
            BinTreeNode(1)
        )
        self.assertEqual(is_BST(Bst), True)

        not_bst_2 = BinTreeNode(val=5)
        not_bst_2.set_left_node(
            BinTreeNode(10)
        )
        self.assertEqual(is_BST(not_bst_2), False)

        not_bst_3 = BinTreeNode(10)

        not_bst_3.set_left_node(BinTreeNode(1))

        not_bst_3.set_right_node(BinTreeNode(50))
        not_bst_3.get_right_node().set_left_node(BinTreeNode(60))
        not_bst_3.get_right_node().set_left_node(BinTreeNode(70))

        self.assertEqual(is_BST(not_bst_3), False)


if __name__ == "__main__":
    unittest.main()
