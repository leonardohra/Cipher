# -*- coding: utf-8 -*-

text = 'Tyger Tyger burning bright In the forests of the night What immortal hand or eye Could frame thy fearful symmetry'

'''
    To work with any Cipher, you need 
    to import the "Cipher" class, that's 
    on the folder "cipher". Python needs 
    the following syntax to use a class 
    inside a folder. (It temporarily adds 
    the folder "cipher" in the variable PATH)
'''

import sys
sys.path.insert(0, './cipher')

'''
    Then import the class Cipher and 
    instantiate it, no need for parameters
    on the constructor
'''
from cipher import Cipher

cipher = Cipher()

'''
    ASCII Cipher: You'll need to import 
    NumeralSystem enumerator, it contains:
    BINARY, OCTAL, DECIMAL, HEXADECIMAL, you
    can check this on cipher/numeral_system.py
'''

from numeral_system import NumeralSystem

'''
    Every cipher can be accessed by 
    cipher.encrypt_[cipher_type], so to use 
    Ascii cipher that's the syntax:
    cipher.encrypt_ascii(text, mode, digits)
    the text is the text to be encrypted, the
    mode is the final numeral system it should
    be encrypted, and the digits are how many
    digits each character should have, for example:
    digits = 3, if the final number is '83', it will
    become '083', because it needs to be 3 digits. 
    Usually 8 digits for binary, 3 digits for octal
    3 digits for decimal, 2 digits for hexadecimal
'''
enc_bin = cipher.encrypt_ascii(text, NumeralSystem.BINARY, 8)
enc_oct = cipher.encrypt_ascii(text, NumeralSystem.OCTAL, 3)
enc_dec = cipher.encrypt_ascii(text, NumeralSystem.DECIMAL, 3)
enc_hex = cipher.encrypt_ascii(text, NumeralSystem.HEXADECIMAL, 2)

print('Text in binary:')
print(enc_bin)
print('Text in octal:')
print(enc_oct)
print('Text in decimal:')
print(enc_dec)
print('Text in hexadecimal:')
print(enc_hex)
    
'''
    To decrypt, the same rules above apply
'''    

print('\nEncrypted text decrypted:')
    
dec_bin = cipher.decrypt_ascii(enc_bin, NumeralSystem.BINARY, 8)
dec_oct = cipher.decrypt_ascii(enc_oct, NumeralSystem.OCTAL, 3)
dec_dec = cipher.decrypt_ascii(enc_dec, NumeralSystem.DECIMAL, 3)
dec_hex = cipher.decrypt_ascii(enc_hex, NumeralSystem.HEXADECIMAL, 2)
    
print('Text from binary:')
print(dec_bin)
print('Text from octal:')
print(dec_oct)
print('Text from decimal:')
print(dec_dec)
print('Text from hexadecimal:')
print(dec_hex)

'''
    Base64: You only need the text as a parameter
'''

print('\nText enconded with base64 encryption:')

base64_enc = cipher.encrypt_base64(text)
print(base64_enc)

print('\nText decoded with base64 decryption:')

base64_dec = cipher.decrypt_base64(base64_enc)
print(base64_dec)

'''
    Shift Cipher: You'll need the text and the 
    quantity of characters you want to displace
    this number can be from 0 (no change) to 25
    (one letter before). But in the decryption
    you can also not specify the shift, and have
    the program try every combination possible and
    return them in an list.
'''

print('\nText encoded with shift cipher (20 shifts):')
shift_enc = cipher.encrypt_shift(text, 20)

print(shift_enc)

print('\nText decoded with shift cipher (20 shifts):')
shift_dec = cipher.decrypt_shift(shift_enc, 20)

print('\nText decoded with bruteforce (all shifts):')
shift_dec_all = cipher.decrypt_shift(shift_enc)

print(shift_dec_all)

'''
    Vigenere shift: You'll need the a key and the text
'''

key = 'Red John'

print('\nText encrypted with vigenere shift:')
vig_shift = cipher.encrypt_vigenere(text, key)

print(vig_shift)


print('\nText decription with vigenere shift:')
vig_shift_dec = cipher.decrypt_vigenere(vig_shift, key)

print(vig_shift_dec)

