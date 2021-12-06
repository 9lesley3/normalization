from src.age.Age import Age


class AgeNormalize:
    def __init__(self):
        pass

    @classmethod
    def normalize_age(cls,original_directory, normalize_directory):
        normalize_text = open(normalize_directory, 'wa')
        with open(original_directory, 'r') as original_text:
            for line in original_text:
                if Age.find_line_age(line):
                    age_value = Age.remove_aspas_and_get_value_of_line(line)
                    text_line = Age.get_normalize_text(age_value)
                    normalize_text.write('    ' + text_line + '\n')
                else:
                    normalize_text.write(line)
        normalize_text.close()
        cls.replace_normalize_into_original_age(original_directory, normalize_directory)

    @classmethod
    def replace_normalize_into_original_age(cls, original_directory, normalize_directory):
        with open(original_directory, "w") as original_text:
            with open(normalize_directory, "r") as normalize_text:
                original_text.write(normalize_text.read())