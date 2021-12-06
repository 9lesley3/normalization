# coding=utf-8
import unittest

from src.constants.Constants import NORMALIZE_RACIAL_OPTIONS, ORIGINAL_RACIAL_OPTIONS
from src.directory.Directories import Directories


class TestRacialNormalize(unittest.TestCase):
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

    def test_racial_amarela_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[0])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[0])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_racial_branca_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[1])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[1])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_racial_indigena_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[2])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[2])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_racial_parda_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[3])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[3])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_racial_preta_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[4])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[4])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_racial_outra_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[5])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[5])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def sumOccurrencesNormalize(self, racial):
        return self.normalize_text.count(racial)

    def sumOccurrencesOriginal(self, array_racial):
        sum_occurrences_original = 0
        for racial in array_racial:
            sum_occurrences_original = sum_occurrences_original + self.original_text.count(racial)
        return sum_occurrences_original


if __name__ == '__main__':
    unittest.main()
