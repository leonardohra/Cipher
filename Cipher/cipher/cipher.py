# -*- coding: utf-8 -*-
from ascii_cipher import Ascii_Cipher
from base64_cipher import Base64_Cipher
from shift_cipher import Shift_Cipher
from vigenere_cipher import Vigenere_Cipher
from numeral_system import NumeralSystem

class Cipher():
    a_c = None
    b_c = None
    s_c = None
    v_c = None
    
    def __init__(self):
        self.a_c = Ascii_Cipher()
        self.b_c = Base64_Cipher()
        self.s_c = Shift_Cipher()
        self.v_c = Vigenere_Cipher()
    
    def encrypt_ascii(self, text, mode, digits):
        '''
            With a text, given the numeral system the user wants
            and how many digits he wants to use, this method will
            try to encrypt it.
            
            Keyword arguments:
            
            text -- the text to be encrypted
            mode -- numeral system it will be encrypted on
            digits -- how many digits form one number in this system
        '''
        
        return self.a_c.encrypt(text, mode, digits)
    
    def decrypt_ascii(self, encrypted, mode, digits):
        ''' 
            With a string of numbers, given the numeral system it's on 
            and how many digits forms one number, this method will try
            to decrypt the text.
            
            Keyword arguments:
            
            encrypted -- the text encrypted
            mode -- numeral system it is encrypted on
            digits -- how many digits form one number in this system
            
        '''
                
        return self.a_c.decrypt(encrypted, mode, digits)

    def encrypt_base64(self, text):
        '''
            Encrypt a text using base 64 standard
            
            Keyword arguments:
            text -- Text to be encrypted
        '''
        
        return self.b_c.encrypt(text)
        
    def decrypt_base64(self, text):
        '''
            Decrypt a text using base 64 standard
            
            Keyword arguments:
            text -- Text to be decrypted
        '''
        
        return self.b_c.decrypt(text)
        
    def encrypt_shift(self, text, shift):
        '''
            This method gets a text and change every letter to
            the letter at position letter + shift
            
            Keyword arguments:
            text -- the text to be encrypted
            shift -- how many positions of the letter it will be shifted
        '''
        
        return self.s_c.encrypt(text, shift)
        
    def decrypt_shift(self, text, shifts=None):
        '''
            It uses the shifts passed as parameters to unshift the text.
            If no shift passed, it will do all possible shifts.
            
            Keyword arguments:
            text -- Text to by decrypted
            shift -- list of possible shifts it is. If not specified, it will try every possible one.
        '''
        
        return self.s_c.decrypt(text, shifts)
        
    def encrypt_vigenere(self, text, keyword):
        '''
            This method uses a keyword to encrypt a text
            
            Keyword arguments:
            text -- the text to be encrypted
            keyword -- keyword based to encrypt
        '''
        
        return self.v_c.encrypt(text, keyword)
        
    def decrypt_vigenere(self, text, keyword):
        '''
            This method uses a keyword to decrypt a text
            
            Keyword arguments:
            text -- the text to be decrypted
            keyword -- keyword based to decrypt
        '''
        
        return self.v_c.decrypt(text, keyword)
        
    def encrypt_all(self, text, keyword = None):
        
        #First we will encrypt with all the possibilities of ASCII
        #(Binary, Octal, Decimal, Hexadecimal)
        modes = [NumeralSystem.BINARY, NumeralSystem.OCTAL, NumeralSystem.DECIMAL, NumeralSystem.HEXADECIMAL]
        digits = [8, 3, 3, 2]
        
        print('ASCII encryption: ')
        print()
        
        for i in range(len(modes)):
            enc = self.encrypt_ascii(text, modes[i], digits[i])
            print('Mode: {} Digits used: {} \nEncrypted text: {}'.format(modes[i], digits[i], enc))
            
        print()
        print('Base64 encryption: ')
        print()
        
        enc = self.encrypt_base64(text)
        print('Encrypted text: {}'.format(enc))
        
        print()
        print('Shift encryption: ')
        print()
        
        shifts = [i + 1 for i in range(25)]
        
        for shift in shifts:
            enc = self.encrypt_shift(text, shift)
            print('Shift used: {} \nEncrypted text: {}'.format(shift, enc))
            
        print()
        print('Vigenère encryption: ')
        print()
        
        if(keyword == None):
            print('No keyword provided, so it\'s impossible to encrypt text.')
        else:
            enc = self.encrypt_vigenere(text, keyword)
            print('Keyword used: {} \nEncrypted text: {}'.format(keyword, enc))
            
            
            
            
            
            