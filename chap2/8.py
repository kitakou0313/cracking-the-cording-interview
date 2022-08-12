import unittest
from libs.linked_list import LinkedList


def is_having_loop(l_list: LinkedList):
    """
    与えられたリストのループ検出
    """
    fast_runner = l_list.head.nxt.nxt
    slow_runner = l_list.head

    while not(fast_runner is None or slow_runner is None):
        if fast_runner == slow_runner:
            return True

        if fast_runner.nxt is None:
            return False
        fast_runner = fast_runner.nxt.nxt
        slow_runner = slow_runner.nxt

    return False


class Test(unittest.TestCase):
    def test1(self, ):
        """
        test
        """
        testCases = (
            (True, True),
            (False, False)
        )
        for isLoop, expected in testCases:
            ll = LinkedList([1, 2, 3, 4, 5])

            if isLoop:
                ll.tail.nxt = ll.head

            self.assertEqual(is_having_loop(ll), expected)


if __name__ == "__main__":
    unittest.main()
