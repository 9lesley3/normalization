from src.age.AgeNormalize import AgeNormalize
from src.constants.Constants import RANGERS_INCOME
from src.directory.Directories import Directories
from src.gender.GenderNormalize import GenderNormalize
from src.income.IncomeNormalize import IncomeNormalize
from src.schooling.SchoolingNormalize import SchoolingNormalize
from src.racial.RacialNormalize import RacialNormalize
import os


def normalize_diff(original_directory, normalize_directory, diff_directory):
    diff_text = open(diff_directory, 'w')
    os.system('diff ' + normalize_directory + ' ' + original_directory + ' >> ' + diff_directory)
    diff_text.close()


def should_normalize_diff(diff_directory):
    diff_text = open(diff_directory, 'r')
    print (diff_text.read())
    diff_text.close()


def replace_text_original_into_auxiliary(original_directory, auxiliary_directory):
    with open(auxiliary_directory, "w") as auxiliary_text:
        with open(original_directory, "r") as original_text:
            auxiliary_text.write(original_text.read())


class Main:
    def __init__(self):
        pass

    normalize_directory = Directories.normalize_directory.value
    original_directory = Directories.original_directory.value
    auxiliary_directory = Directories.auxiliary_directory.value
    diff_directory = Directories.diff_directory.value
    rangers_income = RANGERS_INCOME
    normalize_text_formatted = ""  # type: str

    replace_text_original_into_auxiliary(original_directory, auxiliary_directory)

    IncomeNormalize.normalize_income(rangers_income, auxiliary_directory, normalize_directory)
    RacialNormalize.normalize_racial(auxiliary_directory, normalize_directory)
    SchoolingNormalize.normalize_schooling(auxiliary_directory, normalize_directory)
    GenderNormalize.normalize_gender(auxiliary_directory, normalize_directory)
    AgeNormalize.normalize_age(auxiliary_directory, normalize_directory)

    normalize_diff(original_directory, normalize_directory, diff_directory)
    should_normalize_diff(diff_directory)
