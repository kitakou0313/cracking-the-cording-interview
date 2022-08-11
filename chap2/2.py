import unittest
from libs.linked_list import SingleLinkedList


def get_Kth_node_value_from_tail(linked_list: SingleLinkedList, k: int):
    """
    末尾からk番目のnodeのvalを返す
    """
    length = len(linked_list.get_vals())
    index = length - k

    trg_node = linked_list.head
    for i in range(index):
        trg_node = trg_node.nxt
    return trg_node.val


class Test(unittest.TestCase):
    testCases = (
        ([10, 20, 30, 40, 50], 1, 50),
        ([10, 20, 30, 40, 50], 5, 10),
    )

    def test1(self, ):
        """
        test
        """
        for listVals, k, expected in self.testCases:
            lList = SingleLinkedList(list(listVals))

            self.assertEqual(lList.get_vals(), listVals)
            self.assertEqual(get_Kth_node_value_from_tail(lList, k), expected)


if __name__ == "__main__":
    unittest.main()
