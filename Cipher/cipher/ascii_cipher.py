# -*- coding: utf-8 -*-

from util import split_by_index_number, convert_to_dec, convert_from_dec
from numeral_system import NumeralSystem

class Ascii_Cipher():
    ''' 
        ASCII
        Some texts are translated to their numbers using the ASCII table
        So it's possible to have a text in its numbers in ASCII as Binary,
        Octal, Decimal or Hexadecimal (those are the most common)
    '''
    
    def encrypt(self, text, mode, digits):
        '''
            With a text, given the numeral system the user wants
            and how many digits he wants to use, this method will
            try to encrypt it.
            
            Keyword arguments:
            
            text -- the text to be encrypted
            mode -- numeral system it will be encrypted on
            digits -- how many digits form one number in this system
        '''
        
        #Splits every character in the text to encrypt each one.
        characters = [c for c in text]
        #For every character, gets the ASCII equivalent in decimal
        chars_ascii = [str(ord(c)) for c in characters]
        
        #This will convert from base 10 (decimal) to base 'mode' (binary, octal, etc)
        ascii_to_mode = [convert_from_dec(num, mode.value, digits) for num in chars_ascii]
        #Join everything back to one string
        result = "".join(ascii_to_mode)
        
        return result
    
    def decrypt(self, encrypted, mode, digits):
        ''' 
            With a string of numbers, given the numeral system it's on 
            and how many digits forms one number, this method will try
            to decrypt the text.
            
            Keyword arguments:
            
            encrypted -- the text encrypted
            mode -- numeral system it is encrypted on
            digits -- how many digits form one number in this system
            
        '''
    
        # If trying to decrypt a character, this work-around is needed
        #if(not isinstance(encrypted, list)):
            #encrypted = [encrypted]
        
        #Let's divide all the encrypted string in bunches of numbers in their system
        divided = split_by_index_number(encrypted, digits)
        
        #A list that will contain the numbers equivalent to ASCII in decimal
        #For each number, let's convert it to decimal
        decimal = [convert_to_dec(divid, mode.value) for divid in divided]
        
        #Then get their character equivalent to the number
        list_chars = [chr(int(digit)) for digit in decimal]
        #Join everything back to one string
        result = ''.join(list_chars)
        
        return result
