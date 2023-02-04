import unittest


def search_trg_num_in_rotated_array(array: list[int], trg_num: int):
    """
    昇順sort後に回転された配列からtrg_numを探索、indexを返す
    """
    head_num, tail_num = array[0], array[-1]

    trg_num_ind = -1
    if head_num > tail_num:
        # 回転済みのケース
        # 二つのソート済み配列にできる
        # O(n) + O(logn)
        pass
    else:
        # 回転されてないケース
        # 2分探索でOK
        # O(logn)
        pass

    return trg_num_ind


class Test(unittest.TestCase):
    """
    docstring
    """

    def test_1(self):
        """
        test
        """
        array = [55, 60, 65, 70, 75, 80, 85,
                 90, 95, 15, 20, 25, 30, 35, 40, 45]
        test_cases = [
            (55, 0), (60, 1), (90, 7), (95, 8), (15, 9), (30, 12), (45, 15)
        ]

        for trg_num, ans in test_cases:
            self.assertEqual(search_trg_num_in_rotated_array(
                array=array, trg_num=trg_num), ans)


if __name__ == "__main__":
    unittest.main()
