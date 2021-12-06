# coding=utf-8
from src.constants.Constants import NORMALIZE_GENDER, ORIGINAL_GENDER


class GenderNormalize:
    def __init__(self):
        pass

    array_normalize_gender = NORMALIZE_GENDER
    array_original_gender = ORIGINAL_GENDER

    @classmethod
    def normalize_gender(cls, original_directory, normalize_directory):
        normalize_text = open(normalize_directory, 'wa')
        with open(original_directory, 'r') as original_text:
            text = original_text.read()
            text = cls.normalize(text)
            normalize_text.write(text)
        normalize_text.close()
        cls.replace_normalize_into_original_gender(original_directory, normalize_directory)

    @classmethod
    def normalize(cls, text):
        for index_gender_options in range(len(cls.array_original_gender)):
            for original_gender in cls.array_original_gender[index_gender_options]:
                text = text.replace(original_gender, cls.array_normalize_gender[index_gender_options])
        return text

    @classmethod
    def replace_normalize_into_original_gender(cls, original_directory, normalize_directory):
        with open(original_directory, "w") as original_text:
            with open(normalize_directory, "r") as normalize_text:
                original_text.write(normalize_text.read())