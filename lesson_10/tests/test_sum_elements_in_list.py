from unittest.mock import patch, call
import pytest
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_10 import sum_of_list_elements

@pytest.mark.positive
class TestSumElementsInLisPositiveScenarious:
    @pytest.mark.parametrize("lst, expected_sum", [
        (['1,2,3,4'], 10),
        (['50, 1'], 51),
    ], ids=["['1,2,3,4']", "['50, 1']"])
    def test_valid_simple_input(self, lst, expected_sum):
        with patch('builtins.print') as mock_print:
            sum_of_list_elements(lst)
            try:
                mock_print.assert_called_with(expected_sum)
            except AssertionError:
                raise AssertionError(f"Expected sum of {lst} to be printed as {expected_sum}, but it wasn't")


    def test_valid_input_with_several_elements(self):
        with patch('builtins.print') as mock_print:
            lst = ['1,2,3,4', '1,2,3,4,50']
            sum_of_list_elements(lst)
            mock_print.assert_has_calls([call(10), call(60)])
@pytest.mark.negative
class TestSumElementsInListNegativeScenarious:
    def test_empty_list(self):
        with patch('builtins.print') as mock_print:
            lst = []
            sum_of_list_elements(lst)
            mock_print.assert_called_with('List is empty')


    def test_input_with_empty_string_element(self):
        with patch('builtins.print') as mock_print:
            lst = [""]
            sum_of_list_elements(lst)
            mock_print.assert_called_with('Не можу це зробити')

    def test_invalid_input_with_non_numeric_string(self):
        with patch('builtins.print') as mock_print:
            lst = ['qwerty1,2,3']
            sum_of_list_elements(lst)
            mock_print.assert_called_with('Не можу це зробити')

    @pytest.mark.parametrize("lst, expected_result_1, expected_result_2", [
        (['1,2,3,4', 'qwerty1,2,3'], 10, 'Не можу це зробити'),
        (['qwerty1,2,3', '50, 50'], 'Не можу це зробити', 100)
    ], ids=["['1,2,3,4', 'qwerty1,2,3']", "['qwerty1,2,3', '50, 50']"])
    def test_input_with_mixed_valid_and_invalid_elements(self, lst, expected_result_1, expected_result_2):
        with patch('builtins.print') as mock_print:
            sum_of_list_elements(lst)
            mock_print.assert_has_calls([call(expected_result_1), call(expected_result_2)])

    def test_none_with_none_input_returns_exception(self):
        with patch('builtins.print') as mock_print:
            lst = [None]
            sum_of_list_elements(lst)
            mock_print.assert_called_with("Інша помилка")



