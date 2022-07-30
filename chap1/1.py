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


def is_specific_without_other_space(string: str):
    """
    stringに重複する文字が無いか判定
    追加メモリ無し
    """
    sorted_string = sorted(string)

    for ind in range(len(sorted_string) - 1):
        if (sorted_string[ind] == sorted_string[ind + 1]):
            return False

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

    def test_is_specific_without_other_space(self):
        """
        is_specific_without_other_spaceのtest
        """
        self.assertEqual(is_specific_without_other_space("abcdefg"), True)
        self.assertEqual(is_specific_without_other_space("aaaaaa"), False)
        self.assertEqual(is_specific_without_other_space(""), True)


if __name__ == "__main__":
    unittest.main()
