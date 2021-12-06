# coding=utf-8
from src.constants.Constants import NORMALIZE_SCHOOLING_LEVEL, ORIGINAL_SCHOOLING_LEVEL, NORMALIZE_STATUS_SCHOOLING


class SchoolingNormalize:
    def __init__(self):
        pass

    array_normalize_schooling = NORMALIZE_SCHOOLING_LEVEL
    array_original_schooling = ORIGINAL_SCHOOLING_LEVEL
    normalize_status_schooling = NORMALIZE_STATUS_SCHOOLING

    @classmethod
    def normalize_schooling(cls, original_directory, normalize_directory):
        normalize_text = open(normalize_directory, 'wa')
        with open(original_directory, 'r') as original_text:
            text = original_text.read()
            text = cls.normalize(text)
            normalize_text.write(text)
        normalize_text.close()
        cls.replace_normalize_into_original_schooling(original_directory, normalize_directory)

    @classmethod
    def normalize(cls, text):
        for index_schooling_level in range(len(cls.array_original_schooling)):
            for original_schooling in cls.array_original_schooling[index_schooling_level]:
                normalize_text = cls.array_normalize_schooling[index_schooling_level] \
                                 + cls.normalize_status_schooling[index_schooling_level]
                text = text.replace(original_schooling, normalize_text)
        return text

    @classmethod
    def replace_normalize_into_original_schooling(cls, original_directory, normalize_directory):
        with open(original_directory, "w") as original_text:
            with open(normalize_directory, "r") as normalize_text:
                original_text.write(normalize_text.read())

