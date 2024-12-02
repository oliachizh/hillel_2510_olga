import pytest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_10 import find_longest_word

class TestFindLongestWordPositiveScenariouse:
    @pytest.mark.parametrize("test_input,expected", [
        (["w", "ww"], "ww"),
        (["test", "longtest"], "longtest"),
        (["test", "word", "mytest"], "mytest"),
    ])
    def test_find_longest_word_simple_valid_input(self, test_input, expected):
        actual = find_longest_word(test_input)
        assert actual == expected

class TestFindLongestWordNegativeScenariouse:
    def test_find_longest_word_invalid_input_type(self):
        actual = find_longest_word([1])
        assert actual == "Must be str"
    def test_find_longest_word_with_empty_list(self):
        with pytest.raises(ValueError) as exc:
            find_longest_word([])
        assert str(exc.value) == "list cant be empty"
