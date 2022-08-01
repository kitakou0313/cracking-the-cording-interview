import unittest


def is_permutation(string_1: str, string_2: str) -> bool:
    """
    二つのstringが並び替えか判定
    時間計算量 O(n_1*log(n_1) + n_2*log(n_2))
    """
    sorted_string_1 = sorted(string_1)
    sorted_string_2 = sorted(string_2)

    return sorted_string_1 == sorted_string_2


def is_permutation_without_sort(string_1: str, string_2: str) -> bool:
    """
    sort無しで判定
    時間計算量 O(n_1 + n_2)
    空間計算量 O(n_1)
    """
    if len(string_1) != len(string_2):
        return False

    num_char_appearing_in_string_1 = dict()
    for char in string_1:
        if char not in num_char_appearing_in_string_1:
            num_char_appearing_in_string_1[char] = 0
        num_char_appearing_in_string_1[char] += 1

    for char in string_2:
        if char not in num_char_appearing_in_string_1:
            return False
        num_char_appearing_in_string_1[char] += -1

    for char, num in num_char_appearing_in_string_1.items():
        if num != 0:
            return False

    return True


class Test(unittest.TestCase):
    def test_is_permutation(self):
        self.assertEqual(is_permutation("abc", "cab"), True)
        self.assertEqual(is_permutation("abc", "def"), False)
        self.assertEqual(is_permutation("", "abc"), False)

    def test_is_permutation_without_sort(self):
        self.assertEqual(is_permutation_without_sort("abc", "cab"), True)
        self.assertEqual(is_permutation_without_sort("abc", "def"), False)
        self.assertEqual(is_permutation_without_sort(
            "aabbcc", "aaabcc"), False)
        self.assertEqual(is_permutation_without_sort("", "abc"), False)


if __name__ == "__main__":
    unittest.main()
