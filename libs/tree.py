import unittest


class BinTreeNode(object):
    """
    二分木
    """

    def __init__(self, val: int):
        """
        docstring
        """
        self.val = val
        self.left_node: BinTreeNode = None
        self.right_node: BinTreeNode = None

    def get_val(self) -> int:
        """
        ノードの要素を返す
        """
        return self.val

    def get_left_node(self) -> 'BinTreeNode':
        """
        左の要素取得
        """
        return self.left_node

    def get_right_node(self) -> 'BinTreeNode':
        """
        右の要素取得
        """
        return self.right_node

    def set_left_node(self, node: 'BinTreeNode'):
        """
        左のノードをセット
        """
        self.left_node = node

    def set_right_node(self, node: 'BinTreeNode'):
        """
        右のノードをセット
        """
        self.right_node = node


class BinTreeTest(unittest.TestCase):
    """
    二分木のテスト
    """

    def test1(self):
        """
        二分木のテスト
        """
        vals = [1, 2, 3]

        root = BinTreeNode(vals[0])
        root.set_left_node(BinTreeNode(vals[1]))
        root.set_right_node(BinTreeNode(vals[2]))

        self.assertEqual(root.get_val(), vals[0])
        self.assertEqual(root.get_left_node().get_val(), vals[1])
        self.assertEqual(root.get_right_node().get_val(), vals[2])

        self.assertIsNone(root.get_left_node().get_left_node())
        self.assertIsNone(root.get_left_node().get_right_node())


if __name__ == "__main__":
    unittest.main()
