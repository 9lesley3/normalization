# coding=utf-8
import unittest

from src.income.Income import Income
from src.directory.Directories import Directories
from src.constants.Constants import RANGERS_INCOME, INCOME_OPTIONS


class TestIncomeNormalize(unittest.TestCase):
    normalize = file
    original = file
    normalize_text = ""
    original_text = ""
    occurrences_normalize_text = 0
    occurrences_original_text = 0
    normalize_directory = Directories.normalize_directory.value
    original_directory = Directories.original_directory.value
    array_rangers_income = RANGERS_INCOME
    array_income_options = INCOME_OPTIONS

    @classmethod
    def setUp(cls):
        cls.normalize = open(cls.normalize_directory, 'r')
        cls.original = open(cls.original_directory, 'r')
        cls.normalize_text = cls.normalize.read()
        cls.original_text = cls.original.read()

    def tearDown(self):
        self.normalize.close()
        self.original.close()

    def test_income_of_up_to_150_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[0])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[0])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_between_150_and_350_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[1])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[1])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_between_350_and_500_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[2])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[2])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_between_500_and_750_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[3])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[3])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_between_750_and_1100_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[4])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[4])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_between_1100_and_2000_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[5])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[5])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_income_over_2000_normalize(self):
        self.occurrences_normalize_text = self.sum_occurrences_normalize(self.array_income_options[6])
        self.occurrences_original_text = self.sum_occurrences_original(self.array_rangers_income[6])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def sum_occurrences_normalize(self, income_bracket):
        return self.normalize_text.count(income_bracket)

    def sum_occurrences_original(self, rangers_income):
        cont = 0  # type: int
        with open(self.original_directory, "r") as original_text:
            for line in original_text:
                if Income.find_line_income(line):
                    income_text = Income.remove_aspas_and_get_value_of_line(line)
                    income_value = Income.value_validation(income_text)
                    if Income.check_if_the_value_is_within_range(income_value, rangers_income[0], rangers_income[1]):
                        cont = cont + 1
        return cont


if __name__ == '__main__':
    unittest.main()
