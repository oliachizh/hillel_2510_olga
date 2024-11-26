import random
import sys
import pathlib
import random
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_09 import check_age_more_than_30
def assert_true(people_records, indexes, expected_result):
    actual_result = check_age_more_than_30(people_records, *indexes)
    assert actual_result == expected_result, f'Expected {expected_result}, but got {actual_result}'