# -*- coding: utf-8 -*-
from util import split_by_index_number, convert_to_dec, convert_from_dec
from numeral_system import NumeralSystem


class Base64_Cipher():
    
    '''
        Base64
        This encryptions consists in:
        1- Getting each character of the text to its binary representation
        using the ASCII table, appending it all as a whole text
        2- Dividing the text in groups of 24 digits
        3- Filling the ones that doesn't have 24 digits
        4- Dividing again in blocks of 6 digits
        5- Converting those 6-digits-binaries to decimals
        6- Using the Base64 table, transform them to other characters
    '''
    
    #This is the dictionary used to encrypt, it has the letters equivalent to numbers on base 64 table
    b64_dict_enc = {}
    #This is the inverse of the dictionary above, used to decrypt, the numbers are equivalent to letters
    b64_dict_dec = {}
    
    def __init__(self):
        
        # The first part is 'A-Z' (converted ASCII-char): '0-25'
        self.b64_dict_enc.update({ '{}'.format(value): chr(letter_upper) 
                             for letter_upper, value in zip( range(65,91), range(0, 26) ) })
        
        # The second part is 'a-z' (converted ASCII-char): '26-51'
        self.b64_dict_enc.update({ '{}'.format(value): chr(letter_lower) 
                             for letter_lower, value in zip( range(97, 123), range(26, 52) ) })
        
        # The third part is '0-9': '52-61
        self.b64_dict_enc.update({ '{}'.format(value): '{}'.format(numbers) 
                             for numbers, value in zip( range(10), range(52, 62) ) })
        
        # The extras
        self.b64_dict_enc.update({ '62': '+', '63': '/' })
        
        # This will be the inverse of the previous
        self.b64_dict_dec = {value: key for key, value in self.b64_dict_enc.items()}
        
    def encrypt(self, text):
        '''
            Encrypt a text using base 64 standard
            
            Keyword arguments:
            text -- Text to be encrypted
        '''
        
        # If trying to encrypt a character, this work-around is needed
        if(not isinstance(text, str)):
            text = [text]
        
        # First step is to convert each letter of the text to it's ASCII equivalent
        text_asc_dec = [ord(letter) for letter in text]
        # Now we need to convert it to binary (using zfill to guarantee it will have 8 digits)
        text_asc_bin = ['{0:b}'.format(letter).zfill(8) for letter in text_asc_dec]
        
        # Then we concatenate all of the list 
        all = ''.join(text_asc_bin)
        
        # And proceed to make it divisible to 24
        rest_24 = len(all)%24
        
        # If there is a rest, we need to fill it (with 0)
        if(rest_24 != 0):
            # That's how many digits are needed to make it divisible to 24
            needs = 24 - rest_24
            # Now we need to check how many '=' we will need to fill (the groups of six 0's)
            comp_qtt = needs//6
            # Fill 'comp' with the '=' needed
            comp = '='*comp_qtt
            # Now that we already set up 'comp', it only needs the quantity of '0' necessary to fill the 6 bit left
            needs -= comp_qtt*6
            # The size 'all' is supposed to have, without the complimentary '='
            all_new_len = (len(all) + needs)
            # Fill the rest needed with '0' on its right
            all = all.ljust(all_new_len, '0')
        
        # Now we need to create groups of 6 digits, that are going to be our binaries for base64
        chunks_bin = split_by_index_number(all, 6)
        # Convert them to decimals
        chunks_dec = [convert_to_dec(c, NumeralSystem.BINARY.value) for c in chunks_bin]
        # And finally to their values in Base64 table
        chunks_base64 = [self.b64_dict_enc[c] for c in chunks_dec]
        
        # Join the list in a string
        result = "".join(chunks_base64) + comp
        
        return result

    def decrypt(self, text):
        '''
            Decrypt a text using base 64 standard
            
            Keyword arguments:
            text -- Text to be decrypted
        '''
        
        # If trying to decrypt a character, this work-around is needed
        if(not isinstance(text, str)):
            text = [text]
        
        # Gets each char in text, except for '=' (complementary)
        chunks_base64 = [c for c in text if c != '=']
        # For each letter in the text, gets its base64 table value
        chunks_dec = [self.b64_dict_dec[chunk] for chunk in chunks_base64]
        # For each number, transform to binary (up to 6 digits)
        chunks_bin = [convert_from_dec(chunk, NumeralSystem.BINARY.value, 6) for chunk in chunks_dec]
        
        # Join everything
        all = ''.join(chunks_bin) 
        # Split in groups of 8
        groups_ascii_bin = split_by_index_number(all, 8) 
        # Convert to decimal, if not thrash (last elements from the conversion added to form the '=')
        groups_ascii_dec = [convert_to_dec(element, NumeralSystem.BINARY.value) for element in groups_ascii_bin if(len(element) == 8)]
        # Transform to letters by ASCII table
        letters = [chr(int(digit)) for digit in groups_ascii_dec] 
        # Join everything
        result = ''.join(letters) 
        
        return result
    