# coding=utf-8
import unittest

from src.constants.Constants import NORMALIZE_RACIAL_OPTIONS, ORIGINAL_RACIAL_OPTIONS
from src.directory.Directories import Directories


class TestAgeNormalize(unittest.TestCase):
    normalize = file
    original = file
    normalize_text = ""
    original_text = ""
    occurrences_normalize_text = 0
    occurrences_original_text = 0
    normalize_directory = Directories.normalize_directory.value
    original_directory = Directories.original_directory.value
    array_normalize_gender = NORMALIZE_RACIAL_OPTIONS
    array_original_gender = ORIGINAL_RACIAL_OPTIONS

    @classmethod
    def setUp(cls):
        cls.normalize = open(cls.normalize_directory, 'r')
        cls.original = open(cls.original_directory, 'r')
        cls.normalize_text = cls.normalize.read()
        cls.original_text = cls.original.read()

    def tearDown(self):
        self.normalize.close()
        self.original.close()

    def test_age_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize("birthday")
        self.occurrences_original_text = self.sumOccurrencesOriginal("age")

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def sumOccurrencesNormalize(self, age_value):
        return self.normalize_text.count(age_value)

    def sumOccurrencesOriginal(self, age_value):
        return self.original_text.count(age_value)


if __name__ == '__main__':
    unittest.main()
