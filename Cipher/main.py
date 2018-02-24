# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, './cipher')

from cipher import Cipher

text = 'You were curious to crack this one'
cipher = Cipher()
print(cipher.encrypt_vigenere(text, 'ragnarok'))