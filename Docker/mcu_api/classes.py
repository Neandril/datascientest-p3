from enum import Enum

# Class for Mcu informations
class Mcu(str):
    name = ''
    comic = ''
    relationship = ''

# Class disaplying a dropdown list for number choice
class Nb_Results(str, Enum):
    First_10 = '10',
    First_50 = '50',
    All = 'All'
