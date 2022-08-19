import unittest


class IntQueue(object):
    """
    int用のQueue
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.data: list = []

    def add(self, val: int):
        """
        追加
        """
        self.data.append(val)

    def pop(self) -> int:
        """
        要素をFIFOで出す
        """
        return self.data.pop(0)

    def is_empty(self) -> bool:
        """
        空か判定
        """
        return len(self.data) == 0


class QueueTest(unittest.TestCase):
    """
    Queueのテスト
    """

    def test_add_pop(self):
        """
        addとpopのテスト
        """
        vals = [1, 2, 3, 4, 10]
        q = IntQueue()

        for val in vals:
            q.add(val)

        pop_outputs = []
        while not(q.is_empty()):
            pop_outputs.append(q.pop())

        self.assertEqual(vals, pop_outputs)


if __name__ == "__main__":
    unittest.main()
