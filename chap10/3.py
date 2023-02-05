import unittest
import bisect


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
        trg_num_ind = bisect.bisect_left(array, trg_num)
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
        not_rotated_array = sorted(array)
        test_cases = [
            55, 60, 90, 95, 15, 30, 45
        ]

        for trg_num in test_cases:
            # self.assertEqual(search_trg_num_in_rotated_array(
            #     array=array, trg_num=trg_num), array.index(trg_num))
            self.assertEqual(search_trg_num_in_rotated_array(
                array=not_rotated_array, trg_num=trg_num
            ), not_rotated_array.index(trg_num))


if __name__ == "__main__":
    unittest.main()
