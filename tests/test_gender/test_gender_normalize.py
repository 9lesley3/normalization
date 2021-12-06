# coding=utf-8
import unittest

from src.directory.Directories import Directories
from src.constants.Constants import NORMALIZE_GENDER, ORIGINAL_GENDER


class TestGenderNormalize(unittest.TestCase):
    normalize = file
    original = file
    normalize_text = ""
    original_text = ""
    occurrences_normalize_text = 0
    occurrences_original_text = 0
    normalize_directory = Directories.normalize_directory.value
    original_directory = Directories.original_directory.value
    array_normalize_gender = NORMALIZE_GENDER
    array_original_gender = ORIGINAL_GENDER

    @classmethod
    def setUp(cls):
        cls.normalize = open(cls.normalize_directory, 'r')
        cls.original = open(cls.original_directory, 'r')
        cls.normalize_text = cls.normalize.read()
        cls.original_text = cls.original.read()

    def tearDown(self):
        self.normalize.close()
        self.original.close()

    def test_gender_male_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[0])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[0],
                                                                     self.array_normalize_gender[0])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_gender_female_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[1])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[1],
                                                                     self.array_normalize_gender[1])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_gender_other_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[2])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[2],
                                                                     self.array_normalize_gender[2])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def test_gender_no_answer_normalize(self):
        self.occurrences_normalize_text = self.sumOccurrencesNormalize(self.array_normalize_gender[3])
        self.occurrences_original_text = self.sumOccurrencesOriginal(self.array_original_gender[3],
                                                                     self.array_normalize_gender[3])

        self.assertEqual(self.occurrences_original_text, self.occurrences_normalize_text)

    def sumOccurrencesNormalize(self, gender):
        return self.normalize_text.count(gender)

    def sumOccurrencesOriginal(self, original_gender, normalize_gender):
        return self.original_text.count(original_gender[0]) + self.original_text.count(
            original_gender[1]) + self.original_text.count(normalize_gender)


if __name__ == '__main__':
    unittest.main()
