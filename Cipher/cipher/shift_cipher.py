# -*- coding: utf-8 -*-

class Shift_Cipher():
    
    '''
        Shift Cipher
        This encryption consists in:
        1- Get the letter of the alphabet
        2- Replaces by the letter in its position + X (shift)
    '''
    
    def encrypt(self, text, shift):
        '''
            This method gets a text and change every letter to
            the letter at position letter + shift
            
            Keyword arguments:
            text -- the text to be encrypted
            shift -- how many positions of the letter it will be shifted
        '''
        
        # If trying to encrypt a character, this work-around is needed
        if(not isinstance(text, str)):
            text = [text]
        
        # We should get every letter to a list.
        letters = [chara for chara in text if chara.isalpha()]
        # Then get their values in decimal base, at ASCII table
        ascii_dec = [ord(letter) for letter in letters]
        
        # Now for the shifting: 
        ascii_dec_shifted = []
        for dec in ascii_dec:
             # The shifted letter will be the decimal + shift
            shifted = dec + shift
            
            #But if it is A-Z (dec <= 90) and after the shift it now is something after Z or
            #It was a-z (between 97 and 122) and after the shift it's after z (122), it must 
            #go back to the start of the alphabet.
            if( (dec <= 90 and shifted > 90) or 
                ( (dec >= 97 and dec <= 122) and shifted > 122) ): 
                shifted -= 26
                
            ascii_dec_shifted.append(shifted)
            
        # Transform it back to letters
        letters_shifted = [chr(dec) for dec in ascii_dec_shifted]
        
        # Where there were letters, but the new ones, otherwise, put what was in text.
        ret = []
        count = 0
        for i in range(len(text)):
            value = ''
            
            if(text[i].isalpha()):
                value = letters_shifted[count]
                count += 1
            else:
                value = text[i]
            
            ret.append(value)
        
        return ''.join(ret)
    
    def decrypt(self, text, shifts=[None]):
        '''
            It uses the shifts passed as parameters to unshift the text.
            If no shift passed, it will do all possible shifts.
            
            Keyword arguments:
            text -- Text to by decrypted
            shift -- list of possible shifts it is. If not specified, it will try every possible one.
        '''
        
        # If trying to decrypt a character, this work-around is needed
        if(not isinstance(text, str)):
            text = [text]
            
        # If trying to use one shift, this work-around is needed
        if(not isinstance(shifts, list)):
            shifts = [shifts]
        
        # If no shifts provided, try with eveything.
        if(shifts == [None]):
            shifts = [i+1 for i in range(25)]
        
        # The possibilities will be encryption making a full round 
        # (if it was encrypted with shift 20, encrypting it with 6 will make it go back to original) 
        possibles = [self.encrypt(text, 26-shift) for shift in shifts]
        
        # If there are more than one possibilities, return the array, if not, return the only value.
        return possibles if (isinstance(possibles, list) and len(possibles) > 1) else possibles[0]