import unittest


def is_specific(string: str):
    """
    stringに重複する文字が無いか判定
    """
    appeared_chars = set([])

    for char in string:
        if char in appeared_chars:
            return False

        appeared_chars.add(char)

    return True


class Test(unittest.TestCase):
    """
    test class
    """

    def test_is_specific(self):
        """
        is_specificのtest
        """
        self.assertEqual(is_specific("abcdefg"), True)
        self.assertEqual(is_specific("aaaaaa"), False)
        self.assertEqual(is_specific(""), True)


if __name__ == "__main__":
    unittest.main()
