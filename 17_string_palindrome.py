import string

ignored = string.punctuation + " "

def string_palindrome(string):
    clean_string = ""
    for i in string:
        clean_string += "" if i in ignored else i
    return clean_string.lower() == clean_string[::-1].lower()

#print string_palindrome("Go hang a salami I'm a lasagna hog.")

inp = raw_input("Enter String:  ")
print string_palindrome(inp)
