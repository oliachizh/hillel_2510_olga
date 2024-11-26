import unittest
import sys
import pathlib
import random
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from homework_09 import check_age_more_than_30
from hillel_2510_olga.lesson_09.core.function_asserts import assert_true


people_records = [
      ('John', 'Doe', 28, 'Engineer', 'New York'),
      ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
      ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
      ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
      ('Michael', 'Brown', 22, 'Student', 'Seattle'),
      ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
      ('David', 'Miller', 33, 'Software Developer', 'Austin'),
      ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
      ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
      ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
      ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
      ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
      ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
      ('Ava', 'White', 42, 'Journalist', 'San Diego'),
      ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

class TestCheckAgePositiveScenariouse(unittest.TestCase):
    def test_check_age_more_than_30(self):
        valid_indexes = [i for i, record in enumerate(people_records) if record[2] >= 30]
        indexes = (random.sample(valid_indexes, 3))
        expected_result = True
        assert_true(people_records, indexes,expected_result)


class TestCheckAgeNegativeScenariouse(unittest.TestCase):
    def test_check_age_less_30(self):
        invalid_indexes = [i for i, record in enumerate(people_records) if record[2] < 30]
        indexes = (random.sample(invalid_indexes, 3))
        expected_result = False
        assert_true(people_records, indexes, expected_result)

    def test_check_age_with_invalid_indexes(self):
        indexes = (1,2, 90)
        expected_result = "Write correct indexes"
        assert_true(people_records,indexes,expected_result)



if __name__ == '__main__':
    unittest.main()