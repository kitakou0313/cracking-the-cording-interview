import unittest


def is_string_rotation(ori_string: str, trg_string: str) -> bool:
    """
    trg_stringがori_stringの回転か調べる
    """
    if len(ori_string) != len(trg_string):
        return False

    return ori_string in (trg_string + trg_string)


class Test(unittest.TestCase):
    testCases = [
        (("waterbottle", "erbottlewat"), True),
        (("foo", "bar"), False),
        (("foo", "foofoo"), False),
    ]

    def test(self):
        for test, expected in self.testCases:
            assert is_string_rotation(*test) == expected


if __name__ == "__main__":
    unittest.main()
