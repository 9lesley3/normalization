from src.constants.Constants import NORMALIZE_RACIAL_OPTIONS, ORIGINAL_RACIAL_OPTIONS


class RacialNormalize:
    def __init__(self):
        pass

    array_normalize_racial = NORMALIZE_RACIAL_OPTIONS
    array_original_racial = ORIGINAL_RACIAL_OPTIONS

    @classmethod
    def normalize_racial(cls, original_directory, normalize_directory):
        normalize_text = open(normalize_directory, 'wa')
        with open(original_directory, 'r') as original_text:
            text = original_text.read()
            text = cls.normalize(text)
            normalize_text.write(text)
        normalize_text.close()
        cls.replace_normalize_into_original_racial(original_directory, normalize_directory)

    @classmethod
    def normalize(cls, text):
        for index_racial_options in range(len(cls.array_original_racial)):
            for original_racial in cls.array_original_racial[index_racial_options]:
                text = text.replace(original_racial, cls.array_normalize_racial[index_racial_options])
        return text

    @classmethod
    def replace_normalize_into_original_racial(cls, original_directory, normalize_directory):
        with open(original_directory, "w") as original_text:
            with open(normalize_directory, "r") as normalize_text:
                original_text.write(normalize_text.read())