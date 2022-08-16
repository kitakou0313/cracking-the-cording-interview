import unittest
from libs.linked_list import SingleLinkedList


def sum_vals_expressed_by_linked_list(list_1: SingleLinkedList, list_2: SingleLinkedList) -> SingleLinkedList:
    """
    結合リストで表された二つの数をsum
    先頭が1のくらい
    """
    result_list = SingleLinkedList([])

    digit_node_list_1 = list_1.head
    digit_node_list_2 = list_2.head

    carry = 0
    while not(digit_node_list_1 is None and digit_node_list_2 is None):
        val_digit_list_1 = digit_node_list_1.val if digit_node_list_1 is not None else 0
        val_digit_list_2 = digit_node_list_2.val if digit_node_list_2 is not None else 0

        digit_val_sum = val_digit_list_1 + val_digit_list_2 + carry

        carry = 1 if digit_val_sum >= 10 else 0

        result_list.add(digit_val_sum % 10)

        digit_node_list_1 = digit_node_list_1.nxt if digit_node_list_1 is not None else None
        digit_node_list_2 = digit_node_list_2.nxt if digit_node_list_2 is not None else None

    if carry != 0:
        result_list.add(carry)

    return result_list


class Test(unittest.TestCase):
    testCases = (
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        ([3, 2, 6], [3, 2, 5], [6, 4, 1, 1]),
        ([0], [0], [0]),
        ([3, 2, 1], [3, 2, 1], [6, 4, 2]),
    )

    def test1(self, ):
        """
        test
        """
        for list1Values, list2Values, expected in self.testCases:
            list1 = SingleLinkedList(list1Values)
            list2 = SingleLinkedList(list2Values)

            self.assertEqual(list1.get_vals(), list1Values)
            self.assertEqual(list2.get_vals(), list2Values)

            res = sum_vals_expressed_by_linked_list(list1, list2)

            self.assertEqual(res.get_vals(), expected)


if __name__ == "__main__":
    unittest.main()
