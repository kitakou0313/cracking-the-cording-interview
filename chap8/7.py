import unittest
import itertools


def generate_all_permutation_of_string(origin_string) -> set:
    """
    入力文字列で作成できるすべての組み合わせを列挙（重複無し）
    """
    if len(origin_string) <= 1:
        return set([origin_string])

    res_set = set([])

    for ind, char in enumerate(origin_string):
        rest_string = origin_string[0:ind] + origin_string[ind + 1:]
        permutations_with_rest_string = generate_all_permutation_of_string(
            rest_string)
        for permutation in permutations_with_rest_string:
            res_set.add(char + permutation)

    return res_set


class Test(unittest.TestCase):
    def test1(self):
        test_cases = [
            "abc",
            "abcde",
            ""
        ]

        for test_input in test_cases:
            expected = set(["".join(v)
                           for v in itertools.permutations(test_input)])
            self.assertEqual(
                generate_all_permutation_of_string(test_input), expected)


if __name__ == "__main__":
    unittest.main()
