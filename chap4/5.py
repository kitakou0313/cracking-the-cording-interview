import unittest
from libs.tree import BinTreeNode


def is_BST(root_node: BinTreeNode) -> bool:
    """
    二分探索木か判定
    再帰的に実装する
    """
    pass


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

        notBst1 = BinTreeNode(val=5)
        notBst1.set_left_node(
            BinTreeNode(6)
        )
        notBst1.set_right_node(
            BinTreeNode(10)
        )
        self.assertEqual(is_BST(notBst1), False)

        notBst = BinTreeNode(val=5)
        notBst.set_left_node(
            BinTreeNode(1)
        )
        notBst.set_right_node(
            BinTreeNode(4)
        )
        self.assertEqual(is_BST(notBst), False)

        Bst = BinTreeNode(val=5)
        Bst.set_left_node(
            BinTreeNode(1)
        )
        self.assertEqual(is_BST(Bst), True)

        notBst = BinTreeNode(val=5)
        notBst.set_left_node(
            BinTreeNode(10)
        )
        self.assertEqual(is_BST(notBst), False)


if __name__ == "__main__":
    unittest.main()
