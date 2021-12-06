# coding=utf-8
import unittest

from src.directory.Directories import Directories
from src.constants.Constants import NORMALIZE_SCHOOLING_LEVEL, ORIGINAL_SCHOOLING_LEVEL


class MyTestCase(unittest.TestCase):
    normalize = file
    original = file
    normalize_text = ""
    original_text = ""
    occurrences_normalize_text = 0
    occurrences_original_text = 0
    normalize_directory = Directories.normalize_directory.value
    original_directory = Directories.original_directory.value
    array_normalize_schooling = NORMALIZE_SCHOOLING_LEVEL
    array_original_schooling = ORIGINAL_SCHOOLING_LEVEL

    @classmethod
    def setUp(cls):
        cls.normalize = open(cls.normalize_directory, 'r')
        cls.original = open(cls.original_directory, 'r')
        cls.normalize_text = cls.normalize.read()
        cls.original_text = cls.original.read()

    def tearDown(self):
        self.normalize.close()
        self.original.close()

    def test_primary_school_1_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_schooling[0])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_schooling[0])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_primary_school_2_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_schooling[1])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_schooling[1])
        self.occurrences_original_text += self.sumOccurrencesOriginal(self.array_original_schooling[2])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_high_school_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_schooling[3])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_schooling[3])
        self.occurrences_original_text += self.sumOccurrencesOriginal(self.array_original_schooling[4])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_higher_school_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_schooling[5])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_schooling[5])
        self.occurrences_original_text += self.sumOccurrencesOriginal(self.array_original_schooling[6])
        self.occurrences_original_text += self.sumOccurrencesOriginal(self.array_original_schooling[7])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_schooling_not_determined_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_schooling[8])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_schooling[8])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_occurrences_of_schooling_and_schoolingStatus_is_equal(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize("schooling : ")
        self.occurrences_original_text = self.sumOccurrencesOriginal(["schoolingStatus : "])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def sumOccurrencesNormalize(self, level_schooling):
        return self.normalize_text.count(level_schooling)

    def sumOccurrencesOriginal(self, array_schooling):
        val = array_schooling[0]
        return self.original_text.count(val)


if __name__ == '__main__':
    unittest.main()
