import unittest


def group_anagrams(strings: str) -> list[str]:
    """
    docstring
    """
    anagram_dict: dict[str, list[str]] = {}

    for string in strings:
        sorted_str = "".join(sorted(string))

        if sorted_str not in anagram_dict:
            anagram_dict[sorted_str] = []

        anagram_dict[sorted_str].append(string)

    sorted_keys = sorted(anagram_dict.keys())

    res = []
    for anagram in sorted_keys:
        res += sorted(anagram_dict[anagram])
    return res


class Test(unittest.TestCase):
    def test_group_anagrams(self):
        strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]

        self.assertEqual(group_anagrams(strings),
                         ['arts', 'star', 'bat', 'tab', 'car', 'cat', 'rat', 'tar'])


if __name__ == "__main__":
    unittest.main()
