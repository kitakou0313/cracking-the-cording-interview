from libs.linked_list import SingleLinkedList, LinkedListNode
import unittest


def remove_node(lList: SingleLinkedList, node: LinkedListNode):
    """
    与えられたリストのNodeを削除
    """
    # 末尾の削除の場合
    if node.nxt is None:
        current_node = lList.head
        while current_node.nxt != node:
            current_node = current_node.nxt

        current_node.nxt = None

    else:
        node.val = node.nxt.val
        node.nxt = node.nxt.nxt


class Test(unittest.TestCase):
    testCases = (
        ([10, 20, 30, 40, 50], 2, [10, 20, 40, 50]),
        ([10, 20, 30, 40, 50], 4, [10, 20, 30, 40]),
    )

    def test1(self, ):
        """
        test
        """
        for list_vals, node_val_ind, expected in self.testCases:
            lList = SingleLinkedList((list_vals[:node_val_ind]))

            lList.add(list_vals[node_val_ind])
            middle_node = lList.tail

            lList.add_multi_node(list_vals[node_val_ind+1:])

            self.assertEqual(lList.get_vals(), list_vals)
            remove_node(lList, middle_node)
            self.assertEqual(lList.get_vals(), expected)


if __name__ == "__main__":
    unittest.main()
