import unittest
from unittest.mock import patch, call
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_09 import sum_of_list_elements

class TestSumOfListElementsPositiveScenarious(unittest.TestCase):
    def test_valid_simple_input(self):
        with patch('builtins.print') as mock_print:
            lst = ['1,2,3,4']
            actual = sum_of_list_elements(lst)
            try:
                mock_print.assert_called_once_with(10)
            except AssertionError:
                raise AssertionError("Expected sum of '1,2,3,4' to be printed as 10, but it wasn't")



    def test_valid_input_with_several_elements(self):
        with patch('builtins.print') as mock_print:
            lst = ['1,2,3,4', '1,2,3,4,50']
            sum_of_list_elements(lst)
            mock_print.assert_has_calls([call(10), call(60)])

class TestSumOfListElementsNegativeScenarious(unittest.TestCase):
    def test_empty_list(self):
        with patch('builtins.print') as mock_print:
            lst = []
            sum_of_list_elements(lst)
            mock_print.assert_called_with('List is empty')

    def test_empty_lis(self):
        with patch('builtins.print') as mock_print:
            lst = [""]
            sum_of_list_elements(lst)
            mock_print.assert_called_with('Не можу це зробити')

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

    def test_input_with_mixed_valid_and_invalid_elements(self):
        with patch('builtins.print') as mock_print:
            lst = ['1,2,3,4', 'qwerty1,2,3']
            sum_of_list_elements(lst)
            mock_print.assert_has_calls([call(10), call('Не можу це зробити')])

    def test_none_with_none_input_returns_exception(self):
        with patch('builtins.print') as mock_print:
            lst = [None]
            sum_of_list_elements(lst)
            mock_print.assert_called_with("Інша помилка")



if __name__ == '__main__':
    unittest.main()

