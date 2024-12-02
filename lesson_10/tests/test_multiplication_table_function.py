import pytest
from unittest.mock import patch, call
import sys
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_10 import multiplication_table

@pytest.mark.positive
@pytest.mark.multiplication
class TestMultiplicationTableFunctionPositiveScenariouse:
    def test_multiplication_table(self):
        with patch('builtins.print') as mock_print:
            multiplication_table(3)
            mock_print.assert_has_calls([call('3x1=3'), call('3x2=6'), call('3x3=9'),
                                         call('3x4=12'), call('3x5=15'), call('3x6=18'),
                                         call('3x7=21'), call('3x8=24'), call("Can't be > 25")])