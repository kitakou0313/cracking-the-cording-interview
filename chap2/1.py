import unittest
from libs.linked_list import LinkedList


def remove_dup_node(linked_list: LinkedList):
    """
    valが重複しているnodeを削除
    """
    val_set = set([])

    for node in linked_list:
        if node.val in val_set:
            linked_list.remove_node(node)
            continue

        val_set.add(node.val)


class Test(unittest.TestCase):
    testCases = (
        ([], []),
        ([1, 1, 1, 1, 1, 1], [1]),
        ([1, 2, 3, 2], [1, 2, 3]),
        ([1, 2, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [1, 2, 3]),
    )

    def test1(self, ):
        """
        test
        """
        for test, expected in self.testCases:
            lList = LinkedList(test)
            self.assertEqual(lList.get_vals(), test)

            remove_dup_node(lList)

            self.assertEqual(lList.get_vals(), expected)


if __name__ == "__main__":
    unittest.main()
