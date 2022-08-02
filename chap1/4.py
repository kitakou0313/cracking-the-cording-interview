import unittest


def is_permutation_of_palindrome(string: str) -> bool:
    """
    stringが回文の順列か判定

    時間計算量 O( len(string) )
    空間計算量 O( len(string) * 2 )
    """
    # 空白削除
    string = string.replace(" ", "")
    # すべて小文字に変換
    string = string.lower()

    # 文字列長の偶奇で分岐
    appeared_char = set([])
    if len(string) % 2 == 1:
        for char in string:
            if char in appeared_char:
                appeared_char.remove(char)
            else:
                appeared_char.add(char)

        if len(appeared_char) != 1:
            return False

    else:
        for char in string:
            if char in appeared_char:
                appeared_char.remove(char)
            else:
                appeared_char.add(char)

        if len(appeared_char) != 0:
            return False

    return True


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(is_permutation_of_palindrome("Tact Coa"), True)
        self.assertEqual(is_permutation_of_palindrome("abcde fghi"), False)
        self.assertEqual(is_permutation_of_palindrome(
            "Able was I ere I saw Elba"), True)
        self.assertEqual(is_permutation_of_palindrome("abAB"), True)


if __name__ == "__main__":
    unittest.main()
