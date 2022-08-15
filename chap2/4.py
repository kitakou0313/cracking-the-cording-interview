import unittest
from libs.linked_list import SingleLinkedList, LinkedListNode


def split_list_with_val(llist: SingleLinkedList, val: int):
    new_head = llist.head
    new_tail = llist.head
    current_node = llist.head

    while current_node is not None:
        next_node = current_node.nxt

        if current_node.val < val:
            current_node.nxt = new_head
            new_head = current_node
        else:
            new_tail.nxt = current_node
            new_tail = current_node

        current_node = next_node

    if new_tail.nxt is not None:
        new_tail.nxt = None

    llist.head = new_head
    llist.tail = new_tail


class Test(unittest.TestCase):
    testCases = (
        ([3, 5, 8, 5, 10, 2, 1], 5, [1, 2, 3, 5, 8, 5, 10]),
    )

    def test1(self, ):
        """
        test
        """
        for listVals, K, expected in self.testCases:
            lList = SingleLinkedList((listVals))

            self.assertEqual(lList.get_vals(), listVals)
            split_list_with_val(lList, K)
            self.assertEqual(lList.get_vals(), expected)


if __name__ == "__main__":
    unittest.main()
