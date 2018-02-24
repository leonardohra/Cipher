# -*- coding: utf-8 -*-

from enum import Enum

class NumeralSystem(Enum):
    '''
        We will need this Enum to indicate which numeral system something is on.
    '''
    BINARY = 2
    OCTAL = 8
    DECIMAL = 10
    HEXADECIMAL = 16