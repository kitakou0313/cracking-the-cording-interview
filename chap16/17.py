import unittest


def search_max_sum_interval(array: list[int]) -> int:
    """
    docstring
    """
    max_sum = -float("inf")

    interval_start_ind = 0
    interval_end_ind = 0
    interval_val_sum = 0

    while interval_start_ind < len(array):
        print(interval_start_ind, interval_end_ind)
        while interval_end_ind < len(array):
            interval_val_sum += array[interval_end_ind]
            max_sum = max(max_sum, interval_val_sum)

            if interval_val_sum <= 0:
                break

            interval_end_ind += 1

        while (interval_val_sum <= 0) and (interval_start_ind <= interval_end_ind):
            interval_val_sum -= array[interval_start_ind]
            max_sum = max(max_sum, interval_val_sum)

            if interval_start_ind == interval_end_ind:
                interval_val_sum += 0
                interval_start_ind = interval_end_ind+1
                interval_end_ind = interval_start_ind

            interval_start_ind += 1

    return max_sum


class Test(unittest.TestCase):
    def test_1(self):
        test_cases = [
            ([2, -8, 3, -2, 4, -10], 5)
        ]

        for array, expected in test_cases:
            self.assertEqual(search_max_sum_interval(array), expected)


if __name__ == "__main__":
    unittest.main()
