# coding=utf-8
from src.constants.Constants import ACTUAL_YEAR


class Age:
    def __init__(self):
        pass

    @classmethod
    def find_line_age(cls, line):
        if "\"age\" :" in line:
            return True
        else:
            return False

    @classmethod
    def remove_aspas_and_get_value_of_line(cls, text):
        value = text.replace('"', '') \
            .replace(',', '') \
            .replace('"\n', '')\
            .split(":")
        value = value[1]
        return value

    @classmethod
    def get_normalize_text(cls, age):
        normalize_age = ACTUAL_YEAR - int(age)
        normalize_text = "\"birthday\" : \"01/01/" + str(normalize_age) + "\""
        return normalize_text
