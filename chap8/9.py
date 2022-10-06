import unittest


def generate_all_parens_pattern_memo(parens_pair_num: int, memo: dict) -> set:
    """
    docstring
    """
    prev_res = memo[parens_pair_num-1] if parens_pair_num-1 in memo else generate_all_parens_pattern_memo(
        parens_pair_num=parens_pair_num-1, memo=memo
    )

    res = set([])
    for parens_pattern in prev_res:
        res.add("(" + parens_pattern + ")")
        res.add(parens_pattern + "()")
        res.add("()" + parens_pattern)

    memo[parens_pair_num] = res
    return res


def generate_all_parens_pattern(parens_pair_num: int) -> set:
    """
    parensのペアで現れる文字列の組み合わせを生成
    """
    memo = dict()
    memo[1] = set(["()"])
    res = generate_all_parens_pattern_memo(parens_pair_num, memo)
    return res


class Test(unittest.TestCase):
    def test1(self):
        test_cases = [
            (2, set(["()()", "(())"])),
            (3, set(["((()))", "(()())", "(())()", "()(())", "()()()"])),
        ]

        for test_input, expected in test_cases:
            self.assertEqual(generate_all_parens_pattern(test_input), expected)


if __name__ == "__main__":
    unittest.main()
