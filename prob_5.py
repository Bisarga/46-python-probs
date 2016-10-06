import string

all_letters = string.ascii_letters
vowels = ['a','e','i','o','u']
consonants = [chr for chr in all_letters if chr not in vowels]


def translate(s1):
    result = ""
    for c in s1:
        if c.lower() in consonants:
            result += c+'o'+c
        else:
            result += c
    return result
            
str1 = raw_input('Enter string : ')
print translate(str1)
        
