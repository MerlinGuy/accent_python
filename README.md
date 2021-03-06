# accent_python
Python scripts for removing unicode accents from text.  The intention is to develop python code 
that works like the Apache Commons command **stripAccents()**


---

##Files (Python)

###accent.py
    
    Contains all the methods for stripping accents from text.  Also has a number of helper methods
    
### name.py
    
    Contains some experimental code for comparing names between stripped and non-stipped data.
    
### test/test_accent.py

    Contains a few unittests for running basic tests against accent.py
     
     
---

## Files (JSON)

###uni_names.json
    
    Test data file containing procycling riders whose names include unicode characters
    
### names.json

    Test data file contiaining procycling riders some of which include unicode characters
    
### test_data.json

    Test data file with both unicode names and their stripped results for testing
    
### test_data2.json

    Test data file with names and the location of the first unicode character for 
    testing **accent.first_unicode(text)** method
   
     
---
     
##accent.py
<br/>
**def strip_accent(text, match_upper=False, throw_error=False):**

    Strips all unicode characters from the text string which are in the ORDINAL lookup dict variable

    :param text: String with unicode characters to strip
    :param match_case: If True, the method will attempt to maintain upper case character words
    :param throw_error: If True, the method with raise an error for unicode it cannot replace
    :return: The passed in text with all unicode alphabet replaced with ascii matches

<br/>
**def upperit(text):**

    Method breaks text in to words and will upper() each if more than one uppercase letter is found

    :param text: String to scan and upper()
    :return: The text parameter with words uppercased.

<br/>
**def isletter(char):**

    :param char: Single character to check
    :return: Returns True if character is an ascii letter, otherwise False

<br/>
**def first_unicode(text):**

    :param text: String to scan for any character whose ordinal is above the ascii boundry
    :return: The position of the first unicode character, otherwise -1

<br/>
**def get_ordinals(char):**

    Function returns a list of all ORDINAL values whose character match the parameter ascii 'char'

    :param char: acsii character to scan for
    :return: List of matching ordinals

<br/>
**def strip_list(nlist):**

    Strips all unicode from a list of strings

    :param nlist: The list of strings to strip
    :return: A new list of stripped strings

<br/>
**def encode_ascii(uni):**

    Attempts to strip all unicode characters from text and then encodes as ascii

    :param text: String to strip and encode to ascii
    :return: Stripped and ascii encode string

    WARNING: this function will attempt to maintain case,
            will not raise error if unmatched unicode is found but
            should merely removed the character from the string

