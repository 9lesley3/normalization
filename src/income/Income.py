# coding=utf-8
from src.constants.Constants import MAX_VALUE_INCOME


class Income:
    def __init__(self):
        pass

    @classmethod
    def is_blank(cls, string):
        if string and string.strip():
            return False
        return True

    @classmethod
    def remove_aspas_and_get_value_of_line(cls, text):
        value = text.replace('"', '').split(":")
        value = value[1].split(",")
        value = value[0]
        return value

    @classmethod
    def value_validation(cls, text):
        value = text.split(".")
        print(value)
        if len(value) > 1:
            return cls.value_has_point(text, value)
        elif len(value) > 1 and (not value[0].contains(('[', '{', '"\n'))):
            return int(value[0])

    @classmethod
    def value_has_point(cls, text, value):
        if (int(value[1]) > 0) or (int(value[0]) < 10):
            return int(text.replace('.', ''))
        else:
            return int(value[0])

    @classmethod
    def get_normalize_text(cls, income, rangers_income, line):
        normalize_text = ""
        for range_value in rangers_income:
            income_min = range_value[0]
            income_max = range_value[1]
            if income <= 150:
                normalize_text = "\"income\" : \"Até 150 reais\""
                break
            elif income > 2000:
                normalize_text = "\"income\" : \"Mais de 2000\""
                break
            elif (income <= income_max) and (income > income_min):
                normalize_text = "\"income\" : \"Entre " + str(income_min) + " e " + str(income_max) + "\""
                break
            else:
                normalize_text = ""

        if cls.is_blank(normalize_text):
            return line
        else:
            return normalize_text

    @classmethod
    def find_line_income(cls, line):
        if ("\"income\" :" in line) and not ('\"Entre ' in line) and not ('\"Até ' in line) \
                and not ('\"Mais ' in line) and not ('\"Desejo ' in line) and not ('[' in line) \
                and not ('{' in line) and not ('"\n' in line):
            return True
        else:
            return False

    @classmethod
    def check_if_the_value_is_within_range(cls, income, income_mim, income_max):
        if (income <= income_max) and (income >= income_mim):
            return True
        elif (income > MAX_VALUE_INCOME) and (income_mim >= MAX_VALUE_INCOME):
            return True
        else:
            return False
