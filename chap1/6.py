import unittest


def compression_string(string: str) -> str:
    """
    入力文字列を圧縮、圧縮後と圧縮前で短い方を返す
    圧縮ルールは文字種+繰り返し回数
    """
    compressed_string = ""
    start_ind = 0

    # 一ループが一文字種の圧縮に対応
    while start_ind < len(string):
        end_ind = start_ind
        char_count = 0
        while end_ind < len(string) and string[start_ind] == string[end_ind]:
            end_ind += 1
            char_count += 1

        compressed_string += string[start_ind] + str(char_count)

        start_ind = end_ind

    return compressed_string if len(compressed_string) < len(string) else string


class Test(unittest.TestCase):
    testCases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    def test_string_compression(self):
        for testString, expected in self.testCases:
            assert compression_string(testString) == expected


if __name__ == "__main__":
    unittest.main()
