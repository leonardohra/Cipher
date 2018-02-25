# -*- coding: utf-8 -*-

from numeral_system import NumeralSystem

def split_by_index_number(text, limit):
    '''
        Splits a string by quantity of characters.
        
        Keyword arguments:
        
        text -- The text to be splitted
        limit -- quantity of letters each part must have at most
    '''
    result = []
    temp_text = ''
    
    # For each letter
    for i in range(len(text)):
        
        # Add the letter to "temp_text"
        temp_text += text[i]
        place = i+1
        
        # If temp text met the limit or its the last, add it to the return list and clean it
        if( (place % limit == 0) or (i + 1 == len(text)) ):
            result.append(temp_text)
            temp_text = ''
            
    return result

def convert_to_dec(number, base):
    '''
        Gets a number in base up to 16 and turn it to decimal
        
        Keyword arguments:
        
        number_str -- the string containing the number to be converted
        base -- numeral base it's in
    '''
    
    # If the number is already in decimal, no need to do anything
    if(base == 10):
        return number
        
    # This dictionary will be like {'0': '0' (...) 'A': '10' (...) 'F': '15'}
    base16 = dict()
    # Adding 0-9: For each number in range 0-9, create a dictionary with the number as key and value. 
    # Add this dictionary to the previous dictionary
    base16.update( { str(number): str(number) for number in range(10) } ) 
    # Adding A-F: For each number (number) in range 10-15 and letter (letter) in range 65-70 (A-F in ASCII), 
    # Create a dictionary with the letter as key and number as value. Add this dictionary to the previous dictionary
    base16.update( { chr(letter): str(number) for number, letter in zip( range(10, 16), range(65, 71) ) } ) 
    
    digits = []
    result = 0 
    # This is the number that will be used as base ( eg. base 8 will be 8^0 for unit, 8^1 for decimal (...) )
    b = base**0
    
    # For each number in the list of numbers, add it to "digits", converting the letters to numbers, if needed
    for i in range(len(number)):
        digits.append(base16[number[i]])
    
    # While there are still numbers to be converted, do the procedure 
    # (number*b, number times the base in the correct exponent)
    while(len(digits) > 0):
        temp_number = int(digits.pop())
        result += b*temp_number
        b *= base
    
    return str(result)

def convert_from_dec(number_str, base, digits):
    '''
        Converts a number from decimal to the base passed as parameter
        
        Keyword arguments:
        
        number_str -- the string containing the number to be converted
        base -- numeral base to be converted in
        digits -- how many digits form one number in this system
    '''
    
    # If number comes in base 10, no need to convert
    if(base == 10):
        return number_str.zfill(digits)
    
    # This dictionary will be like {'0': '0' (...) '10': 'A' (...) '15': 'F'}
    base16 = dict()
    # Adding 0-9: For each number in range 0-9, create a dictionary with the number as key and value. 
    # Add this dictionary to the previous dictionary
    base16.update( { str(number): str(number) for number in range(10) } ) 
    # Adding A-F: For each number (number) in range 10-15 and letter (letter) in range 65-70 (A-F in ASCII), 
    # Create a dictionary with the number as key and letter as value. Add this dictionary to the previous dictionary
    base16.update( { str(number): chr(letter) for number, letter in zip( range(10, 16), range(65, 71) ) } ) 
    
    # Get the number in int format
    number = int(number_str)
    finished = False
    new_number = []
    
    # While number isn't 0 (finished)
    while(not finished):
        # Get the quotient of number divided by base, this will be the next "number"
        quotient = number//base
        # And get the rest of the same division
        rest = number%base
        
        # The number in the new base will be a list of 'rest's inverted 
        # (all the digits are inserted on the beginning of the list)
        new_number.insert(0, base16[str(rest)])
        number = quotient
        
        if(number == 0):
            finished = True
            
    #Join the whole number in a string and return it. fill with 0 to the left (zfill) if needed
    result = "".join(new_number).zfill(digits)
    
    return result

