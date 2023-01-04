import unittest


def search_min_diff(list_a: list, list_b: list) -> int:
    """
    list_a, b内の要素の中で最も差が小さいもの間の差を返す
    """
    sorted_list_a = sorted(list_a)
    sorted_list_b = sorted(list_b)

    min_diff = abs(sorted_list_a[0] - sorted_list_b[0])

    end_ind_b = 0
    for ind_a, val_a in enumerate(sorted_list_a):
        lowest_diff_with_ind_a = float("inf")
        prefer_step_diff = float("inf")
        for ind_b in range(end_ind_b, len(sorted_list_b)):
            diff = abs(val_a - sorted_list_b[ind_b])

            if diff > prefer_step_diff:
                end_ind_b = ind_b-1
                break

            if diff <= lowest_diff_with_ind_a:
                lowest_diff_with_ind_a = diff

            prefer_step_diff = diff

        min_diff = min(min_diff, lowest_diff_with_ind_a)

    return min_diff


def search_min_diff_bad(list_a: list, list_b: list) -> int:
    """
    list_a, b内の要素の中で最も差が小さいもの間の差を返す
    O(N_a * N_b)
    """
    min_diff = float("inf")

    for val_in_a in list_a:
        for val_in_b in list_b:
            min_diff = min(min_diff, abs(val_in_a - val_in_b))

    return min_diff


class Test(unittest.TestCase):
    def test1(self):
        test_cases = [
            ([1, 3, 15, 11, 2], [23, 127, 235, 19, 8], 3)
        ]

        for listA, listB, expected in test_cases:
            self.assertEqual(search_min_diff_bad(listA, listB), expected)
            self.assertEqual(search_min_diff(listA, listB), expected)


if __name__ == "__main__":
    unittest.main()
