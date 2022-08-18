from inspect import stack
import unittest
from libs.linked_list import SingleLinkedList
from libs.stack import IntStack


def is_kaibun_list(llist: SingleLinkedList):
    """
    単方向連結リストの要素が回文になっているか判定
    """
    stack = IntStack()

    list_length = len(llist)
    vals = llist.get_vals()

    if list_length % 2 == 0:
        for val in vals:
            if not(stack.is_empty()) and val == stack.get_top():
                stack.pop()
            else:
                stack.add(val)

        if not(stack.is_empty()):
            return False
    return True


class Test(unittest.TestCase):
    testCases = (
        # ([1], True),
        # ([2, 3, 5, 3, 2], True),
        # ([2, 2, 5, 2, 2], True),
        ([4, 1, 1, 4], True),
        ([5, 4, 3, 1], False),
        # ([5, 4, 1], False),
    )

    def test1(self, ):
        """
        test
        """
        for testInput, expected in self.testCases:
            lList = SingleLinkedList(testInput)
            self.assertEqual(lList.get_vals(), testInput)

            self.assertEqual(is_kaibun_list(lList), expected)


if __name__ == "__main__":
    unittest.main()
