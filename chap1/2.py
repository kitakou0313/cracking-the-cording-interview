import unittest


def is_permutation(string_1: str, string_2: str) -> bool:
    """
    二つのstringが並び替えか判定
    """
    sorted_string_1 = sorted(string_1)
    sorted_string_2 = sorted(string_2)

    return sorted_string_1 == sorted_string_2


class Test(unittest.TestCase):
    def test_is_permutation(self):
        self.assertEqual(is_permutation("abc", "cab"), True)
        self.assertEqual(is_permutation("abc", "def"), False)
        self.assertEqual(is_permutation("", "abc"), False)


if __name__ == "__main__":
    unittest.main()
