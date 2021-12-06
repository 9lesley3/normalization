# coding=utf-8

from src.income.Income import Income


class IncomeNormalize:
    def __init__(self):
        pass

    @classmethod
    def normalize_income(cls, rangers_income, original_directory, normalize_directory):
        normalize_text = open(normalize_directory, 'wa')
        with open(original_directory, 'r') as original_text:
            for line in original_text:
                if Income.find_line_income(line):
                    income_text = Income.remove_aspas_and_get_value_of_line(line)
                    income_value = Income.value_validation(income_text)
                    text_line = Income.get_normalize_text(income_value, rangers_income, line)
                    normalize_text.write('    ' + text_line + ',\n')
                else:
                    normalize_text.write(line)
        normalize_text.close()
        cls.replace_normalize_into_original_income(original_directory, normalize_directory)

    @classmethod
    def replace_normalize_into_original_income(cls, original_directory, normalize_directory):
        with open(original_directory, "w") as original_text:
            with open(normalize_directory, "r") as normalize_text:
                original_text.write(normalize_text.read())