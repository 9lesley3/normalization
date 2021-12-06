# coding=utf-8
RANGERS_INCOME = [[0, 150], [150, 350], [350, 500], [500, 750], [750, 1100], [1100, 2000], [2000, 3000]]

INCOME_OPTIONS = ['\"income\" : \"Até 150 reais\"', '\"income\" : \"Entre 150 e 350\"',
                  '\"income\" : \"Entre 350 e 500\"', '\"income\" : \"Entre 500 e 750\"',
                  '\"income\" : \"Entre 750 e 1100\"', '\"income\" : \"Entre 1100 e 2000\"',
                  '\"income\" : \"Mais de 2000\"']

MAX_VALUE_INCOME = 2000

ACTUAL_YEAR = 2021

NORMALIZE_RACIAL_OPTIONS = ['\"racial\" : \"Amarela\"', '\"racial\" : \"Branca\"',
                            '\"racial\" : \"Indígena\"', '\"racial\" : \"Parda\"',
                            '\"racial\" : \"Preta\"', '\"racial\" : \"Outra/Não deseja informar\"']

ORIGINAL_RACIAL_OPTIONS = [['\"racial\" : \"amarela\"'], ['\"racial\" : \"branca\"'],
                           ['\"racial\" : \"indígena\"'], ['\"racial\" : \"pardo\"'],
                           ['\"racial\" : \"preta\"'], ['\"racial\" : \"Outra/Não deseja informar\"']]

ARRAY_PRIMARY_SCHOOL_1 = ['\"schooling\" : \"5 do fundamental\",']

ARRAY_INCOMPLETE_PRIMARY_SCHOOL_2 = ['\"schooling\" : \"7 série do fundamental\",']

ARRAY_COMPLETE_PRIMARY_SCHOOL_2 = ['\"schooling\" : \"Fundamental completo\",']

ARRAY_COMPLETE_HIGH_SCHOOL = ['\"schooling\" : \"2 grau completo \",']

ARRAY_INCOMPLETE_HIGH_SCHOOL = ['\"schooling\" : \"Segundo grau incompeto\",']

ARRAY_STUDYING_HIGH_SCHOOL = ['\"schooling\" : \"Cursando o segundo grau\",']

ARRAY_COMPLETE_HIGHER_SCHOOL = ['\"schooling\" : \"Curso superior completo \",']

ARRAY_INCOMPLETE_HIGHER_SCHOOL = ['\"schooling\" : \"Ensino superior incompleto \",']

ARRAY_SCHOOLING_NOT_DETERMINED = ['\"schooling\" : \"Não determinado\",']

NORMALIZE_SCHOOLING_LEVEL = ['\"schooling\" : \"Ensino fundamental 1\",',
                             '\"schooling\" : \"Ensino fundamental 2\",',
                             '\"schooling\" : \"Ensino fundamental 2\",',
                             '\"schooling\" : \"Ensino médio\",',
                             '\"schooling\" : \"Ensino médio\",',
                             '\"schooling\" : \"Ensino superior\",',
                             '\"schooling\" : \"Ensino superior\",',
                             '\"schooling\" : \"Ensino superior\",',
                             '\"schooling\" : \"Não determinado\",']

ORIGINAL_SCHOOLING_LEVEL = [ARRAY_PRIMARY_SCHOOL_1, ARRAY_INCOMPLETE_PRIMARY_SCHOOL_2,
                            ARRAY_COMPLETE_PRIMARY_SCHOOL_2, ARRAY_INCOMPLETE_HIGH_SCHOOL,
                            ARRAY_COMPLETE_HIGH_SCHOOL, ARRAY_INCOMPLETE_HIGHER_SCHOOL,
                            ARRAY_COMPLETE_HIGHER_SCHOOL, ARRAY_STUDYING_HIGH_SCHOOL,
                            ARRAY_SCHOOLING_NOT_DETERMINED]


NORMALIZE_STATUS_SCHOOLING = ['\n    \"schoolingStatus\" : \"Incompleto\",',
                              '\n    \"schoolingStatus\" : \"Incompleto\",',
                              '\n    \"schoolingStatus\" : \"Completo\",',
                              '\n    \"schoolingStatus\" : \"Incompleto\",',
                              '\n    \"schoolingStatus\" : \"Completo\",',
                              '\n    \"schoolingStatus\" : \"Incompleto\",',
                              '\n    \"schoolingStatus\" : \"Completo\",',
                              '\n    \"schoolingStatus\" : \"Cursando\",',
                              '\n    \"schoolingStatus\" : \"Incompleto\",']

ARRAY_MALE = ['\"gender\" : \"0\"', '\"gender\" : 0']
ARRAY_FEMALE = ['\"gender\" : \"1\"', '\"gender\" : 1']
ARRAY_OTHER = ['\"gender\" : \"2\"', '\"gender\" : 2']
ARRAY_NO_ANSWER = ['\"gender\" : \"3\"', '\"gender\" : 3']

NORMALIZE_GENDER = ['\"gender\" : \"Masculino\"', '\"gender\" : \"Feminino\"',
                    '\"gender\" : \"Outro\"', '\"gender\" : \"Prefere não responder\"']

ORIGINAL_GENDER = [ARRAY_MALE, ARRAY_FEMALE, ARRAY_OTHER, ARRAY_NO_ANSWER]