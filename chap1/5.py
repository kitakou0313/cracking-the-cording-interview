import unittest


def is_one_step(string_1: str, string_2: str) -> bool:
    """
    挿入、削除、置き換えで二つの文字列を等しくできるか判定
    """
    if abs(len(string_1) - len(string_2)) > 1:
        return False

    # 長さが等しい時 -> 2文字異なっていたらfalse
    if len(string_1) == len(string_2):
        flag = False

        for ind, chars in enumerate(zip(string_1, string_2)):
            char_in_string_1, char_in_string_2 = chars
            if char_in_string_1 != char_in_string_2 and flag:
                return False
            elif char_in_string_1 != char_in_string_2 and not(flag):
                flag = True

    # 長さが異なる時 -> 足りないものを挿入する必要がある ので置き換えが必要になればfalse
    else:
        longer_string = string_1 if len(string_1) > len(string_2) else string_2
        shorter_string = string_2 if len(
            string_1) > len(string_2) else string_1

        ind_in_longer = 0
        ind_in_shorter = 0

        flag = False

        for i in range(len(shorter_string)):
            if longer_string[ind_in_longer] != shorter_string[ind_in_shorter] and flag:
                return False
            elif longer_string[ind_in_longer] != shorter_string[ind_in_shorter] and not(flag):
                ind_in_longer += 1
                flag = True

    return True


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_one_step("pale", "bake"), False)
        self.assertEqual(is_one_step("pale", "ple"), True)
        self.assertEqual(is_one_step("pales", "pale"), True)
        self.assertEqual(is_one_step("pale", "pales"), True)
        self.assertEqual(is_one_step("pale", "bale"), True)
        self.assertEqual(is_one_step("pale", "bake"), False)
        self.assertEqual(is_one_step("test", "te"), False)

        self.assertEqual(is_one_step("ale", "ela"), False)


if __name__ == "__main__":
    unittest.main()
