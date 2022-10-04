from operator import index
import unittest


def convert_bit_to_indices(bit_int: int) -> set:
    """
    入力された整数をビットに変換
    """
    res = set([])

    index = 0
    while bit_int != 0:
        if bit_int & 1 == 1:
            res.add(index)

        bit_int = bit_int >> 1
        index += 1

    return res


def generate_all_subset(array: list) -> list:
    """
    入力の要素の部分集合を全列挙
    """
    number_of_element = len(array)

    res_set = set([])

    for bit_int in range(0, 2 ** number_of_element):
        indices = convert_bit_to_indices(bit_int)

        subset = []
        for index in indices:
            subset.append(array[index])

        subset = tuple(subset)
        res_set.add(subset)

    return res_set


class Test(unittest.TestCase):
    def test1(self):

        test_cases = [
            ([1, 2, 3], {(), (1,), (2,), (3,),
             (1, 2), (2, 3), (1, 3), (1, 2, 3)}),
            ([1, 2], {(), (1,), (2,), (1, 2)})
        ]

        for test_input, expected in test_cases:
            self.assertEqual(generate_all_subset(test_input), expected)


if __name__ == "__main__":
    unittest.main()
