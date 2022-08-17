from cgitb import reset
import unittest


class IntStack():
    """
    int用stack
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.data: list = []

    def pop(self) -> int:
        """
        FILOで要素を出す
        """
        return self.data.pop()

    def add(self, val: int):
        """
        要素を追加
        """
        self.data.append(val)

    def __len__(self):
        """
        docstring
        """
        return len(self.data)

    def get_top(self) -> int:
        """
        頂点要素を返す
        """
        return self.data[-1]


class StackTest(unittest.TestCase):
    """
    Stackのテスト
    """

    def test_add(self):
        """
        追加のテスト
        """
        stack = IntStack()
        expected_res = []

        stack.add(1)
        expected_res.append(1)

        stack.add(2)
        expected_res.append(2)

        self.assertEqual(stack.data, expected_res)

    def test_pop(self):
        """
        popのテスト
        FILOで出てくるか
        popした要素は削除されているか
        """
        stack = IntStack()
        res = []
        expected_res = []

        stack.add(1)
        expected_res.append(1)

        stack.add(2)
        expected_res.append(2)

        expected_res.reverse()

        res.append(stack.pop())

        self.assertEqual(stack.data, [1])
        self.assertEqual(res[0], 2)


if __name__ == "__main__":
    unittest.main()
