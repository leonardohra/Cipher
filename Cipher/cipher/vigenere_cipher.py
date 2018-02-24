# -*- coding: utf-8 -*-
from shift_cipher import Shift_Cipher 

class Vigenere_Cipher():
    
    '''
        Vigenère Cipher
        It consists in:
        1- With a keyword, use every character to encrypt every character of the text
        (key[0] to encrypt text[0] (...), when the keyword finishes, go back to first digit of keyword)
        2- The encryption is based on Caesar Cipher. A = 0 shifts, B = 1 shift, C = 2 shift (...)
    '''
    def __encrypt_or_decrypt(self, text, keyword, encrypt):
        '''
            This function uses Cipher Shift to shift (encrypt)
            or unshift (decrypt) the text, according to the 
            parameter encrypt
            
            Keyword arguments:
            text -- the text to be encryted/decrypted
            keyword -- keyword based to encryted/decrypt
            encrypt -- whether the text should be encrypted 
            or decrypted (True to encrypt text)
        '''
        
        s_c = Shift_Cipher()
        function = { 
            True: s_c.encrypt, 
            False: s_c.decrypt
                    }
        
        # We should get every letter to a list.
        letters = [chara for chara in text if chara.isalpha()] 
        # Get the upper case of each character of keyword
        keyword = [chara.upper() for chara in keyword if chara.isalpha()]
        # This list will have the letters as shifts, A (65 on ASCII) should shift 0, B (66 on ASCII) should shift 1 (...)
        shifts = [ord(c) - 65 for c in keyword]
        
        let_enc = [function[encrypt](letters[i], shifts[i%len(shifts)]) for i in range(len(letters))]
        
        ret = []
        count = 0
        for i in range(len(text)):
            value = ''
            
            if(text[i].isalpha()):
                value = let_enc[count]
                count += 1
            else:
                value = text[i]
            
            ret.append(value)
        
        return ''.join(ret)
        
    def encrypt(self, text, keyword):
        '''
            This method uses a keyword to encrypt a text
            
            Keyword arguments:
            text -- the text to be encrypted
            keyword -- keyword based to encrypt
        '''
        result = self.__encrypt_or_decrypt(text, keyword, True)
        
        return result
    
    def decrypt(self, text, keyword):
        '''
            This method uses a keyword to decrypt a text
            
            Keyword arguments:
            text -- the text to be decrypted
            keyword -- keyword based to decrypt
        '''
        result = self.__encrypt_or_decrypt(text, keyword, False)
        
        return result